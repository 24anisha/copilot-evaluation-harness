import os
import json
from score_scripts import test_score, fix_score, doc_score, model_handler
from absl import flags, app
import sys
from pathlib import Path

OUTPUT_DIR = "out"
REPOS_DIR = os.path.join(OUTPUT_DIR, "repos")
RESULTS_DIR = os.path.join(OUTPUT_DIR, "results")

FLAGS = flags.FLAGS

flags.DEFINE_string("metric", "fix", "Which metric to evaluate (e.g., fix, test_gen, or doc).")
flags.DEFINE_list("languages", ["python"], "Which coding language(s) to evaluate (comma-separated).")
flags.DEFINE_integer("n_cases", 10, "Number of test cases to run.")
flags.DEFINE_string("model_endpoint", None, "Which model endpoint to use (e.g., openai, anthropic, or gemini).")
flags.DEFINE_string("model_name", None, "Which model to use.")
flags.DEFINE_string("prompt", None, "An optional prompt to use with the model.")

def evaluate(data_dir, model):
    """
    Evaluates a model's performance on test cases by processing and scoring responses.

    Args:
        data_dir (str): Path to the directory containing test case JSON files.
        model (object): A model instance with a `call_model` method that generates responses.

    Returns:
        None: The function processes test cases, evaluates model responses, and 
              saves the results in the `RESULTS_DIR`.
    """

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
    # random.shuffle(data_dicts)
    
    languages = ['python', 'java', 'javascript', 'typescript', 'csharp'] if 'all' in FLAGS.languages else FLAGS.languages
    for test_case in data_dicts:
        if processed_cases >= FLAGS.n_cases:
            break
        if test_case["language"] in languages:

            # Get response from model
            model_input = create_model_input(test_case, data_dir)
            model_response = model.call_model(model_input)

            print("Model Input:\n" + model_input)
            print("\n Model Response:\n" + model_response)

            # Evaluate using specific dir process
            out_file = os.path.join(RESULTS_DIR, f"{test_case['case_id']}.json")
            result = process_func(test_case=test_case, model_response=model_response)
            with open(out_file, 'w') as f:
                json.dump(result, f, indent=4)
            processed_cases += 1

def create_model_input(test_case, data_dir):
    """
    Generates the model input string by formatting the prompt and code snippet.

    Args:
        test_case (dict): A dictionary containing information about the test case.
        data_dir (str): The directory containing relevant data files, used when extracting 
                        documentation lines if the metric is 'doc'.

    Returns:
        str: A formatted string containing the prompt and code snippet enclosed 
             within <prompt> and <code> tags.
    """
    input = (
        f"<prompt>\n"
        f"{FLAGS.prompt if FLAGS.prompt else create_prompt(test_case)}\n"
        f"</prompt>\n"
        f"<code>\n"
        f"{test_case['code_snippet'] if FLAGS.metric != 'doc' else extract_doc_lines(test_case, data_dir)}\n"
        f"</code>"
    )
    return input

def create_prompt(test_case):
    """
    Generates a prompt based on the specified metric and test case.

    Args:
        test_case (dict): A dictionary containing test case details, including
                          'command_specific_fields' with 'analyzer_error' for the 'fix' metric.

    Returns:
        str: A formatted prompt string based on the value of FLAGS.metric. The prompt will guide
             the model to generate code for a specific task:
             - 'fix': Prompt to fix an error in the code.
             - 'doc': Prompt to write a docstring for a function.
             - 'test': Prompt to write a unit test for a function.
    """
    if FLAGS.metric == 'fix':
        return f"Fix this error: {test_case['command_specific_fields']['analyzer_error']}. Provide only the fixed code, with no excess text."
    if FLAGS.metric == 'doc':
        return f"Write a docstring for the following lines {test_case['line_range']}. Only provide the docstring, with no excess text."
    if FLAGS.metric == 'test':
        return f"Write a unit test for the function {test_case['command_specific_fields']['method_name']}. Only provide the unit test, with no excess text."

def extract_doc_lines(test_case, data_dir):
    """
    Generates a prompt based on the specified metric and test case.

    Args:
        test_case (dict): A dictionary containing test case details, including
                          'command_specific_fields' with 'analyzer_error' for the 'fix' metric.

    Returns:
        str: A formatted prompt string based on the value of FLAGS.metric. The prompt will guide
             the model to generate code for a specific task:
             - 'fix': Prompt to fix an error in the code.
             - 'doc': Prompt to write a docstring for a function.
             - 'test': Prompt to write a unit test for a function.

    Notes:
        - The function relies on the global `FLAGS.metric` to determine which type of prompt to generate.
        - For 'fix', the prompt will request fixing an error and providing only the fixed code.
        - For 'doc', the prompt will ask for a docstring with no additional text.
        - For 'test', the prompt will instruct to write a unit test with no excess text.
    """
    file_path = os.path.join(data_dir, test_case["case_id"], test_case["file_path"])
    start_line, end_line = test_case["line_range"]
    with open(file_path, 'r') as file:
        lines = file.readlines()
        extracted_lines = lines[start_line:end_line +1]
        return '\n'.join(extracted_lines)
    
def process_fix(test_case, model_response):
    """
    Evaluates a model-generated fix by scoring it against the original test case.

    Args:
        test_case (dict): A dictionary containing test case details, including:
                          - "repo_name" (str): Name of the repository containing the file.
                          - "file_path" (str): Relative path to the file being analyzed.
                          - "command_specific_fields" (dict): Contains analysis task details.
                          - "language" (str): The programming language of the file.
        model_response (str): The model-generated fix or suggestion to be evaluated.

    Returns:
        dict: A dictionary containing the fix evaluation score and related details.
    """
    return fix_score.score_fix(
        base_path=os.path.join(REPOS_DIR, test_case["repo_name"]), 
        repo_name=test_case["repo_name"], 
        relative_path=Path(test_case["file_path"]), 
        task=test_case["command_specific_fields"]["static_analyzer"],
        language=test_case["language"], 
        model_response=model_response
    )

def process_test(test_case, model_response):
    """
    Evaluates a model-generated test case by scoring it against the original test case.

    Args:
        test_case (dict): A dictionary containing test case details, including:
                          - "repo_name" (str): Name of the repository containing the file.
                          - "file_path" (str): Relative path to the file being tested.
                          - "language" (str): The programming language of the file.
        model_response (str): The model-generated test case or response to be evaluated.

    Returns:
        dict: A dictionary containing the test evaluation score and related details.
    """
    return test_score.score_test(
        base_path=os.path.join(REPOS_DIR, test_case["repo_name"]),
        repo_folder_name=test_case["repo_name"],
        relative_path=Path(test_case["file_path"]),
        language=test_case["language"],
        model_response=model_response
    )
    
def process_doc(test_case, model_response):
    """
    Evaluates a model-generated documentation snippet by scoring it against the original test case.

    Args:
        test_case (dict): A dictionary containing test case details, including:
                          - "case_id" (str): Identifier for the test case.
                          - "file_path" (str): Relative path to the target file.
                          - "line_range" (tuple): A tuple (start_line, end_line) indicating 
                            the relevant range in the file.
                          - "language" (str): The programming language of the file.
        model_response (str): The model-generated documentation snippet to be evaluated.

    Returns:
        dict: A dictionary containing the documentation evaluation score and related details.
    """
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

    languages = FLAGS.languages

    for lang in languages:
        if lang not in ['python', 'java', 'javascript', 'typescript', 'csharp', 'all']:
            print(f"Error: Invalid language '{lang}'. Valid options are 'python', 'javascript', 'java', 'typescript', 'csharp', 'all'.")
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