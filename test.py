
def hello():
    global x
    x = 7
    print("x in func =", x)

hello()
x=23
print("x after func =", x)