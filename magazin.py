
import sys
products = {
    "Olma":     [1200, 1300, 1100, 1250, 1400, 1150, 1350],
    "Banan":    [800, 850, 900, 780, 820, 870, 890],
    "Gilos":    [3000, 3200, 3100, 3050, 3300, 3150, 3250],
    "Shaftoli": [1600, 1500, 1550, 1650, 1700, 1580, 1620],
    "Sabzi":    [600, 550, 580, 620, 610, 595, 605],
    "Kartoshka":[400, 420, 380, 410, 430, 395, 415],
    "Piyoz":    [700, 720, 690, 710, 730, 705, 715],
}

def show_products():
    print("\nMahsulotlar:")
    for i, name in enumerate(products.keys(), start=1):
        print(f"{i}. {name}")
    print()

def show_prices(product_name):
    prices = products.get(product_name)
    if prices is None:
        print(f"'{product_name}' nomli mahsulot topilmadi.")
        return
    print(f"\n{product_name} narxlari: {prices}\n")

def add_or_remove_price(product_name, price):
    prices = products.get(product_name)
    if prices is None:
        print(f"'{product_name}' topilmadi. Iltimos, mahsulot nomini to‘g‘ri kiriting.")
        return
    if price in prices:
        prices.remove(price)
        print(f"{product_name} dan {price} o‘chirildi. Yangi ro‘yxat: {prices}")
    else:
        prices.append(price)
        print(f"{price} {product_name} ga qo‘shildi. Yangi ro‘yxat: {prices}")

def input_product(prompt="Mahsulot nomini kiriting: "):
    name = input(prompt).strip()
    for key in products.keys():
        if key.lower() == name.lower():
            return key
    return name

def main():
    print("=== 7 mahsulot, har birida 7 narx — boshqaruv ===")
    while True:
        print("\nMenyu:")
        print("1 - Mahsulotlar ro'yxatini ko'rish")
        print("2 - Bir mahsulotning narxlarini ko'rish")
        print("3 - Narx qo'shish / mavjud bo'lsa o'chirish (toggle)")
        print("4 - Mahsulot qo'shish (yangi nom bilan, boshlang'ich bo'sh narxlar ro'yxati)")
        print("5 - Mahsulot o'chirish")
        print("6 - Hammasini chop et")
        print("0 - Chiqish")
        cmd = input("Tanlovni kiriting (raqam): ").strip()
        if cmd == "1":
            show_products()
        elif cmd == "2":
            prod = input_product("Qaysi mahsulotni ko'rmoqchisiz? ")
            show_prices(prod)
        elif cmd == "3":
            prod = input_product("Qaysi mahsulotga narx kiritasiz? ")
            if prod not in products:
                print(f"'{prod}' topilmadi. Avvalo mahsulotni qo'shing (menu 4).")
                continue
            p_raw = input("Narxni butun son formatida kiriting (masalan 1200): ").strip()
            if not p_raw.isdigit():
                print("Xato: narx butun son bo'lishi kerak.")
                continue
            price = int(p_raw)
            add_or_remove_price(prod, price)
        elif cmd == "4":
            new_name = input("Yangi mahsulot nomi: ").strip()
            if any(k.lower() == new_name.lower() for k in products):
                print("Bunday nomli mahsulot mavjud.")
            else:
                print("Agar boshlang'ich 7 ta narxni hohlasangiz, vergul bilan yozing (masalan: 100,200,...). Bo'sh qoldirsangiz 7 ta 0 qo'yiladi.")
                line = input("Narxlar (yoki Enter): ").strip()
                if line:
                    parts = [p.strip() for p in line.split(",") if p.strip().isdigit()]
                    nums = [int(p) for p in parts][:7]
                    while len(nums) < 7:
                        nums.append(0)
                else:
                    nums = [0]*7
                products[new_name] = nums
                print(f"Mahsulot '{new_name}' qo'shildi: {nums}")
        elif cmd == "5":
            prod = input_product("Qaysi mahsulotni o'chirmoqchisiz? ")
            if prod in products:
                del products[prod]
                print(f"'{prod}' o'chirildi.")
            else:
                print("Bunday mahsulot topilmadi.")
        elif cmd == "6":
            print("\n--- HAMMASI ---")
            for k, v in products.items():
                print(f"{k}: {v}")
            print("---------------")
        elif cmd == "0":
            print("Xayr! Dasturdan chiqildi.")
            sys.exit(0)
        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")
if __name__ == "__main__":
    main()
products = {
    "Olma": 1200,
    "Banan": 800,
    "Gilos": 3000,
    "Shaftoli": 1600,
    "Sabzi": 600,
    "Kartoshka": 400,
    "Piyoz": 700
}
print("=== Mahsulotlar ro'yxati ===")
for i, (name, price) in enumerate(products.items(), start=1):
    print(f"{i}. {name} - {price} so'm")
tanlanganlar = {}
for i in range(1, 4):
    nom = input(f"\n{i}-mahsulot nomini kiriting: ").capitalize()
    if nom not in products:
        print("Bunday mahsulot yo'q, qaytadan kiriting.")
        continue
    try:
        soni = int(input(f"{nom} dan nechta olasiz? "))
    except ValueError:
        print("Iltimos, son kiriting!")
        continue
    tanlanganlar[nom] = soni
print("\n=== Xarid ro'yxati ===")
jami = 0
for nom, soni in tanlanganlar.items():
    narx = products[nom]
    summa = narx * soni
    print(f"{nom}: {soni} x {narx} = {summa} so'm")
    jami += summa

print("---------------------------")
print(f"Jami to'lov: {jami} so'm")

