def calculate_structure_sum(*data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i,(list, tuple, set)):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            summa += calculate_structure_sum(*i.items())
        elif isinstance(i, (int, float)):
            summa += 
        elif isinstance(i, str):
            summa += len(i)
    return summa


#print(*data_structure)

print(calculate_structure_sum([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]))
