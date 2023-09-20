import enchant
import string
import random

string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'

wordguess = ""
knownlet = ""
d = enchant.Dict("en_US")
print("Try Donut and Raise as the first two words, then respond with any green letters, substitute any unkown letters with ?. For example: '?E??R'")
input1 = input()
print("what are the out of place letters?")
input2 = input()
letternum = 0

for v in input1:
    if v != "?":
        knownlet += str(v)

for x in input2:
    if x != "?":
        knownlet += str(x)

print("known letters:")
print(knownlet)

e = 1

guesses = []

print("-- SOLVING --")

while e in range(1,13000):
    hasallknownlet = True
    for i, w in enumerate(input1):
        if w == "?":
            randomlet = random.choice(string.ascii_lowercase)
            # print(randomlet)
            wordguess += randomlet
        else:
            # print(str(w))
            wordguess += str(w)
    # print(e)
    # print(wordguess)
    for f in knownlet:
        if (f in wordguess) == False:
            hasallknownlet = False
    if hasallknownlet:
        if (wordguess in guesses) == False:
            if d.check(wordguess):
                # print(wordguess)
                # print("hi")
                guesses.append(wordguess)
                e += 1
                print(wordguess)
    wordguess = ""
    # e += 1
print("-- FINISHED --")
print(guesses)

# print(wordguess)
