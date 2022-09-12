import math
pSam = 0.40     #sample probability
p0 = 0.31       #null probability
n = 100         #sample size

z = (pSam - p0)/math.sqrt(p0 * (1-p0) /n)

print("z = " + str(z))