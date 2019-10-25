def is_armstrong_number(number):
    digits = list(str(number))  # create an array of strings out of the number
    power = len(digits)  # power is equivalent to the length of the input
    armstrong_sum = 0

    for i in range(len(digits)):
        armstrong_sum += int(digits[i]) ** power
        # troubleshooting:
        # print(f"digit {i} is {digits[i]} to the power of {power}")
    # troubleshooting:
    # print(s)
    return int(number) == armstrong_sum
