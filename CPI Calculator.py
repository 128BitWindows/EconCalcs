quan = [10, 50, 100]
baseP = [100, 40, 5]
yearP = [110, 45, 6]

quanTot = 0;
baseW = 0;
yearW = 0;
yearCPI = 0;

for x in range(len(quan)):
    quanTot = quanTot + quan[x]

quanTot = quanTot * 1.0 

for x in range(len(baseP)):
    baseW = baseW + ((quan[x] / quanTot) * baseP[x])
    yearW = yearW + ((quan[x] / quanTot) * yearP[x])

yearCPI = yearW / baseW * 100

print("Weighted Base Year: " + str(baseW))
print("Weighted Current Year: " + str(yearW))
print("Current Year CPI " + str(yearCPI))

