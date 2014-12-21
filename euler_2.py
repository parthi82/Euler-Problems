# This program prints sum of even fibonnaci series number below 4 million
a = 0
b = 1
s = 0

while b < 400001:
    if (a + b) % 2 == 0:
       s += (a + b)
    b = (a + b)   
    a = (b - a)

print 'THE SUM OF ALL EVEN FIBONACCI NUMBERS BELOW 4 MILLION IS ',
print s

