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

    def __init(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """
    Object that generates a pdf.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


