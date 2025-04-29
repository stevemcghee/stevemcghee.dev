from primePy import primes
import math

i = 0.0
j = 0.0
answers = []
for i in range(100):
  print ("===%f" % i)
  if (primes.check(i)):
    j = (i*i)
  else:
    j = (i/2)
  print (j)
  answers.append(j)


j = 0
for i in range(100):
    if primes.check(i):
        z = math.sqrt(answers[i])
        if z == j: print ("%d ok prime" % i)
    else:
        z = answers[i] * 2
        if z == j: print ("%d ok notprime" % i)
    j = j+1