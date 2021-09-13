# 1

names = ['aLfred', 'djonataN', 'irOn MAN', 'vasYa']
mapped_names = list(map(lambda x: x.upper(), names))
print(mapped_names)

# 2

numbers = [4, 17, 3, 90, 28, 55]
filtered_numbers = list(filter(lambda x: x%2!=0, numbers))
print(filtered_numbers)

# 3

from functools import reduce
numbers = [4, 17, 3, 90, 28, 55]
reduced_numbers = reduce(lambda x, y: x*y, numbers, 15)
print(reduced_numbers)

# 4

palindromes = ['hello', 'sentences where punctuation', 45,'Able was I, ere I saw Elba', 34.0, 78.87, 'found', 'level', '12/11/21', 'radar','stats']
palindromes = [str(x) for x in palindromes]
new_spisok = []
spisok2 = []
new_spisok = [j.replace(' ', '').replace(',', '').lower() for j in palindromes ]
new_spisok = [i for i in new_spisok if i == i[::-1]]
new_spisok = ' '.join(new_spisok)
print(new_spisok)