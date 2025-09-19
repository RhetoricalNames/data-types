""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
    print(values[0])
print(values[6]) """
def message(input):
    print(input)

""" x = "this is a thing"
y= x.split( )
#split ( ) splits the words between spacebars
z = y[3]
print(y)
print(z)



word_counter = input("Input a sentence")
print(len(word_counter.split( ))) """
""" 
x = "testa"
print(f"hello {x}") """


""" temp = 68
if temp > 68:
    print('warm')
elif temp == 68: #'elif' is 'else if'
    print('perfect')
else:
    print('cold') """

""" number_finder = input("Input a number")
if int(number_finder) % 2 == 0:
    print("even")
else:
    print("odd") """

""" bill = input("What's the bill?")

service = input("How was the service? Bad, okay, good, or great?")
if service == "bad":
    print((bill))
elif service == "okay":
    print(float(bill) * 1.15)
elif service == "good":
    print(float(bill) * 1.20)
elif service == "great":
    print(float(bill) * 1.25) """


""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" x = 1
if x == 2:
    print("x equals 2")
elif x == 3:
    print("x equals 3")
elif x == 4:
    print("x is 4")
elif x == 1:
    print("x = 1") """

""" factor = 2
factorlist = [1]
number = input("Input a number")
number = int(number)
if number > 100000000:
     print("Number too big!")
     quit()
else:
    for i in range(number):
        if (number % factor) == 0:
                newfactortolist = [factor]
                factorlist.append(newfactortolist)
        factor = factor + 1
print(factorlist) """

factor = 1
factorlist = [1]
number1 = input("Input a number")
number2 = input("Input another number")
number1 = int(number1)
number2 = int(number2)
for i in range(number1 + number2):
    if (number1 % factor == 0) and (number2 % factor == 0):
            newhighestfactortolist = [factor]
            factorlist[0] = (newhighestfactortolist)
    factor = factor + 1
print(f"The GCF of {number1} and {number2} is {factorlist}")
