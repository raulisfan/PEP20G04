#
def build(a, b, c):
    def response(x):
        return a * (x ** 2) + b * x + c
    return response

functie = build(2, 4, 6)
print(functie(4))


#
list_of_functions = []
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a, b, c))

print(list_of_functions)

#
dict_of_results = {}
for function in list_of_functions:
    list_of_results = [function(x) for x in range(-10, 10)]
    dict_of_results.update({function : list_of_results })

print(dict_of_results)

#
function_with_smallest_result = None
smallest_value = None
k = 10000000
for function, values in dict_of_results.items():
    for element in values:
        if element < k:
            k = element
            function_with_smallest_result = function
            smallest_value = element

print(function_with_smallest_result, smallest_value)

#
print(function_with_smallest_result(0))