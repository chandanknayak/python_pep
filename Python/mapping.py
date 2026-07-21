def count_numbers(numbers):
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return counts


nums = [1, 2, 2, 3, 1, 4, 2]
result = count_numbers(nums)

print(result)

def grade():
    
















