import datetime

def add(moment):
    try:
        g = datetime.timedelta(seconds=10**9)
        return moment + g
    except ValueError:
        print('Invalid input. Please try again.')
    else:
        print('Something went wrong that wasn\'t a ValueError. Beats me. Try again.')