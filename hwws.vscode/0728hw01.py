def duplicated_letters(words):
    result = []
    for word in words:
        if words.count(f'{word}') > 1:
            if word in result:
                return result
            else:
                result += [word]
    return(result)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
