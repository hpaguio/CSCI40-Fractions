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

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass