def my_sort(numbers):
    odd = [n for n in numbers if n % 2 != 0]
    even = [n for n in numbers if n % 2 == 0]
    return sorted(odd) + sorted(even)


print(my_sort([3, 1, 5, 10, 6, 9, 7, 2, 8, 4]))