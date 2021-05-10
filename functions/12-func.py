def temp_convert(c):
    return 9/5 * c + 32

def min_to_sec(m):
    return m * 60

def km_to_m(km):
    return km * 1000

def myMap(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

temps = [34.5,45.3,42.3,39.8,29.4,28.5,33.6]
mins = [5,6,12,45,60,1,2.5,5.5]
kms = [2,2.3,5.4,5,3.8,10,120]

print(myMap(temp_convert, temps))
print(myMap(min_to_sec, mins))
print(myMap(km_to_m, kms))
