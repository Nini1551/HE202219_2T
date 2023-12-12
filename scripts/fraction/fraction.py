"""
Create and test a fraction class via user inputs.
A fraction is defined by its numerator and its denominator.
"""
import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : L. HUYBRECHTS
    Date : November 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, numerator: int = 0, denominator: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE : - numerator: an int
              - denominator: a non-null int
        POST : set the following attributes :
               - numerator : the reduced numerator of the fraction
               - denominator : the reduced denominator of the fraction
        RAISES : - ZeroDivisionError: denominator is null
        """
        if denominator == 0:
            raise ZeroDivisionError("The denominator of a fraction can't be null.")

        abs_numerator = abs(numerator)
        if numerator / denominator < 0:
            numerator = -abs_numerator
        else:
            numerator = abs_numerator

        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = abs(denominator) // gcd

    @property
    def numerator(self) -> int:
        """Get the numerator of the fraction

        PRE : -
        POST : Return the numerator of the fraction
        """
        return self.__numerator

    @property
    def denominator(self) -> int:
        """Get the denominator of the fraction

        PRE : -
        POST : Return the denominator of the fraction
        """
        return self.__denominator

    # ------------------ Static methods ------------------

    @staticmethod
    def __set_fraction_param(other):
        """Verify if another value is an integer or a fraction and transform it in a fraction

         PRE : - other: an integer or a fraction
         POST : the fractionated other value
         RAISES : - ValueError: other is nor an integer or a fraction
         """
        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            raise ValueError()

        return other

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : the numerator and the denominator separated by a backslash
        """
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self) -> str:
        """Return the textual representation of the reduced form of the fraction

        PRE : -
        POST : the classname, the numerator and the denominator separated by a backslash
               EX: <Fraction: .../...>
        """
        return str(f"<Fraction: {str(self)}>")

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : -
        POST : the fraction as a mixed number; the sum of the integer part and the fraction part
        """
        int_part = self.numerator // self.denominator
        fraction_part = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_part} + {fraction_part}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : - other: an integer or a fraction
         POST : a fraction that sums the current fraction and the other fraction
         RAISES : - ValueError: other is nor an integer or a fraction
         """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that subtracts the current fraction and the other fraction
        RAISES : - ValueError: other is nor an integer or a fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that multiplies the current fraction and the other fraction
        RAISES : - ValueError: other is nor an integer or a fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : - other: an integer or a fraction
        POST : a fraction that truly divides the current fraction and the other fraction
        RAISES : - ValueError: other is nor an integer or a fraction
        """
        other = self.__set_fraction_param(other)

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions

        PRE : - other: an integer
        POST : - the current fraction powered by another integer
        """
        if other != 0 and self.is_zero():
            return Fraction()

        numerator = self.numerator
        denominator = self.denominator

        if other < 0:
            numerator, denominator = denominator, numerator
            other *= -1

        numerator **= other
        denominator **= other
        return Fraction(numerator, denominator)

    def __float__(self) -> float:
        """Returns the decimal value of the fraction

        PRE : -
        POST : the floated value of the fraction
        """
        return self.numerator / self.denominator

    def __abs__(self):
        """Returns the absolute value of the fraction

        PRE : -
        POST : the absolute value of the fraction
        """
        return Fraction(abs(self.numerator), self.denominator)

    def __eq__(self, other) -> bool:
        """Overloading of the == operator for fractions

        PRE : - other: a fraction, an integer or a float
        POST : the equality between the current fraction and the other value
        """
        return float(self) == float(other)

    def __gt__(self, other) -> bool:
        """Overloading of the > operator for fractions

        PRE : - other: an integer or a fraction
        POST : the current fraction is greater than the other fraction
        """
        return float(self) > float(other)

    def __ge__(self, other) -> bool:
        """Overloading of the >= operator for fractions

        PRE : - other: an integer or a fraction
        POST : the current fraction equals or is greater than the other fraction
        """
        return float(self) >= float(other)

    def __lt__(self, other) -> bool:
        """Overloading of the < operator for fractions

        PRE : - other: an integer or a fraction
        POST : the current fraction is lower than the other fraction
        """
        return float(self) < float(other)

    def __le__(self, other) -> bool:
        """Overloading of the <= operator for fractions

        PRE : - other: an integer or a fraction
        POST : the current fraction equals or is lower than the other fraction
        """
        return float(self) <= float(other)

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0

        PRE : -
        POST : the numerator is null
        """
        return not self.numerator

    def is_integer(self) -> bool:
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : the reduced denominator equals 1
        """
        return self.denominator == 1

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : the absolute value of the fraction is < 1
        """
        return abs(float(self)) < 1

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : the reduced numerator equals 1
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) -> bool:
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : - other: a fraction
        POST : ?
        """
        difference = abs(self - other)
        return difference.is_unit()


if __name__ == '__main__':
    print('--- TEST : FRACTION CLASS ---\n')
    try:
        print('Fraction(10,0) :', end=' ')
        print(Fraction(10, 0))
    except ZeroDivisionError as error:
        print(error)

    fraction1 = Fraction(100, 4)
    print(f'Fraction(100, 4) : {fraction1} ; {fraction1.as_mixed_number()}')
    fraction2 = Fraction(-50, 62)
    print(f'Fraction(-50, 62) : {fraction2} ; {fraction2.as_mixed_number()}')
    fraction3 = Fraction(23, -17)
    print(f'Fraction(23, -17) : {fraction3} ; {fraction3.as_mixed_number()}')
    fraction4 = Fraction(-8, -6)
    print(f'Fraction(-8, -6) : {fraction4} ; {fraction4.as_mixed_number()}\n')

    num_frac1 = int(input('Numerator Fraction 1: '))
    den_frac1 = int(input('Denominator Fraction 1: '))
    num_frac2 = int(input('Numerator Fraction 2: '))
    den_frac2 = int(input('Denominator Fraction 2: '))

    frac1 = Fraction(num_frac1, den_frac1)
    print(f"Fraction 1 : {frac1} ; {frac1.as_mixed_number()}")
    frac2 = Fraction(num_frac2, den_frac2)
    print(f"Fraction 2 : {frac2} ; {frac2.as_mixed_number()}\n")

    print(f"{frac1} + {frac2} = {frac1 + frac2}")
    print(f"{frac1} - {frac2} = {frac1 - frac2}")
    print(f"{frac1} * {frac2} = {frac1 * frac2}")
    print(f"{frac1} / {frac2} = {frac1 / frac2}")
    print(f"{frac1} ** 2 = {frac1 ** 2}")
    print(f"{frac2} ** 5 = {frac2 ** 5}\n")

    print(f"float({frac1}) = {float(frac1)}")
    print(f"float({frac2}) = {float(frac2)}\n")

    print(f"abs({frac1}) = {abs(frac1)}")
    print(f"abs({frac2}) = {abs(frac2)}\n")

    print(f"{frac1} = {frac2} : {frac1 == frac2}")
    print(f"{frac1} > {frac2} : {frac1 > frac2}")
    print(f"{frac1} >= {frac2} : {frac1 >= frac2}")
    print(f"{frac1} < {frac2} : {frac1 < frac2}")
    print(f"{frac1} <= {frac2} : {frac1 <= frac2}\n")

    print(f"Is {frac1} zero ? : {frac1.is_zero()}")
    print(f"Is {frac2} zero ? : {frac2.is_zero()}")
    print(f"Is {frac1} an integer ? : {frac1.is_integer()}")
    print(f"Is {frac2} an integer ? : {frac2.is_integer()}")
    print(f"Is {frac1} proper ? : {frac1.is_proper()}")
    print(f"Is {frac2} proper ? : {frac2.is_proper()}")
    print(f"Is {frac1} unit ? : {frac1.is_unit()}")
    print(f"Is {frac2} unit ? : {frac2.is_unit()}")
    print(f"Is {frac1} and {frac2} adjacents ? : {frac1.is_adjacent_to(frac2)}\n")
