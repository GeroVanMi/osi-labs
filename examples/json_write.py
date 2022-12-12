import json
import subprocess

data = [
    {
        "a": 5
    },
    {
        "q": [33, 34]
    }
]

with open('spio.json', 'w') as file:
    json.dump(data, file)

subprocess.run(["cat spio.json | json_pp > spio_formed.json"], shell=True)
