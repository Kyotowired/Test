#!/usr/bin/python

###
"The purpose of this script is to verify the Collatz conjecture by inputting a single natural number (n), then, if even, enter the number into the formula  n/2. If odd 3n+1."
###

n = raw_input("Enter a natural number to begin.>>>     ")
start = n
n = int(n)
print ""
print ""

##This definition verifies that n is a natural number
def verify_nat(n):
	if n >= 1:
		pass
	else:
		print "Not a valid entry"

		
verify_nat(n)
count = 0		
while n != 1:
	if n%2 == 0: ##Determines whether n is even
		n = n/2
	else:
		n = 3*n+1
	count = count+1
##Can we print each number that is produced?
##Output to a .txt file???
print "Number of loops: " + str(count)
print "Started at: " + str(start)
print ""
print ""
exit = raw_input ("Enter 'q' to exit or a new natural number to repeat.")
##if exit == 'q':
	##pass
##else:
	##verify_nat(exit)