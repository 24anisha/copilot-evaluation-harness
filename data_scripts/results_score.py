import os
from pathlib import Path
import json

data_dir = os.path.join("./out/results/", "doc_2025-03-13")
total = 0
passed = 0
for file_name in os.listdir(data_dir):
    try:
        with open(f"{data_dir}/{file_name}/result.json", "r") as file:
            test_case = json.load(file)
            passed += test_case["success"]
            total += 1
    except:
        continue

print(f"Total: {total}, Passed: {passed}, Percentage: {passed/total*100}%")