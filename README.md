## Copilot Evaluation Harness
Dataset and Evaluation Metrics for the [Copilot Evaluation Harness Paper](https://arxiv.org/pdf/2402.14261)

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
    "repo_name": username/reponame of git repository. For this repository, it would be 24anisha/copilot-evaluation-harness
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
}
```
