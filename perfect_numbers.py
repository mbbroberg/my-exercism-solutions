def classify(number):
    aliquot_sum = 0
    aliquot_series = []

    if number < 1:
        raise ValueError

    for n in range(1, number):
        if number % n == 0:
            aliquot_series.append(n)
            aliquot_sum += n

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
    # print(f'sum is {aliquot_sum} with series {aliquot_series}')


classify(-1)
classify(10)
