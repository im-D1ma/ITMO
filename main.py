print ('\n\t\t Task 1\n')

a = ('Python is the best programming language in the world')
b = a[6:(-7):]

print (a)
print (b)

print ('\n\t\t Task 2\n')

a = ('Guido van Rossum is the benevolent dictator for life')
b = a[::3]

print (a)
print (b)

print ('\n\t\t Task 3\n')

text = ('You have a problem with authority, Mr. Anderson.')
symbol = list (text)
key = list (map (text.count, text))
dict = dict (zip (symbol, key))


print (text)
print (symbol)
print (key)
print (dict)