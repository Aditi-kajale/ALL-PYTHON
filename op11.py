# an eg of Call By Reference
def fn(lst): # name of actual & formal arg may be same or different
	lst += [30]   # lst.append(30)
	print("In fn(), adr of lst is",id(lst)) # 1000

lst = [10,20]
print("Adr of lst in main() is",id(lst)) # 1000
print("Before fn() in main(), lst contains",lst) # [10,20]
fn(lst)
print("After fn() in main(), lst contains",lst) # [10,20,30]
