import re

def validate_pin(pin):

      pattern=re.compile("(\d\d\d\d)")
      asd=pattern.search(pin)
      asdf=asd.group()
      if asd == None:
          print(True)
      else:
          print(False)

validate_pin("112")
