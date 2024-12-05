import os
import json
import requests
from score_scripts import test_score, fix_score, doc_score, model_handler
from absl import flags, app
import sys
import anthropic
from pathlib import Path
import random

FLAGS = flags.FLAGS

flags.DEFINE_string("metric", "fix", "Which metric to evaluate (e.g., fix, test_gen, or doc).")
flags.DEFINE_list("languages", ["python"], "Which coding language(s) to evaluate (comma-separated).")
flags.DEFINE_integer("n_cases", 10, "Number of test cases to run.")
flags.DEFINE_string("model_endpoint", None, "Which model endpoint to use (e.g., openai, anthropic, or gemini).")
flags.DEFINE_string("model_name", None, "Which model to use.")
flags.DEFINE_string("prompt", None, "An optional prompt to use with the model.")

def evaluate(data_dir, model):
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

    # Initialize evaluation results dictionary
    processed_cases = 0
    random.shuffle(data_dicts)
    for test_case in data_dicts:
        if processed_cases >= FLAGS.n_cases:
            break
        if test_case["language"] in FLAGS.languages:

            # Get response from model
            model_input = create_model_input(test_case, data_dir)
            model_response = model.call_model(model_input)

            # Evaluate using specific dir process
            out_file = "out/results/" + test_case["case_id"] + ".json"
            result = process_func(test_case=test_case, model_response=model_response)
            with open(out_file, 'w') as out_file:
                json.dump(result, out_file, indent=4)
            processed_cases += 1

def create_model_input(test_case, data_dir):
    #Prompt:
    input = (
        f"<prompt>\n"
        f"{FLAGS.prompt if FLAGS.prompt else test_case['prompt']}\n"
        f"</prompt>\n"
        f"<code>\n"
        f"{test_case['code_snippet'] if FLAGS.metric != 'doc' else extract_doc_lines(test_case, data_dir)}\n"
        f"</code>"
    )
    return input

def extract_doc_lines(test_case, data_dir):
    file_path = os.path.join(data_dir, test_case["case_id"], test_case["file_path"])
    start_line, end_line = test_case["line_range"]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        extracted_lines = lines[start_line:end_line +1]
        return '\n'.join(extracted_lines)
    
def process_fix(test_case, model_response):
    return fix_score.score_fix(
        base_path=Path(base_path), 
        repo_name=test_case["repo_name"], 
        relative_path=Path(test_case["file_path"]), 
        task=test_case["command_specific_fields"]["static_analyzer"],
        language=test_case["language"], 
        model_response=model_response
    )

def process_test(test_case, model_response):
    return test_score.score_test(
        base_path=base_path,
        repo_folder_name=test_case["repo_name"],
        relative_path=Path(test_case["file_path"]),
        language=test_case["language"],
        model_response=model_response
    )
    
def process_doc(test_case, model_response):
    return doc_score.score_doc(
        base_path=base_path,
        start_line=test_case["line_range"][0],
        language=test_case["language"],
        relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
        model_output=model_response
    )

process_dir = {"fix": process_fix, "test_gen": process_test, "doc": process_doc}

def main(_):

    if FLAGS.metric not in ['fix', 'test_gen', 'doc']:
        print(f"Error: Invalid metric '{FLAGS.metric}'. Valid options are 'fix', 'test_gen', or 'doc'.")
        sys.exit(1)
    
    if not FLAGS.languages:
        print("Error: You must specify at least one language.")
        sys.exit(1)

    language_dir = ['python', 'java', 'javascript', 'typescript', 'csharp']
    languages = language_dir if 'all' in FLAGS.languages else FLAGS.languages.split(",")

    for lang in languages:
        if lang not in ['python', 'java', 'javascript', 'typescript', 'csharp']:
            print(f"Error: Invalid language '{lang}'. Valid options are 'python', 'javascript', 'java', 'typescript', 'csharp'.")
            sys.exit(1)
    
    if not FLAGS.model_endpoint:
        print("Error: You must specify a model endpoint.")
        sys.exit(1)
    
    if not FLAGS.model_name:
        print("Error: You must specify a model name.")
        sys.exit(1)
    
    if FLAGS.n_cases < 1:
        print("Error: The number of test cases must be at least 1.")
        sys.exit(1)

    # Determine the base directory for loading test cases based on the selected metric
    data_dir = os.path.join('data', FLAGS.metric)

    if not os.path.exists(data_dir):
        print(f"Error: The data directory '{data_dir}' does not exist.")
        sys.exit(1)

    # create an environment variable with which to pass in the API key
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: The environment variable 'API_KEY' is not set.")
        sys.exit(1)
    
    model = model_handler.ModelHandler(model_endpoint=FLAGS.model_endpoint, model_name=FLAGS.model_name)

    evaluate(data_dir, model)


if __name__ == "__main__":
    base_path = os.getcwd()
    app.run(main)