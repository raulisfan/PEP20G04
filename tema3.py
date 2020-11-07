#
def ordered_ints(list_of_objects: list):
    listanoua = []
    for element in range(0, len(list_of_objects)):
        if type(list_of_objects[element]) == str:
            listanoua.append(int(list_of_objects[element]))
        elif type(list_of_objects[element]) == int:
            listanoua.append(list_of_objects[element])
        elif list_of_objects[element] == True:
            listanoua.append(1)
        else:
            listanoua.append(0)
    return sorted(listanoua, reverse=True)

lista = [1, True, '123', False, 6, ()]
print(ordered_ints(lista))

#
def sum_of_square(n: int):

    if n >= 1:
        if n == 1:
            return 1
        return n * n + sum_of_square(n-1)
    else:
        return 'n < 1'

print(sum_of_square(10))

#
def factorial_of_squares(n: int):
    if n >= 1:
        if n == 1:
            return 1
        return (n * n) * factorial_of_squares(n-1)
    else:
        return 'n < 1 '

print(factorial_of_squares(5))

#
def process_text(text: str):
    m=len(text)
    text2 = ''

    for i in range(0,m):
        if text[i] == ' ':
            k = i
            break

    text1 = text[0:k].upper()

    for i in range(k+1, m):
        if text[i].islower():
            text2 = text2 + text[i]
        else:
            text2 = text2 + '_'

    return (text1, text2)

print(process_text('1234567a Text to te5t'))
