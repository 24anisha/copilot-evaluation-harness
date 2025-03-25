## Copilot Evaluation Harness
Dataset and Evaluation Metrics for the [Copilot Evaluation Harness Paper](https://arxiv.org/pdf/2402.14261).

This repository is a work in progress. Currently, a sample of data from one of our five evaluation metrics is available to use.
The data in this repository is parsed and utilized in tandem with [plum](https://github.com/24anisha/plum), which we use to programmatically interact with repositories (set up environment, run tests, change code, etc).

### Installation
- Copilot Evaluation Harness relies on the plum package
- Go to https://github.com/24anisha/plum and download the repository. cd into the repo, create a conda environment, and run 
`
pip install -e .
`
.
- Then open this repository, activate the plum conda environment, and again run 
`
pip install -r requirements.txt
`
.

### Ingestion
The following code snippet allows you to iterate through the data for a specific evaluation metric and read the JSON file for each test case into a dictionary
```python
import os
import json

base_dir = "data/fix"
data_dicts = []
# Loop through all cases in the fix metric
for file_name in os.listdir(base_dir):

    file_path = os.path.join(base_dir, file_name)

    if os.path.isfile(file_path) and file_name.endswith('.json'):

        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
            data_dicts.append(data)

```

### Data Structure
Each JSON test case in the data has the following information:

```
{
    "case_id": unique case number identifier in the form "case-{case_number}"
    "repo_name": username/reponame of git repository
    "file_path": path to the file relative to the case repository where the code snippet exists in the repo
    "code_snippet": code selection that is passed to the model as context
    "line_range": [
        starting_line,
        ending_line
    ],
    # the command specific fields are different for each evaluation metric. These are the fields for the bug fixing command
    "command_specific_fields": {
        "static_analyzer": static analyzer used,
        "rule": analyzer error rule name,
        "analyzer_error": full text of error.
    }
    "language": coding language
}
```
Note each Doc case also has a corresponding code file

### Accessing the LLM Endpoint
Our end to end script is currently structured to handle requests to the Anthropic sonnet 3.5 model. To send requests to the model,
set your own api key to `API_KEY` with 
`
export API_KEY=<api key>
`
.
### Running the Pipeline

To run the pipeline, install the required dependencies from pyproject.toml and 



then run the following command:

```
python end_to_end_script.py
```
with the following flags:

- `--metric` (required): Choose from `fix`, `test_gen`, or `doc` to specify the metric for the pipeline.
- `--languages` (required): Specify the programming languages (e.g., `python`, `javascript`, etc.).
- `--n_cases` (required): The number of test cases to run.
- `--model_endpoint` (required): Choose from `Anthropic`, `OpenAI`, `Gemini`, or `Azure` to specify the endpoint for the model.
- `--model_name` (required): Specify the model's name (e.g. `claude-3-5-sonnet-latest`).
- `--prompt` (optional): Create your own prompt/context for the model.

#### Example Usage:

To run the pipeline for fixing issues in Python and JavaScript, with 10 test cases:
example: 

```
python end_to_end_script.py --metric=fix --languages=python,javascript --n_cases=10 --model_endpoint=Anthropic --model_name=claude-3-5-sonnet-latest
```
In this example:
- `--metric=fix` specifies the "fix" metric.
- `--languages=python,javascript` indicates the languages to be used in the pipeline.
- `--n_cases=10` runs the pipeline for 10 test cases.
- `--model_endpoint=Anthropic` indicates the endpoint for the model.
- `--model_name=claude-3-5-sonnet-latest` specifies the model's name.

