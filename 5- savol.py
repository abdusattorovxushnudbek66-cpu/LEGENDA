narxlar = {1200,8000,15000,9000}
narx = int (input("narx kiriting:" ))
if narx in narxlar:
    narxlar.remove(narx)
    print(f"{narx} ro'yxatdan o'chirildi.")
else:
    narxlar.append(narx)
    print(f"{narx} ro'yxatga qo'shildi.")
print("Yangilangan narxlar ro'yxati:", narxlar)