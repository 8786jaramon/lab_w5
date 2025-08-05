numbers = [23, 67, 12, 89, 45, 91, 34] 
max_num = numbers[0]
max_index = 0
for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i
print("ตัวเลขมากที่สุด:", max_num)
print("อยู่ตำแหน่ง:", max_index)