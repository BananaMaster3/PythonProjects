# Python Class 2710
# Lesson 4 Problem 6
# Author: isaiah08 (595367)
class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        self.num = num
        self.denom = denom
        self.simplify()
            
    def __str__(self):  
        return str(self.num) + '/' + str(self.denom)
    
    def __float__(self):
        """
        float(Fraction)
        returns the fraction in float state.
        """
        return self.num/self.denom
    
    
    def simplify(self):
        if self.num == 0:
            self.denom = 1
            return None
        
        do_it_again = False
        for i in range(2, abs(self.denom)):
            if abs(self.num) % i == 0 and abs(self.denom) % i == 0:
                self.num = self.num // i
                self.denom = self.denom // i
                if self.num % i == 0 and self.denom % i == 0:
                    do_it_again = True
        if self.num < 0 and self.denom < 0:
                self.num = abs(self.num)
                self.denom = abs(self.denom)
                
        if do_it_again == True:
            self.simplify()
        

        
                
                
    def add(self, other_fraction):
        if self.denom == other_fraction.denom:
            new_frac = Fraction(self.num + other_fraction.num, self.denom)
            return new_frac
        new_frac = Fraction((self.num * other_fraction.denom) + (other_fraction.num * self.denom), self.denom * other_fraction.denom)
        return new_frac
    
    def sub(self, other_fraction):
        # if the denominators are equal
        if self.denom == other_fraction.denom:
            new_frac = Fraction(self.num - other_fraction.num, self.denom)
            return new_frac
        # getting the denominators equal
        new_frac = Fraction((self.num * other_fraction.denom) - (other_fraction.num * self.denom), self.denom * other_fraction.denom)
        return new_frac
     
    def mul(self, other_fraction):
        new_frac = Fraction(self.num * other_fraction.num, self.denom * other_fraction.denom)
        return new_frac
    
        
    
    
     

    # you should add more methods


# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print 1/-6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/3, since 1/2 + (-1/6) = 1/3
print(p.sub(q))  # should print 2/3, since 1/2 - (-1/6) = 2/3
print(p.sub(p))  # should print 0/1, since p-p is 0
print(p.mul(q)) # should print 1/-12
### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False
