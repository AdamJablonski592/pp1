import json

with open("test.json", "r") as f:
    data = json.load(f)
    i = 0
    while i < len(data):
        data_row = data[i]
        for k, v in data_row.items():
            print(k, ":", v)
        i += 1