def temp_convert(c):
    return 9/5 * c + 32

def min_to_sec(m):
    return m * 60

def km_to_m(km):
    return km * 1000

# c = 34.5
# temp = temp_convert(c)
# print(temp)

temps = [34.5,45.3,42.3,39.8,29.4,28.5,33.6]
converted_temp = []
for t in temps:
    f = temp_convert(t)
    converted_temp.append(f)

print(converted_temp)

mins = [5,6,12,45,60,1,2.5,5.5]
sec = []
for m in mins:
    sec.append(min_to_sec(m))

print(sec)

kms = [2,2.3,5.4,5,3.8,10,120]
mts = []
for k in kms:
    mts.append(km_to_m(k))
print(mts)
