

def remove_vowels(string):
    vowels=['a','e','o','u','i','A','E','O','U','I']
    for i in string:
        if i in vowels:
            string = string.replace(i,'')

    return string

remove_vowel("This is so fcking awesome")

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU") # best practise award .. check out .translate method
