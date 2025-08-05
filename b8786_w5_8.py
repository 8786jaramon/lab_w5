scores = [85, 92, 78, 96, 88, 79, 90, 87]
print("=== การวิเคราะห์คะแนนสอบ ===")
print(f"คะแนนทั้งหมด: {scores}")
print(f"ค่าเฉลี่ย: {sum(scores)/len(scores):.2f}")
print(f"คะแนนสูงสุด: {max(scores)}")
print(f"คะแนนต่ำสุด: {min(scores)}")
above_85 = [(i+1, s) for i, s in enumerate(scores) if s > 85]
print(f"จำนวนคนที่ได้คะแนนมากกว่า 85: {len(above_85)} คน\n")
if above_85:
    print("คะแนนที่มากกว่า 85:")
    for i, s in above_85:
        print(f"นักเรียนคนที่ {i}: {s} คะแนน")
