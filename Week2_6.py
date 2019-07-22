
letters =   {
             "a": 1,
             "b": 3,
             "c": 3,
             "d": 2,
             "e": 1,
             "f": 4,
             "g": 2,
             "h": 4,
             "i": 2,
             "j": 8,
             "k": 5,
             "l": 1,
             "m": 3,
             "n": 1,
             "o": 1,
             "p": 3,
             "q": 10,
             "r": 1,
             "s": 1,
             "t": 1,
             "u": 1,
             "v": 4,
             "w": 4,
             "x": 8,
             "y": 4,
             "z": 10
            }

print('What is your word? ')
word = input()

score = 0

for character in word:
    score = score + letters[character.lower()]

print('The score is : {0}'.format(score))
