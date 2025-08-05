num = int(input("กรอกตัวเลขจำนวนเต็ม: "))
if num < 2:
    print(f"{num} ไม่เป็นเลขเฉพาะ")
else:
    is_p = True
    for i in range(2, num):
        if num % i == 0:
            is_p = False
            break
    if is_p:
        print(f"{num} เป็นเลขเฉพาะ")
    else:
        print(f"{num} ไม่เป็นเลขเฉพาะ")