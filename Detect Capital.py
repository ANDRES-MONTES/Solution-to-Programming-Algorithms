def detectCapitalUse(word: str) -> bool:
    if word.isupper():
        return True
    elif word.islower():
        return True
    else:
        counter = 0
        for i in word:
            if i.isupper():
                counter += 1
        if (counter > 1) or (word[0].islower()):
            return False
        return True
        

if __name__ == '__main__':
    word = "USA"
    result = detectCapitalUse()
    print(result)