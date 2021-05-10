def temp_convert(c):return 9/5 * c + 32

def min_to_sec(m):return m * 60

def km_to_m(km):return km * 1000

temps = [34.5,45.3,42.3,39.8,29.4,28.5,33.6]
mins = [5,6,12,45,60,1,2.5,5.5]
kms = [2,2.3,5.4,5,3.8,10,120]

print(list(map(temp_convert, temps)))
print(list(map(min_to_sec, mins)))
print(list(map(km_to_m, kms)))
