number = int(input("一つの自然数を入れてね:"))

if number % 3 == 0:
    output = "Fizz"

elif number % 5 == 0:
    output = "Buzz"
elif number % 15 == 0:
    output = "FizzBuzz"
else:
    output = str(number)

print(output)
