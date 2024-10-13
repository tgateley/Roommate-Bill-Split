class Bill:
    """
    Object that contains data about a bill, such as the billing cycle
    and total amount of the bill.
    """

    def __init__(self, amount, bill_cycle):
        self.amount = amount
        self.bill_cycle = bill_cycle


class Roommate:
    """
    Object that contains roommate name, their days spent in the flat, and their
    share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, roommate2):
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        return round(weight * bill.amount, 2)


class PdfReport:
    """
    Object that generates a pdf.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


the_bill = Bill(amount=120, bill_cycle="March 2024")
john = Roommate(name='John', days_in_house=20)
mary = Roommate(name='Mary', days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, roommate2=mary))
print("Mary pays: ", mary.pays(bill=the_bill, roommate2=john))
