def slices(source, length):

    if source == "":
        raise ValueError("Source series cannot be blank.")
    elif length < 0:
        raise ValueError("Length of slices cannot be less than 1.")
    elif length > len(source):
        raise ValueError("Source length needs to be longer than your requested slice.")

    source_length = len(source)

    return [
        source[index : index + length] for index in range(source_length - length + 1)
    ]


print(slices("123456", 3))
