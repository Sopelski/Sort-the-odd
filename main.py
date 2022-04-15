'''You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.'''

def sort_array(source_array):
    odd_numbers =[]
    b = 0
    for a in source_array:
        if a % 2 != 0:
            odd_numbers.append(a)
    odd_numbers.sort()
    while b < len(odd_numbers)-1:
        for index,c in enumerate(source_array):
            if c % 2 != 0:
                source_array[index] = odd_numbers[b]
                b +=1

    return print(source_array)

sort_array([5, 3, 1, 8, 0])