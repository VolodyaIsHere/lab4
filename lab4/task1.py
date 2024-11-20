# TODO решите задачу
import json

def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)
    ssum = sum([dicts["score"] * dicts["weight"] for dicts in data])
    return round(ssum, 3)


print(task())
