# eg - 1 on String type
# string literal (value on RHS of a string variable)

# string literal can be enclosed in ' ' or " "

str1 = 'There will be no python classes tomw'
str2 = "There will be no python classes tomw"

print("str1 contains",str1)
print("str2 contains",str2)

#str3 = 'Sir, pls don't keep python class tomw'  # error, invalid syntax
str4 = "Sir, pls don't keep python class tomw"

print("str4 contains",str4)

#str5 = "He said,"Will you keep classes tomw?""  # error
str6 = 'He said,"Will you keep classes tomw?"'

print("str6 contains",str6)

str7 = 'Sir, pls don\'t keep python class tomw'   # \ is escape sequence i.e.
				# it will treat ' as char & not cmd

print("str7 contains",str7)

multi_line = '''
Hello & Welcome All To
"Databyte's Annual Function Day"
Thanks '''

print("multi_line contains",multi_line)

'''
This is a multi line comment '''



