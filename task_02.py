length = float(input())
width = float(input())

tup = (length, width)

perimeter = (length + width) * 2
if perimeter.is_integer():
    print(int(perimeter))
