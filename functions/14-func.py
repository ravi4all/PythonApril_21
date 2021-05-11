temps = [34.5,45.3,42.3,39.8,29.4,28.5,33.6]
mins = [5,6,12,45,60,1,2.5,5.5]
kms = [2,2.3,5.4,5,3.8,10,120]

f = list(map(lambda c : 9/5 * c + 32, temps))
s = list(map(lambda m : m * 60, mins))
m = list(map(lambda km : km * 1000, kms))

print(f)
print(s)
print(m)