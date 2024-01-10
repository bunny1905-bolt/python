def probability_calculator(favorable_outcomes, total_outcomes):
    if total_outcomes <= 0:
        return "Error: Total outcomes must be greater than 0."

    probability = favorable_outcomes / total_outcomes
    return probability

# Example usage:
favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
total_outcomes = int(input("Enter the total number of possible outcomes: "))

result = probability_calculator(favorable_outcomes, total_outcomes)
print(f"The probability of the event is: {result}")

