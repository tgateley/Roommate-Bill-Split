import webbrowser
import os

from fpdf import FPDF


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
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=20, h=20)

        # Title of the bill
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=200, h=10, txt="Flatmates Bill", border=0, align='C', ln=1)
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=20, txt=f"Period: {bill.bill_cycle}", border=0, ln=2)

        # name and amount owed by the fist roommate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=10, txt=roommate1.name, border=0)
        pdf.cell(w=100, h=10, txt=str(roommate1.pays(bill, roommate2)), border=0, ln=1)

        # Name and amount owed by the second roommate
        pdf.cell(w=100, h=10, txt=roommate2.name, border=0)
        pdf.cell(w=100, h=10, txt=str(roommate2.pays(bill, roommate1)), border=0, ln=1)

        pdf.cell(w=100, h=10, txt="Bill total: ", border=0)
        pdf.cell(w=100, h=10, txt=str(bill.amount), border=0, ln=1)

        # Change directory to pdf_reports, generate and open the PDF
        os.chdir("pdf_reports")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
