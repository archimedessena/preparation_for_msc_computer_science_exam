numbers = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8, 9, 10,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def count_frequency(num):
    frequency = {}
    for n in num:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    return frequency

frequency_result = count_frequency(numbers)
print(frequency_result)  # Output: {1: 2, 2: