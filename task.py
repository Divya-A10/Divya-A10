from typing import final

print("welcome to the calculator!")
bill=float(input("what was the total bill?$"))
tip=int(input("what percentage of tip would you like to give? 12 13 15"))
people=int(input("how many people have to split the bill?"))
bill_with_tip=tip / 100 * bill+ bill
print(bill_with_tip)
final_amount=round(bill)