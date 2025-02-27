class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, float):
            self.numerator, self.denominator = 0, 1
            return

        if isinstance(numerator, str):
            numerator = numerator.strip()
            if "/" not in numerator:
                self.numerator, self.denominator = 0, 1
                return
            
            parts = numerator.split("/")
            if len(parts) != 2 or not parts[0].lstrip("-").isdigit() or not parts[1].lstrip("-").isdigit():
                self.numerator, self.denominator = 0, 1
                return
            
            numerator, denominator = int(parts[0]), int(parts[1])

        if denominator == 0:
            raise ZeroDivisionError("Invalid denominator 0")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        greatestCommonDivisor = Fraction.gcd(abs(numerator), abs(denominator))

        if greatestCommonDivisor == 0:
            self.numerator = numerator // 1
            self.denominator = denominator // 1
        else:
            self.numerator = numerator // greatestCommonDivisor
            self.denominator = denominator // greatestCommonDivisor

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        while b:
            a, b = b, a % b
        return abs(a)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.numerator == 0:
            return "0"
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"