import re

def validate_pin(pin):

    try:
        x=int(pin)
    except ValueError:
        print(False)

    try:
        if len(str(x)) == 4 or len(str(x))==6:
            print(True)
        else:
            print(False)
    except UnboundLocalError:
        print(False)

validate_pin("111111112")
