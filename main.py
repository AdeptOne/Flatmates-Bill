import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data a bill, sych as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, second_flatmate):
        weight = self.days_in_house / (self.days_in_house + second_flatmate.days_in_house)
        to_pay = (bill.amount * weight)
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amount
    and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, first_flatmate, second_flatmate, bill):
        first_flatmate_pay = str(round(first_flatmate.pays(bill=bill, second_flatmate=second_flatmate), 2))
        second_flatmate_pay = str(round(second_flatmate.pays(bill=bill, second_flatmate=first_flatmate), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("./img/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80,
                 txt="Flatmates Bill", align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40,
                 txt="Period:")
        pdf.cell(w=150, h=40,
                 txt=bill.period, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25,
                 txt=first_flatmate.name)
        pdf.cell(w=150, h=25,
                 txt=first_flatmate_pay, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25,
                 txt=second_flatmate.name)
        pdf.cell(w=150, h=25,
                 txt=second_flatmate_pay, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="April 2022")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print('John pays: ', john.pays(bill=the_bill, second_flatmate=marry))
print('Marry pays: ', marry.pays(bill=the_bill, second_flatmate=john))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(first_flatmate=john, second_flatmate=marry, bill=the_bill)