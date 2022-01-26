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