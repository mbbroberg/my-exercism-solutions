def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    number = int(number)
    output = ""

    for i in factors:
        if number % i == 0:
            output+=factors[i]
    
    if len(output) > 0:
        return output
    else:
        return str(number)