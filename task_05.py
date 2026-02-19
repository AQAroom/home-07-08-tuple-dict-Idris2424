h = int(input())
m = int(input())
s = int(input())

tup = (h,m,s)

seconds = tup[0] * 3600 + tup[1] * 60 + tup[2]
print(seconds)
