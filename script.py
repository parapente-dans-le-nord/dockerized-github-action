import os
import json
import random

repoPath = os.environ['GITHUB_WORKSPACE']
stepOutputPath = os.environ['GITHUB_OUTPUT']
issueBody = os.environ['issueBody']

print("Le body de l'issue")
print(issueBody)

for var in os.environ:
    print(var)

try:
    with open(f"{repoPath}/src/spots.json", 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"file {file} not found.")
except json.JSONDecodeError:
    print(f"json not valid in {file}.")

spotName = data['spots'][random.randint(0, len(data['spots']))]['name']
print(f"spotName is {spotName}")

# Parse body and build json
# Is spot already in list based on name ?
#spot already exist = exit 1 with message

with open(stepOutputPath, 'a') as file:
    file.write(f"spotName={spotName}")

