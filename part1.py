# Part 1 of the Python Review lab.

def hello_world():
	return("hello world")


def greet_by_name(name):
	return("hello "+ name)


def encode(x):
        return(x*3953531)
	

def decode(y):
        return(y/3953531)        
	


a1=hello_world()

a2=greet_by_name("fanar")
a3=encode(2)
a4=decode(2)
print(a1)
print(a2)
print(a3)
print(a4)
