import itertools

#English letters: "ofqxvg"
englishLetters = ['f', 'v', 'g', 'o', 'x', 'q']
variations = itertools.permutations(englishLetters, 6)

#wordlist containing possible password
with open("wordlist.txt", "w") as f:
    for v in variations:
        f.write('{}\n'.format(''.join(v)))
        f.close