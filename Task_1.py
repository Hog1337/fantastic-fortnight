num = -13.4
word = 'кран'
string = 'строка с большим смыслом'
list = ['с', 'п', 'и', 'с', 'о', 'к']
cort = ('к', 'o', 'р', 'т', 'е', 'ж')

print('-----')
print(abs(num))
print(round(num))
print(num + 12)
print(num - 12)
print(num**2)
print('-----')

print(word.isdigit())
print(word.isalnum())
word = word.replace('ан', 'qwerty')
print(word)
print(word +' ' +  word )
print(word*3)
print('-----')

print(string.isalpha())
print(string.swapcase())
print(string.capitalize())
print(string * 3)
print(len(string))
print(string.count('о'))
print('-----')

list.append('213')
list.pop(2)
list.reverse()
list.extend('123')
print(list)

print('-----')
print(len(cort))
print(cort.count('о'))
print(cort.index('ж'))
