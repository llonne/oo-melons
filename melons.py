"""This file should have our order classes in it."""
from random import randint


class AbstractMelonOrder(object):
    """A melon order template"""


    def __init__(self, species, qty, country_code, order_type, tax):
        """Initialize melon order"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        base_price = randint(5, 9)
        return base_price

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price
        if self.species is 'Christmas':
            total = (1 + self.tax) * self.qty * (base_price * 1.5)

            if self.order_type is 'international' and self.qty < 10:
                return total + 3

            return total

        elif self.order_type is 'international' and self.qty < 10:
            return total + 3

        else:
            return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A tax-free melon order with inspection."""

    def __init__(self, species, qty):
        """Initialize GovernmentMelonOrder"""

        super(GovernmentMelonOrder, self).__init__(species, qty, 'USA', 'domestic', 0)

        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        
        super(DomesticMelonOrder, self).__init__(species, qty, 'USA', 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code, 'international', 0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
