from numpy.core import number


def fizzbuzzz_convert(number):


if number % 15 == 0:
    return ("FizzBuzz")

elif number % 5 == 0:
    return ("Buzz")

elif number % 3 == 0:
    return ("Fizz")

else:
    return (str(number))

result = fizzbuzzz_convert(1)
print(result)

fizzbuzzz_convert(2)
print(result)
