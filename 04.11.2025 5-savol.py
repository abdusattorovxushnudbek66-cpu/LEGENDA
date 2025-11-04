parol = input("\nParol kiriting: ")

if len(parol) > 6 and "123" not in parol:
    print("Parol qabul qilindi ")
else:
    print("Parol xato  — uzunligi 6 dan katta bo‘lishi va '123' ketma-ketligi bo‘lmasligi kerak.")
