from numpy.core import number


def fizzbuzzz_convert(number):


if number == number % 15:
    print("FizzBuzz")

elif number % 5 == 0:
    print("Buzz")

elif number % 3 == 0:
    print("Fizz")

else:
    print(str(number))

fizzbuzzz_convert(1)
fizzbuzzz_convert(2)
fizzbuzzz_convert(34)
fizzbuzzz_convert(34)
fizzbuzzz_convert(3)
fizzbuzzz_convert(1342)
fizzbuzzz_convert(189)
