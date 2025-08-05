sentence = "Python is a powerful programming language"
words = sentence.split()
print("รายการคำ: ")
for i, item in enumerate(words, 1):
    print(f"{i}. {item}")
print(f"จำนวนคำทั้งหมด: {len(words)}")