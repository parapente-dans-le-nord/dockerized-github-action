import os
import json
import random
from urllib.parse import urlparse

repoPath = os.environ.get('GITHUB_WORKSPACE','.')
stepOutputPath = os.environ.get('GITHUB_OUTPUT',None)
issueBody = os.environ.get('INPUT_ISSUE_BODY',None)

def exitError(reason):
    with open(stepOutputPath, 'a') as file:
        file.write("docker-ga-action-error=true\n")
        file.write(f"docker-ga-action-reason={reason}\n")
        exit(0)

try:
    with open(f"{repoPath}/src/spots.json", 'r') as file:
        spots = json.load(file)
except FileNotFoundError:
    print(f"file {file} not found.")
except json.JSONDecodeError:
    print(f"json not valid in {file}.")

def parseSpot(body) :
    spotStart = False
    spot = {}
    for line in body.split('\n') :
        if "```" in line :
            spotStart = not spotStart
        elif spotStart :
            spot[line.split(':',1)[0].strip()] = line.split(':',1)[1].strip()
    
    if spot['type'] is None or spot['type'] not in ['bord-de-mer','plaine','treuil']:
        exitError("La variable type doit etre renseigné et avoir comme valeur bord-de-mer, plaine ou treuil")
    
    if spot['type'] == "bord-de-mer" and spot.get('tideTableUrl',None) is None:
        exitError("le type etant bord-de-mer, il faut renseigner **tideTableUrl** avec l'url des marées")
    
    if spot['localisation'] is None or spot['localisation'] not in ['nord','autre']:
        exitError("la variable localisation prend comme valeur nord ou autre")

    if spot['type'] == "bord-de-mer" :
        spot['needSeaCheck'] = True
    
    spot['maxSpeed'] = int(spot['maxSpeed'])
    spot['minSpeed'] = int(spot['minSpeed'])

    spot['goodDirection'] = spot['goodDirection'].split()
    spot['excludeDays'] = [int(value) for value in spot['excludeDays'].split()]
    spot['monthsToExcludes'] = [int(value) for value in spot['monthsToExcludes'].split()]
    spot['url'] = os.path.basename(urlparse(spot['url']).path)
    spot['tideTableUrl'] = spot['tideTableUrl'].split('/')[-2] + '/'

    return spot

def checkSpotAlreadyPresent(spots,spot):
    newSpotName = spot['name']
    for spot in spots['spots']:
        if newSpotName == spot['name'] :
            return True
    return False

spot = parseSpot(issueBody)

if checkSpotAlreadyPresent(spots,spot):
    reason = f"Le spot **{spot['name']}** existe déjà. Si vous vouliez le mettre à jour, il faut renseigner UPDATE au lieu de CREATE. Vous pouvez editer l'issue en corrigeant pour relancer le processus."
    exitError(reason)

spots['spots'].append(spot)

try:
    with open(f"{repoPath}/src/spots.json", 'w') as file:
        json.dump(spots, file, indent=2)
except FileNotFoundError:
    exitError(f"file {file} not found.")

with open(stepOutputPath, 'a') as file:
        file.write("docker-ga-action-error=false\n")
        exit(0)

