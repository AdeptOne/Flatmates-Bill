import webbrowser

from fpdf import FPDF


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