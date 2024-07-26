import json


def check_values(tests):
    if "values" in tests:
        return tests["values"]


def rewrite(tests, values):
    for test in tests:
        for value in values:
            if test["id"] == value["id"]:
                test["value"] = value["value"]
            if check_values(test) is not None:
                rewrite(check_values(test), values)


with open(input("Путь к файлу с результатами тестов: "), "r") as f:
    values = json.load(f)["values"]
with open(input("Путь к файлу со структурой тестов: "), "r") as f:
    tests = json.load(f)


with open(input("Путь к формируемому файлу: "), "w") as f:
    rewrite(tests["tests"], values)
    # атрибут indent применен для удобства проверки файла
    json.dump(tests, f, indent=4)
