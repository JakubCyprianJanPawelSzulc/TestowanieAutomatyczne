x = input('podaj liczbe calkowita ')

x=int(x)

if(x%15==0):
    print('"FizzBuzz"')
elif(x%3):
    print('"Fizz"')
elif(x%5):
    print('"Buzz"')
else:
    print(x)