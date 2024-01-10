def add_time(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))

    total_minutes = h1 * 60 + m1 + h2 * 60 + m2
    new_hours, new_minutes = divmod(total_minutes, 60)

    return f"{new_hours:02d}:{new_minutes:02d}"

def subtract_time(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))

    total_minutes = h1 * 60 + m1 - (h2 * 60 + m2)
    new_hours, new_minutes = divmod(total_minutes, 60)

    return f"{new_hours:02d}:{new_minutes:02d}"

def time_calculator(time1, operator, time2):
    if operator not in ('+', '-'):
        return "Error: Operator must be '+' or '-'."

    if operator == '+':
        result = add_time(time1, time2)
    else:
        result = subtract_time(time1, time2)

    return result

# Example usage:
time1 = "12:30"
operator = "+"
time2 = "4:45"

result = time_calculator(time1, operator, time2)
print(result)
