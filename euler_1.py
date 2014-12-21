# sum of multiples of 3 or 5 below 1000
max_value = 1000
x = 1
sum = 0
while x < 1000:
   if x % 3 == 0 or x % 5 == 0:
       sum += x
   x += 1

print sum   