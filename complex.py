first = input("please enter your first number: ").split()

print("+ is for addition""\n""- is for subtracting""\n""* is for multiplication ""\n""/ is for division" )

print("% is for modulus the two number")

opperation = input("please enter your opperation: ")

second = input("please enter your second number: ").split()


def multiply(first, second):
    x = int(first[0]) * int(second[0])
    y = int(first[1]) * int(second[1])
    z = str(x - y)
    a = int(first[0]) * int(second[1])
    b = int(first[1]) * int(second[0])
    c = a + b
    if c > 0:
        c = "+" + str(c) + "i"
    else:
        c = str(c) + "i"
    multiplication = [z, c]
    # final = ''.join(multiplication)
    return multiplication


if opperation == "+":
    def sum(first, second):
        x = str(int(first[0]) + int(second[0]))
        y = int(first[1]) + int(second[1])
        if y > 0 :
            z = "+" +str(y) + "i"
        else:
            z = str(y)+"i"

        summation = [x , z]
        final = ''.join(summation)
        return final


    print(sum(first, second))
elif opperation == "-" :
    def sub (first , second):
        x = str(int(first[0]) - int(second[0]))
        y = int(first[1]) - int(second[1])
        if y > 0:
            z = "+" + str(y) + "i"
        else:
            z = str(y) + "i"

        subtraction = [x, z]
        final = ''.join(subtraction)
        return final

    print(sub(first,second))
elif opperation == "*":

    def multiply (first , second):
        x = int(first[0]) * int(second[0])
        y = int(first[1]) * int(second[1])
        z = str(x - y)
        a = int(first[0]) * int(second[1])
        b = int(first[1]) * int(second[0])
        c = a + b
        if c >0 :
            c = "+"+str(c)+"i"
        else:
            c = str(c)+"i"
        multiplication = [z , c]
        # final = ''.join(multiplication)
        return multiplication
    test = multiply(first,second)
    print(''.join(test))
elif opperation == "/":
    def divide (first , second):
        conjugate = [int(second[0]),-int(second[1])]
        den = multiply(second,conjugate)
        nem = multiply(first,conjugate)
        a = nem[1]
        b = a[:-1]
        x = int(nem[0]) / int(den[0])
        y = int(b) / int(den[0])
        x = str(x)
        if y > 0:
            y = "+"+str(y)+"i"
        else:
            y = str(y) + "i"
        division = [x , y]
        final = ''.join(division)
        return final
    print(divide(first,second))
elif opperation == "%" :
    def mod(first,second):
        x = ((int(first[0]))**2 +(int(first[1]))**2)**0.5
        y = ((int(second[0]))**2 +(int(second[1]))**2)**0.5
        mod1= [str(x) ,"+0.00i"]
        mod2= [str(y) ,"+0.00i"]
        final1 =''.join(mod1)
        final2 =''.join(mod2)
        return final1,final2
    test1 , test2 = mod(first,second)
    print(test1)
    print(test2)
else:
    print("please enter valid opperation")







