class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d


    def __str__(self):
        return "{}/{}".format(self.num,self.den)


    def __add__(self, other):
        temp_num = self.num*other.den + other.num*self.den
        temp_den = self.den*other.den

        smaller = min(abs(temp_den), abs(temp_num))
        HCF = 1
        for i in range(1, smaller + 1):
            if (temp_num%i == 0) and (temp_den%i == 0):
                HCF = i

        return "{}/{}".format((temp_num//HCF),(temp_den//HCF))

    def __sub__(self, other):
        temp_num = self.num*other.den - other.num*self.den
        temp_den = self.den*other.den

        smaller = min(abs(temp_den), abs(temp_num))
        HCF = 1
        for i in range(1, smaller + 1):
            if (temp_num%i == 0) and (temp_den%i == 0):
                HCF = i
        return "{}/{}".format((temp_num//HCF),(temp_den//HCF))



x=Fraction(4, 7)
y=Fraction(8, 6)

print(x + y)
print(x-y)
















