#Assign function as a variable
def sum():#function name is sum
    print("Hello world!")
a=sum#a variable can store the function
    
a()
#passing a function as an argument
def square(num):
    return num*num

def cal(operation,num):
    return operation(num)

res=cal(square,5)
print(res)
#returning a function from another function
def outer():
    
 def inner():
    print("My name is ashok")

 return inner 

res=outer()#outer function can be stored in a variable

res()
