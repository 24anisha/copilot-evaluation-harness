import os
import json
import requests
from score_scripts import test_score


def evaluate(data_dir, model_endpoint):
    data_dicts = []
    # Iterate through the data
    for file_name in os.listdir(data_dir):

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

    for test_case in data_dicts[:3]:
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
        results[test_case["case_id"]] = process_test(test_case, response_data)

    # Save the results to file
    output_file = "evaluation_results.json"
    with open(output_file, 'w') as out_file:
        json.dump(results, out_file, indent=4)

def process_test(test_case, model_response):
    print(base_path)
    print(test_case["repo_name"])
    return test_score.score_test(base_path, test_case["repo_name"], test_case["file_path"], test_case["language"], model_response)
    

def pass_through_model(model_endpoint, headers, prompt, code_snippet):
    response = requests.post(model_endpoint, headers=headers, json={"inputs": "Prompt: " + prompt + " Code: " + code_snippet})
    response_data = response.json()
    return response_data["generated_text"] #return string
    
if __name__ == "__main__":
    # Example usage
    data_dir = "data/test_gen"
    model_endpoint = "https://api-inference.huggingface.co/models/your-model-name" #huggingface model endpoint
    base_path = os.getcwd()

    evaluate(data_dir, model_endpoint)