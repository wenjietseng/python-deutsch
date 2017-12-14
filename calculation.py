# variable is a sticker to object
a = 7
b = a
print(a)
print(b)

# numbers

# is 05 vaild?
#05

I_am_float = 9 / 5
I_am_integer = 9 // 5

a = a - I_am_float 
print(a)

# *=, //=, +=, ..., %

print(int('99'))
#print(int('Who am I?'))

empty_string = '' # "" works too
cats = 99
home = ''
home += 'I will have '
home += str(cats)
home += ' cats in the future.'
print(home)

print('Change float to string ', str(1000.4))
print('Change integer to string ', str(99))
print('Change boolean to string ', str(True))
print('String ' + 'can combine together ' + 'by "+"\n' + '\ for escape')

print('Extract a character with []')
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[5])
print(letters[25])

name = 'Wen-Jie Tseng'
# name[3] = ' ' # Python strings are immutable
# slice[start:end:step]
print(letters[10:])
print(lettes[-3:])
print(letters[::4])
print(letters[-1::-1])
