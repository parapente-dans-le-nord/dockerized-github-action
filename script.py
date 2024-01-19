import os
import json
import random

repoPath = os.environ['GITHUB_WORKSPACE']
stepOutputPath = os.environ['GITHUB_OUTPUT']

try:
    with open(f"{repoPath}/src/spots.json", 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"file {file} not found.")
except json.JSONDecodeError:
    print(f"json not valid in {file}.")

spotName = data['spots'][random.randint(0, len(data['spots']))]['name']
print(f"spotName is {spotName}")

with open(stepOutputPath, 'a') as file:
    file.write(f"spotName={spotName}")

