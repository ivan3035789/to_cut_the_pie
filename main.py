a = int(input())
b = int(input())
d = a
while d % a or d % b:
    d += a
print(d)