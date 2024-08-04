def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) < 1:
        return
    elif len(str_number) == 1:
        return first
    result = first * get_multiplied_digits(int(str_number[1:]))
    return result
print(get_multiplied_digits(897))
