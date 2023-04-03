while True:
    try:
        lower, upper, digit, space = 0, 0, 0, 0
        for char in input():
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1
        print(lower, upper, digit, space)
    except EOFError:
        break