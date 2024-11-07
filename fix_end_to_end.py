import os
import json
from score_scripts import fix_score
from pathlib import Path
import anthropic



def evaluate(data_dir, model_endpoint):
    data_dicts = []
    # Iterate through the data
    for file_name in os.listdir(data_dir):

        file_path = os.path.join(data_dir, file_name)

        if os.path.isfile(file_path) and file_name.endswith('.json'):

            with open(file_path, 'r') as data_file:
                data = json.load(data_file)
                data_dicts.append(data)

    # Initialize evaluation results dictionary
    results = {}

    for test_case in data_dicts:
        # Get response from model
        response_data = pass_through_model(model_endpoint, test_case["prompt"], test_case["code_snippet"])

        # Evaluate using specific dir process
        results[test_case["case_id"]] = process_fix(test_case, response_data)

    # Save the results to file
    output_file = "evaluation_results.json"
    with open(output_file, 'w') as out_file:
        json.dump(results, out_file, indent=4)

def process_fix(test_case, model_response):
    return fix_score.score_fix(Path(base_path), test_case["repo_name"], Path(test_case["file_path"]),model_response, test_case["command_specific_fields"]["static_analyzer"], test_case["language"])

def pass_through_model(model_endpoint, prompt, code_snippet):
    message = model_endpoint.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content":  "Prompt: " + "fix this code." + " Code: " + code_snippet} #replace long string with prompt when data is ready
        ]
    )
    return message.content[0].text #return string
    
if __name__ == "__main__":
    # Example usage
    data_dir = "data/demo_json"
    model_endpoint = anthropic.Anthropic(
        api_key="",
        )
    base_path = os.getcwd()

    evaluate(data_dir, model_endpoint)