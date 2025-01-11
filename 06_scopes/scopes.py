username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()

x = 99 
def func3(y):
    z = x + y
    return z

result = func3(5)
print(result)

def func2():
    global x
    x = 12

func2()
print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myresult = f1()
myresult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))