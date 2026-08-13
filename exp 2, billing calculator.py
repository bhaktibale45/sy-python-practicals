

print("====================================")
print("       GROCERY SHOP BILLING")
print("====================================")


item1 = input("Enter first item name: ")
price1 = float(input("Enter price of first item: "))
qty1 = int(input("Enter quantity: "))

item2 = input("Enter second item name: ")
price2 = float(input("Enter price of second item: "))
qty2 = int(input("Enter quantity: "))

item3 = input("Enter third item name: ")
price3 = float(input("Enter price of third item: "))
qty3 = int(input("Enter quantity: "))


total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3


total_bill = total1 + total2 + total3

if total_bill >= 1000:
    discount = total_bill * 0.10
elif total_bill >= 500:
    discount = total_bill * 0.05
else:
    discount = 0


final_amount = total_bill - discount


print("\n====================================")
print("             BILL")
print("====================================")

print(item1, ":", price1, "x", qty1, "=", total1)
print(item2, ":", price2, "x", qty2, "=", total2)
print(item3, ":", price3, "x", qty3, "=", total3)

print("------------------------------------")
print("Total Bill       :", total_bill)
print("Discount         :", discount)
print("Final Payable    :", final_amount)
print("====================================")
print("       Thank You! Visit Again!")
print("====================================")