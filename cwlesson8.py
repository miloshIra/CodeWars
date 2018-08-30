
#my solution ... :(

def create_phone_number(n):
    z = (n[0:3])
    x = "("+ (''.join(str(z) for z in z)) + ")"

    a = (n[3:6])
    b = ''.join(str(a) for a in a)

    c = (n[6:])
    d = ''.join(str(c) for c in c)

    number = x +" "+ b +"-"+ d
    return number

#beast guy solution :D

def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

  # This is awesome and i should of tought of this!
