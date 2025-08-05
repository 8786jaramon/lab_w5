number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for num in number:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f"เลขคู่: {even}")
print(f"เลขคี่: {odd}")
