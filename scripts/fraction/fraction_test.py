"""
Test the fraction class.
"""
import unittest
from fraction import Fraction


class FractionTestCase(unittest.TestCase):
    """
    Test all the methods of the fraction class.
    """

    fract0 = Fraction()
    fract1 = Fraction(6)
    fract2 = Fraction(denominator=9)
    fract3 = Fraction(-125, 50)
    fract4 = Fraction(-8, -32)
    fract5 = Fraction(3, -4)

    def test_fraction_init(self):
        """
        Test the constructor of the fraction class.
        Test the numerator of a fraction.
        Test the denominator of a fraction
        """
        self.assertEqual(self.fract0.numerator, 0, 'Fraction().numerator')
        self.assertEqual(self.fract0.denominator, 1, 'Fraction().denominator')

        self.assertEqual(self.fract1.numerator, 6, 'Fraction(6).numerator')
        self.assertEqual(self.fract1.denominator, 1, 'Fraction(6).denominator')

        self.assertEqual(self.fract2.numerator, 0, 'Fraction(denominator=9).numerator')
        self.assertEqual(self.fract2.denominator, 1, 'Fraction(denominator=9).denominator')

        self.assertEqual(self.fract3.numerator, -5, 'Fraction(-125, 50).numerator')
        self.assertEqual(self.fract3.denominator, 2, 'Fraction(-125, 50).denominator')

        self.assertEqual(self.fract4.numerator, 1, 'Fraction(-8, -32).numerator')
        self.assertEqual(self.fract4.denominator, 4, 'Fraction(-8, -32).denominator')

        self.assertEqual(self.fract5.numerator, -3, 'Fraction(-3, -4).numerator')
        self.assertEqual(self.fract5.denominator, 4, 'Fraction(-3, -4).denominator')

        with self.assertRaises(ZeroDivisionError, msg='Fraction(128, 0)'):
            Fraction(128, 0)

    def test_fraction_str(self):
        """
        Test the string method of the fraction class.
        """
        self.assertEqual(str(self.fract0), '0/1', 'str(Fraction())')
        self.assertEqual(str(self.fract1), '6/1', 'str(Fraction(6))')
        self.assertEqual(str(self.fract2), '0/1', 'str(Fraction(denominator=9))')
        self.assertEqual(str(self.fract3), '-5/2', 'str(Fraction(-125, 50))')
        self.assertEqual(str(self.fract4), '1/4', 'str(Fraction(-8, -32))')
        self.assertEqual(str(self.fract5), '-3/4', 'str(Fraction(3, -4))')

    def test_fraction_repr(self):
        """
        Test the representation of the fraction class.
        """
        self.assertEqual(repr(self.fract0), '<Fraction: 0/1>', 'repr(Fraction())')
        self.assertEqual(repr(self.fract1), '<Fraction: 6/1>', 'repr(Fraction(6))')
        self.assertEqual(repr(self.fract2), '<Fraction: 0/1>', 'repr(Fraction(denominator=9))')
        self.assertEqual(repr(self.fract3), '<Fraction: -5/2>', 'repr(Fraction(-125, 50))')
        self.assertEqual(repr(self.fract4), '<Fraction: 1/4>', 'repr(Fraction(-8, -32))')
        self.assertEqual(repr(self.fract5), '<Fraction: -3/4>', 'repr(Fraction(3, -4))')

    def test_fraction_as_mixed_number(self):
        """
        Test the mixed number form of a fraction.
        """
        self.assertEqual(self.fract0.as_mixed_number(), '0 + 0/1', 'Fraction().as_mixed_number()')
        self.assertEqual(self.fract1.as_mixed_number(), '6 + 0/1', 'Fraction(6).as_mixed_number()')
        self.assertEqual(self.fract2.as_mixed_number(), '0 + 0/1', 'Fraction(denominator=9).as_mixed_number()')
        self.assertEqual(self.fract3.as_mixed_number(), '-3 + 1/2', 'Fraction(-125, 50).as_mixed_number()')
        self.assertEqual(self.fract4.as_mixed_number(), '0 + 1/4', 'Fraction(-8, -32).as_mixed_number()')
        self.assertEqual(self.fract5.as_mixed_number(), '-1 + 1/4', 'Fraction(3, -4).as_mixed_number()')

    def test_fraction_add(self):
        """
        Test to add of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.fract0 + self.fract3, Fraction(-5, 2), 'Fraction() + Fraction(-125, 50)')
        self.assertEqual(self.fract1 + self.fract2, Fraction(6, 1), 'Fraction(6) + Fraction(denominator=9)')
        self.assertEqual(self.fract4 + self.fract5, Fraction(-2, 4), 'Fraction(-8, -32) + Fraction(3, -4)')
        self.assertEqual(self.fract5 + 1, Fraction(1, 4), 'Fraction(3, -4) + 1')

        with self.assertRaises(ValueError, msg='Fraction() + 1.2'):
            self.fract0 + 1.2

    def test_fraction_sub(self):
        """
        Test to subtract of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.fract0 - self.fract3, Fraction(5, 2), 'Fraction() - Fraction(-125, 50)')
        self.assertEqual(self.fract1 - self.fract2, Fraction(6, 1), 'Fraction(6) - Fraction(denominator=9)')
        self.assertEqual(self.fract4 - self.fract5, Fraction(1, 1), 'Fraction(-8, -32) - Fraction(3, -4)')
        self.assertEqual(self.fract5 - 1, Fraction(-7, 4), 'Fraction(3, -4) - 1')

        with self.assertRaises(ValueError, msg='Fraction() - 1.2'):
            self.fract0 - 1.2

    def test_fraction_mul(self):
        """
        Test to multiply of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.fract0 * self.fract3, Fraction(0, 1), 'Fraction() * Fraction(-125, 50)')
        self.assertEqual(self.fract1 * self.fract2, Fraction(0, 1), 'Fraction(6) * Fraction(denominator=9)')
        self.assertEqual(self.fract4 * self.fract5, Fraction(-3, 16), 'Fraction(-8, -32) * Fraction(3, -4)')
        self.assertEqual(self.fract5 * 1, Fraction(3, -4), 'Fraction(3, -4) * 1')

        with self.assertRaises(ValueError, msg='Fraction() * 1.2'):
            self.fract0 * 1.2

    def test_fraction_truediv(self):
        """
        Test to true division of a fraction and another fraction or an integer.
        """
        self.assertEqual(self.fract0 / self.fract3, Fraction(0, 1), 'Fraction() / Fraction(-125, 50)')
        self.assertEqual(self.fract4 / self.fract5, Fraction(-1, 3), 'Fraction(-8, -32) / Fraction(3, -4)')
        self.assertEqual(self.fract5 / 1, Fraction(3, -4), 'Fraction(3, -4) / 1')

        with self.assertRaises(ZeroDivisionError, msg='Fraction(6) / Fraction(denominator=9)'):
            self.fract1 / self.fract2

        with self.assertRaises(ValueError, msg='Fraction() / 1.2'):
            self.fract0 / 1.2

    def test_fraction_pow(self):
        """
        Test to power a fraction with an integer.
        """
        self.assertEqual(self.fract0 ** -1, Fraction(0, 1), 'Fraction() ** -1')
        self.assertEqual(self.fract4 ** 3, Fraction(1, 64), 'Fraction(-8, -32) ** 3')
        self.assertEqual(self.fract5 ** -2, Fraction(16, 9), 'Fraction(3, -4) ** -2')

    def test_fraction_float(self):
        """
        Test the float value of a fraction.
        """
        self.assertEqual(float(self.fract0), 0, 'float(Fraction())')
        self.assertEqual(float(self.fract1), 6, 'float(Fraction(6))')
        self.assertEqual(float(self.fract2), 0, 'float(Fraction(denominator=9))')
        self.assertEqual(float(self.fract3), -5/2, 'float(Fraction(-125, 50))')
        self.assertEqual(float(self.fract4), 1/4, 'float(Fraction(-8, -32))')
        self.assertEqual(float(self.fract5), -3/4, 'float(Fraction(3, -4))')

    def test_fraction_abs(self):
        """
        Test the absolute value of a fraction.
        """
        self.assertEqual(abs(self.fract0), Fraction(), 'abs(Fraction())')
        self.assertEqual(abs(self.fract1), Fraction(6), 'abs(Fraction(6))')
        self.assertEqual(abs(self.fract2), Fraction(denominator=9), 'abs(Fraction(denominator=9))')
        self.assertEqual(abs(self.fract3), Fraction(125, 50), 'abs(Fraction(-125, 50))')
        self.assertEqual(abs(self.fract4), Fraction(8, 32), 'abs(Fraction(-8, -32))')
        self.assertEqual(abs(self.fract5), Fraction(3, 4), 'abs(Fraction(3, -4))')

    def test_fraction_eq(self):
        """
        Test if the fraction is equal to another fraction, a float or an integer.
        """
        self.assertTrue(self.fract0 == self.fract2, 'Fraction() == Fraction(denominator=9)')

        self.assertFalse(self.fract1 == self.fract3, 'Fraction(6) == Fraction(-125, 50)')
        self.assertFalse(self.fract4 == self.fract5, 'Fraction(-8, -32) == Fraction(3, -4)')

    def test_fraction_gt(self):
        """
        Test if the fraction is greater than another fraction, a float or an integer.
        """
        self.assertTrue(self.fract1 > self.fract3, 'Fraction(6) > Fraction(-125, 50)')
        self.assertTrue(self.fract4 > self.fract5, 'Fraction(-8, -32) > Fraction(3, -4)')

        self.assertFalse(self.fract0 > self.fract2, 'Fraction() > Fraction(denominator=9)')

    def test_fraction_ge(self):
        """
        Test if the fraction is greater or equal to another fraction, a float or an integer.
        """
        self.assertTrue(self.fract1 >= self.fract3, 'Fraction(6) >= Fraction(-125, 50)')
        self.assertTrue(self.fract4 >= self.fract5, 'Fraction(-8, -32) >= Fraction(3, -4)')
        self.assertTrue(self.fract0 >= self.fract2, 'Fraction() >= Fraction(denominator=9)')

    def test_fraction_lt(self):
        """
        Test if the fraction is lower than another fraction, a float or an integer.
        """
        self.assertFalse(self.fract1 < self.fract3, 'Fraction(6) < Fraction(-125, 50)')
        self.assertFalse(self.fract4 < self.fract5, 'Fraction(-8, -32) < Fraction(3, -4)')
        self.assertFalse(self.fract0 < self.fract2, 'Fraction() < Fraction(denominator=9)')

    def test_fraction_le(self):
        """
        Test if the fraction is lower or equal to another fraction, a float or an integer.
        """
        self.assertTrue(self.fract0 <= self.fract2, 'Fraction() <= Fraction(denominator=9)')

        self.assertFalse(self.fract1 <= self.fract3, 'Fraction(6) <= Fraction(-125, 50)')
        self.assertFalse(self.fract4 <= self.fract5, 'Fraction(-8, -32) <= Fraction(3, -4)')

    def test_fraction_is_zero(self):
        """
        Test if the value of the fraction is null.
        """
        self.assertTrue(self.fract0.is_zero(), 'Fraction().is_zero()')
        self.assertTrue(self.fract2.is_zero(), 'Fraction(denominator=9).is_zero()')

        self.assertFalse(self.fract1.is_zero(), 'Fraction(6).is_zero()')
        self.assertFalse(self.fract3.is_zero(), 'Fraction(-125, 50).is_zero()')
        self.assertFalse(self.fract4.is_zero(), 'Fraction(-8, -32).is_zero()')
        self.assertFalse(self.fract5.is_zero(), 'Fraction(3, -4).is_zero()')

    def test_fraction_is_integer(self):
        """
        Test if the value of the fraction is an integer.
        """
        self.assertTrue(self.fract0.is_integer(), 'Fraction().is_integer()')
        self.assertTrue(self.fract1.is_integer(), 'Fraction(6).is_integer()')
        self.assertTrue(self.fract2.is_integer(), 'Fraction(denominator=9).is_integer()')

        self.assertFalse(self.fract3.is_integer(), 'Fraction(-125, 50).is_integer()')
        self.assertFalse(self.fract4.is_integer(), 'Fraction(-8, -32).is_integer()')
        self.assertFalse(self.fract5.is_integer(), 'Fraction(3, -4).is_integer()')

    def test_fraction_is_proper(self):
        """
        Test if the value of the fraction is proper.
        """
        self.assertTrue(self.fract0.is_proper(), 'Fraction().is_proper()')
        self.assertTrue(self.fract2.is_proper(), 'Fraction(denominator=9).is_proper()')
        self.assertTrue(self.fract4.is_proper(), 'Fraction(-8, -32).is_proper()')
        self.assertTrue(self.fract5.is_proper(), 'Fraction(3, -4).is_proper()')

        self.assertFalse(self.fract1.is_proper(), 'Fraction(6).is_proper()')
        self.assertFalse(self.fract3.is_proper(), 'Fraction(-125, 50).is_proper()')

    def test_fraction_is_unit(self):
        """
        Test if the value of the fraction is unit.
        """
        self.assertTrue(self.fract4.is_unit(), 'Fraction(-8, -32).is_unit()')

        self.assertFalse(self.fract0.is_unit(), 'Fraction().is_unit()')
        self.assertFalse(self.fract1.is_unit(), 'Fraction(6).is_unit()')
        self.assertFalse(self.fract2.is_unit(), 'Fraction(denominator=9).is_unit()')
        self.assertFalse(self.fract3.is_unit(), 'Fraction(-125, 50).is_unit()')
        self.assertFalse(self.fract5.is_unit(), 'Fraction(3, -4).is_unit()')

    def test_fraction_is_adjacent_to(self):
        """
        Test if the fraction is adjacent to another fraction.
        """
        self.assertTrue(self.fract5.is_adjacent_to(self.fract4), 'Fraction(3, -4).is_adjacent_to(Fraction(-8, -32))')
        self.assertTrue(self.fract4.is_adjacent_to(self.fract5), 'Fraction(-8, -32).is_adjacent_to(Fraction(3, -4))')

        self.assertFalse(self.fract1.is_adjacent_to(self.fract2), 'Fraction(6).is_adjacent_to(Fraction(denominator=9))')
        self.assertFalse(self.fract0.is_adjacent_to(self.fract3), 'Fraction().is_adjacent_to(Fraction(-125, 50))')


if __name__ == "__main__":
    unittest.main()
