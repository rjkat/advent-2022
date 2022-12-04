def print_formula(letter):
    if letter is None:
        return 'NA()'

    if letter == "z":
        next_letter = "A"
    elif letter == "Z":
        next_letter = None
    else:
        next_letter = chr(ord(letter) + 1)

    s = f'IF(GT(IFERROR(FIND("{letter}", $B2) + FIND("{letter}", $C2) + FIND("{letter}", $D2), -1), 0), "{letter}", {print_formula(next_letter)})'

    return s


s = print_formula("a")
print(s)