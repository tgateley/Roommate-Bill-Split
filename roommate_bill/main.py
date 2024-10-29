from roommates import Bill, Roommate
from pdfreport import PdfReport

bill_amount = float(input("Enter the bill amount: "))
bill_period = input("Ender the bill period: ")
the_bill = Bill(amount=bill_amount, bill_cycle=bill_period)

name1 = input("Enter your name: ")
days_in_house1 = int(input(f"How many days did {name1} stay in home during the bill period? "))
name2 = input("Enter your roommate's name: ")
days_in_house2 = int(input(f"How many days did {name2} stay in home during the bill period? "))

roommate1 = Roommate(name=name1, days_in_house=days_in_house1)
roommate2 = Roommate(name=name2, days_in_house=days_in_house2)

print(f"{name1}pays: ", roommate1.pays(bill=the_bill, roommate2=roommate2))
print("Mary pays: ", roommate2.pays(bill=the_bill, roommate2=roommate1))
Pdf = PdfReport(f"{the_bill.bill_cycle}.pdf")
Pdf.generate(roommate1, roommate2, the_bill)
