"""Classes for melon orders."""
import random
import calendar
import datetime


x = calendar.weekday


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    # date_order = datetime.datetime.now()

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = random.randrange(5, 9)

        current_day = calendar.weekday(self.date_order.year, self.date_order.month, self.date_order.day)
        current_time = int(str(self.date_order.time())[0:2])

        if current_day >= 0 and current_day < 5 and current_time > 8 and current_time <= 11:
            base_price += 4

        # add 4
        # current__time = whatever the function gives us
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas":
            base_price = self.get_base_price() * 1.5
        else:
            base_price = self.get_base_price()
        self.total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            if self.qty < 10:
                self.total += 3

        return self.total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"
    date_order = datetime.datetime.now() 

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"
    date_order = datetime.datetime.now() 

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
        
        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Class"""

    tax = 0
    order_type = "domestic"
    date_order = datetime.datetime.now() 

    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
