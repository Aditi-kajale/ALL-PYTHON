# egs of dictionary comprehension
# syntax is
# {key:value for var in iterator}

# eg-1 create a dictionary of nos from 1-10 & their squares

d = {no:no*no for no in range(1,11)}

print("d contains",d)


# eg-2, create a dictionary of month nos & corresponding month names

import calendar
# expression contains the formula for 1 pair followed by no of pairs reqd
d = {mthno : list(calendar.month_abbr) [mthno] for mthno in range(1,13)}
# list(calendar.month_abbr) creates an array/list of all month names (abbreviated values)
# if entire month name is reqd, use month_name attribute

print("d contains",d)

# eg-3, create a dictionary using data of 2 lists
items = ['pen','eraser','pencil','marker']
cost = [15,3,4.5,45]

d = {items[i] : cost[i] for i in range(len(items))}

print("d contains",d)


#eg # 4, to replace the data of a dictionary using dictionary comprehension OR to update the
# dictionary using dictionary comprehension
persons = {'manish':35,'abha':12,'ganesh':20,'namita':40,'rahul':30}
print("persons dict contains",persons)
# if age >= 30, replace age value with 'old', otherwise replace it with 'young'

persons = {name : ('old' if age >= 30 else 'young') for (name,age) in persons.items()}

print("persons dict contains",persons)










