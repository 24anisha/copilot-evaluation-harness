import os
import json
import shutil

SOURCE_DIR = "test_gen_java"
DEST_BASE = "test_gen_java_new"

i = 742

for dirname in os.listdir(SOURCE_DIR):
    dir_path = os.path.join(SOURCE_DIR, dirname)
    case_id = f"case-{i}"
    dest_folder = DEST_BASE
    os.makedirs(dest_folder, exist_ok=True)

    if os.path.isdir(dir_path):
        output_filename = os.path.join(dest_folder, f"{case_id}.json")
        output = {}
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            if file.endswith("state.json"):
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)

                    output.update({
                        "case_id": case_id,
                        "file_path": data["activeTextEditor"]["documentFilePath"], 
                        "line_range": [
                            data["activeTextEditor"]["selections"][0]["active"]["line"],
                            data["activeTextEditor"]["selections"][0]["anchor"]["line"]
                        ],
                        "language": data["activeTextEditor"]["languageId"]
                    })

                except (json.JSONDecodeError, IOError, KeyError) as e:
                    print(f"Error processing {file_path}: {e}")
            elif file.endswith("conversation.json"):
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)

                    output.update({
                        "repo_name": data[0]["repo_folder"].replace("--", "/"), #double check
                        "command_specific_fields": {
                            "method_name": data[0]["original_method_name"]
                        },
                        "code_snippet": data[0]["original_method"]
                    })

                except (json.JSONDecodeError, IOError, KeyError) as e:
                    print(f"Error processing {file_path}: {e}")
        # sort output
        order = ["case_id", "repo_name", "file_path",
    "code_snippet", "line_range", "command_specific_fields", "language"]
        output = {i: output[i] for i in order}
        with open(output_filename, "w") as out_file:
            json.dump(output, out_file, indent=4)

    i += 1  # Increment case number once per subdirectory

print("Done.") 