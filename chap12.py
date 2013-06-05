def anagrams(words):
    wordlist = open(words)
    anagramsList = {}
    for line in wordlist:
        word = line.strip().lower()
        s = list(word)
        s.sort()
        s = ''.join(s)
        if s in anagramsList:
            anagramsList[s].append(word)
        else:
            anagramsList[s] = [word]
    return anagramsList

def anagrams_in_order(anagrams):
    ordered = []
    for s in anagrams:
        ordered.append((len(anagrams[s]), s))
    ordered.sort(reverse=True)
    for a in ordered:
        print anagrams[a[1]]

print anagrams_in_order(anagrams('words.txt'))