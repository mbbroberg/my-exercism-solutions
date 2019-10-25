def two_fer(name="you"):
    try:
        return f"One for {name}, one for me."
    except ValueError:
        print("I can't two-fer that type of value. Please use a person's name.")
