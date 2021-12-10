def find_decimal_length(n):
    string = str(n)
    return len(string[string.find("."):]) - 1


print(find_decimal_length(0))
