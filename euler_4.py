import time

# the returns larest palindrome which 
# is product of two 3 digit numbers

def find_max_palindrome(min=100, max=999):
    max_palindrome = 0
    for a in range(min, max + 1):  
    	for b in range(a + 1, max + 1):
    		prod = a * b
    		if prod  > max_palindrome and str(prod) == str(prod)[::-1]:
    			max_palindrome = prod
    return max_palindrome

startTime = time.time()
L = find_max_palindrome()
elapsedTime = (time.time() - time.time())

print '%s is the palindrome formed from the product of two three digit number, found in %s' % (L,elapsedTime)
