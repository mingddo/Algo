def low_and_up(words):
    result = ''
    for i in range(0, len(words)):
        if i % 2:
            result += words[i].upper()
        else:
            result += words[i]

    return result

print(low_and_up('apple'))
print(low_and_up('banana'))