import json

values_file, tests_file, report_file = input(), input(), input()


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


with open(values_file, "r") as f:
    values = json.load(f)["values"]
with open(tests_file, "r") as f:
    tests = json.load(f)


with open(report_file, "w") as f:
    rewrite(tests["tests"], values)
    # атрибут indent применен для удобства проверки файла
    json.dump(tests, f, indent=4)
