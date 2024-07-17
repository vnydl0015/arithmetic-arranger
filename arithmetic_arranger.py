import re

def arithmetic_arranger(problems, play=None):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row, second_row, operator, result = [], [], [], []
    for equation in problems:
        if '*' in equation or '/' in equation:
            return "Error: Operator must be '+' or '-'."
        if play == True:
            result.append(str(eval(equation)))

        for char in equation:
            if char in ('+', '-'):
                operator.append(char)
            elif char != ' ' and not char.isdigit():
                return 'Error: Numbers must only contain digits.'

        equation = re.split(', |-|\+', equation)
        if len(equation[0].strip()) > 4 or len(equation[1].strip()) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        first_row.append(equation[0].strip())
        second_row.append(equation[1].strip())

    line1, line2, line3, line4 = '', '', '', ''
    for i, j, k in zip(first_row, operator, second_row):
        max_spacing = max(map(len, (i, k))) + 2
        line1 += f"{i:>{max_spacing}}    "
        line2 += f"{j} {k:>{max_spacing - 2}}    "
        line3 += "-" * max_spacing + "    "
        if play == True:
            line4 += f"{result[0]:>{max_spacing}}    "
            result = result[1:]
    final = f"{line1.rstrip()}\n{line2.rstrip()}\n{line3.rstrip()}"
    if play == True:
        final += f"\n{line4.rstrip()}"
    return final
