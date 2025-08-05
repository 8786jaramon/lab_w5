n = int(input("กรอกตัวเลขจำนวนเต็ม: "))
F = 1
for n in range(1, n + 1 ):
    F *= n
print(f"{n}! = {F}")