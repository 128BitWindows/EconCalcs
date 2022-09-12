import math

z = 1.96    #Z crit
p = 0.6     #probability 
s = 120     #sample size

MOE = z * math.sqrt(p * (1-p) / s)
print("MOE = " + str(MOE))
print("Upper = " + str(p + MOE))
print("Lower = " + str(p - MOE))