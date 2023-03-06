while True:
    posled = input('Введите последовательность чисел через пробел: ').split(' ')
    try:
        for i in range(len(posled)):
            posled[i] = int(posled[i])
        break
    except ValueError:
        print('Были введены не числа')

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

posled = merge_sort(posled)
while True:
    chislo = int(input('Введите число, не являющееся минимальным и не превосходящее максимальное значение'
                       ' во введенной последовательности: '))
    if chislo > posled[-1] or chislo <= posled[0]:
        print('Введите число, соответствующее требованиям')
    else:
        break

def finding(list, chislo):
    for i in range(len(list)):
        while list[i] < chislo:
            i += 1
        break
    return (f'Введенное число {chislo} находится между элементами №{i} и №{i + 1} введенной'
                     f' последовательности после сортировки')

print(finding(posled, chislo))

# def binary_search(array, element, left, right):
#     if left > right:
#         return False
#     middle = (right + left) // 2
#     if array[middle] == element:
#         return middle
#     elif element < array[middle]:
#         return binary_search(array, element, left, middle - 1)
#     else:
#         return binary_search(array, element, middle + 1, right)