def lonely(numbers):
    result = [numbers[0]]
    for number in numbers:
        if number != result[-1]:
            result += [number]
        
    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))