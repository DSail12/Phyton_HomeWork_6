# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 5, 3] и [5, 3, 10, 2, 1]

lst = list(input('Введите пожалуйста список чисел через пробел:\n').split(' '))

lst_unique = []
lst_repeat = []
lst_wo_double = list(set(lst))

for i in lst:
    if i not in lst_unique:
        lst_unique.append(i)
    else:
        lst_unique.remove(i)
        lst_repeat.append(i)

print(f'{lst} => {lst_unique} и {lst_repeat} и {lst_wo_double}')