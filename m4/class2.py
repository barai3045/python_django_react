# conditions 

marks = 85
result = ""

if marks < 33:
    result = "Failed"
elif marks > 80:
    result = "You passed with A+"
else:
    result = "Passed"

#print(result)


# match statement

vowel = 't'

match vowel:
    case 'a': print("Vowel Alphabet")
    case 'e': print("Vowel Alphabet")
    case 'i': print("Vowel Alphabet")
    case 'o': print("Vowel Alphabet")
    case 'u': print("Vowel Alphabet")
    case _: print("Simple Alphabet")
    