calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    string = len(string),string.upper(),string.lower()
    return string
print(string_info("тест"))
print(string_info("FC Dynamo Moscow"))
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.upper() == i.upper():
                Flag = True
                return Flag
    Flag = False
    return Flag
print(is_contains("Петя", ["Юля", "Витя", "Аня", "Маша"]))
print(calls)
