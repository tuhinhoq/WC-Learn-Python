print("Enter a number: ")
a=input()
b=int(a)

print("Enter another number: ")
d=input()
c=int(d)


print("Press: 1 For Add, 2 For Sub, 3 For Multiply, 4 For Divided")
bb=input()
aa=int(bb)



def add(b,c):
    return b+c
def sub(b,c):
    return b-c
def mul(b,c):
    return b*c
def div(b,c):
    return b/c



if aa==1:
    print(b, "+", c, "=", add(b,c))
elif aa==2:
    print(b, "-", c, "=", sub(b,c))
elif aa==3:
    print(b, "*", c, "=", mul(b,c))
elif aa==4:
    print(b, "/", c, "=", div(b,c))
else:
    print("Wrong Input.")



