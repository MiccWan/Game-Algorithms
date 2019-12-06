import json
with open("evalResult.json", "r") as jsonFile:
    data = json.load(jsonFile)

print(sum(data.values())/1296)
print(len(data))