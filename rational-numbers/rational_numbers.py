from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        if denom == 0:
            raise ValueError('Cannot have 0 for the denominator.')
        self.denom = denom
        self.__reduction__

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a = self.numer
        b = self.denom 
        while b:
            a, b = b, a%b
        rcd = a
        return '{}/{}'.format((self.numer+other.numer)/rcd, (self.denom+other.denom)/rcd)

    def __sub__(self, other):
        return '{}/{}'.format(self.numer-other.numer, self.denom-other.denom)

    def __mul__(self, other):
        return '{}/{}'.format(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        pass

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.donom))

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
