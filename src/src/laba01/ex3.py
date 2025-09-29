price =  float(input('Введите цену: '))
sale = float(input('Введите скидку: '))
nds =  float(input('Введите НДС: '))
price_sale = price * (1 - sale / 100)
nds_1 = price_sale * (nds / 100)
total = price_sale + nds_1
print(f"База после скидки: {price_sale:.2f} ₽")
print(f"НДС:{nds_1:.2f} ₽")
print(f"Итого к оплате: {total:.2f} ₽")