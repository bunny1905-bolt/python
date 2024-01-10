def arithmetic_formatter(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    formatted_problems = ""
    line1 = line2 = line3 = line4 = ""

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        max_length = max(len(operand1), len(operand2)) + 2
        line1 += operand1.rjust(max_length) + "    "
        line2 += operator + operand2.rjust(max_length - 1) + "    "
        line3 += "-" * max_length + "    "

        result = str(eval(problem))
        line4 += result.rjust(max_length) + "    "

    formatted_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    if display:
        formatted_problems += "\n" + line4.rstrip()

    return formatted_problems

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_formatter(problems, True))