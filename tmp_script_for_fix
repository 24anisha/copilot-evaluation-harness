import os
import json
import requests
from score_scripts import fix_score


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
        "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"
    }

    # Initialize evaluation results dictionary
    results = {}

    for test_case in data_dicts:
        # Extract data from test case
        base_path = test_case["repo_name"]
        relative_path = test_case["file_path"]
        language = test_case["language"]
        task = test_case["command_specific_fields"]["static_analyzer"]
        prompt = test_case["prompt"]
        code_snippet = test_case["code_snippet"]
        case_id = test_case["case_id"]
        line_range = test_case["line_range"]

        # Pass data through model
        response = requests.post(model_endpoint, headers=headers, json=json.dumps({"inputs": "Prompt: " + prompt + " Code: " + code_snippet}))
        
        # Get response from model
        response_data = response.json()

        # Evaluate with score scripts
        fix_result = fix_score.score_fix(base_path, relative_path, language, response_data, task, line_range)

        results[case_id] = {"fix_result": fix_result}

    # Save the results to file
    output_file = "evaluation_results.json"
    with open(output_file, 'w') as out_file:
        json.dump(results, out_file, indent=4)

if __name__ == "__main__":
    # Example usage
    data_dir = "data/fix"
    model_endpoint = "https://api-inference.huggingface.co/models/your-model-name" #huggingface model endpoint

    evaluate(data_dir, model_endpoint)