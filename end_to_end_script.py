'''
Write a script that can do the end-to-end inference and evaluation on the test cases in this repository using the score scripts and data. 
It can assume the model endpoint is a huggingface model.
'''

# Iterate through data
import os
import json
import requests

base_dir = "data/fix"
data_dicts = []

# Iterate through the data
for file_name in os.listdir(base_dir):

    file_path = os.path.join(base_dir, file_name)

    if os.path.isfile(file_path) and file_name.endswith('.json'):

        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
            data_dicts.append(data)

# Connect to model endpoint + get headers
model_endpoint = "https://api-inference.huggingface.co/models/your-model-name" #huggingface model endpoint
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"
}

# Initialize evaluation results dictionary
results = {}

for test_case in data_dicts:
    # Pass data through model
    response = requests.post(model_endpoint, headers=headers, json=json.dumps({"inputs": test_case["code_snippet"]}))
    
    # Get response from model
    response_data = response.json()

    # TODO: Evaluate using score_scripts
    result = 

    results[test_case["case_id"]] = result

# Save the results to file
output_file = "evaluation_results.json"
with open(output_file, 'w') as out_file:
    json.dump(results, out_file, indent=4)