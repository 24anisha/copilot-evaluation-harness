import os
import json
import requests
from score_scripts import test_score, fix_score, doc_score
from absl import flags, app
import sys

FLAGS = flags.FLAGS

flags.DEFINE_string("metric", "fix", "Which metric to evaluate (e.g., fix, test, or doc).")
flags.DEFINE_list("language", ["python"], "Which coding language(s) to evaluate (comma-separated).")
flags.DEFINE_integer("n_cases", 10, "Number of test cases to run.")

def evaluate(data_dir, model_endpoint):
    process_func = process_dir[FLAGS.metric]

    data_dicts = []
    # Iterate through the data
    for file_name in os.listdir(data_dir):
        if FLAGS.metric == 'doc':
            folder_path = os.path.join(data_dir, file_name)

            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path) and file_name.endswith('.json'):

                    with open(file_path, 'r') as data_file:
                        data = json.load(data_file)
                        data_dicts.append(data)

        else:
            file_path = os.path.join(data_dir, file_name)

            if os.path.isfile(file_path) and file_name.endswith('.json'):

                with open(file_path, 'r') as data_file:
                    data = json.load(data_file)
                    data_dicts.append(data)

    # Connect to model endpoint + get headers
    headers = {
        "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}",
        "Content-Type": "application/json"
    }

    # Initialize evaluation results dictionary
    results = {}

    for test_case in data_dicts[:FLAGS.n_cases]:
        # Get response from model
        #response_data = pass_through_model(model_endpoint, headers, test_case["prompt"], test_case["code_snippet"])
        response_data =  """
            Here is a test case for the function:

        ```python
        def test_example():
        assert 1 == 1
        ```
        """

        # Evaluate using specific dir process
        results[test_case["case_id"]] = process_func(test_case, response_data)

    # Save the results to file
    output_file = "evaluation_results.json"
    with open(output_file, 'w') as out_file:
        json.dump(results, out_file, indent=4)

def process_fix(test_case, model_response):
    return fix_score.score_fix(base_path=base_path, repo_name=test_case["repo_name"], relative_path=test_case["file_path"], task=test_case["command_specific_fields"]["static_analyzer"], language=test_case["language"], model_response=model_response)

def process_test(test_case, model_response):
    return test_score.score_test(base_path=base_path, repo_folder_name=test_case["repo_name"], relative_path=test_case["file_path"], language=test_case["language"], model_response=model_response)
    
def process_doc(test_case, model_response):
    import pdb; pdb.set_trace()
    return doc_score.score_doc(base_path=base_path, start_line=test_case["line_range"][0], language=test_case["language"], relative_file_path=test_case["case_id"] + "/" + test_case["file_path"], model_output=model_response)

process_dir = {"fix": process_fix, "test_gen": process_test, "doc": process_doc}

def pass_through_model(model_endpoint, headers, prompt, code_snippet):
    response = requests.post(model_endpoint, headers=headers, json={"inputs": "Prompt: " + prompt + " Code: " + code_snippet})
    response_data = response.json()
    return response_data["generated_text"] #return string
    

def main(_):

    if FLAGS.metric not in ['fix', 'test', 'doc']:
        print(f"Error: Invalid metric '{FLAGS.metric}'. Valid options are 'fix', 'test', or 'doc'.")
        sys.exit(1)
    
    if not FLAGS.language:
        print("Error: You must specify at least one language.")
        sys.exit(1)

    # Determine the base directory for loading test cases based on the selected metric
    if FLAGS.metric == 'test': FLAGS.metric = 'test_gen'
    data_dir = os.path.join('data', FLAGS.metric)
    if not os.path.exists(data_dir):
        print(f"Error: The data directory '{data_dir}' does not exist.")
        sys.exit(1)

    model_endpoint = "https://api-inference.huggingface.co/models/your-model-name" #huggingface model endpoint
    evaluate(data_dir, model_endpoint)

if __name__ == "__main__":
    base_path = os.getcwd()
    app.run(main)