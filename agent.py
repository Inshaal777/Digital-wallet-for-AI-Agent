import logging
from wallet import DigitalWallet

class AI_Agent:
    def __init__(self, name):
        self.name = name
        self.wallet = DigitalWallet()
        self.verified = False
        self.budget = 0.0

    def verify(self):
        self.verified = True
        logging.info(f"{self.name} has been verified.")

    def set_budget(self, amount):
        if amount < 0:
            logging.error("Budget cannot be negative.")
            return False
        self.budget = amount
        logging.info(f"Budget set to ${self.budget} for {self.name}.")
        return True

    def make_payment(self, payment_api, amount):
        if not self.verified:
            logging.warning(f"{self.name} is not verified.")
            return False
        if amount > self.budget:
            logging.warning(f"{self.name} attempted to exceed budget: ${amount} > ${self.budget}.")
            return False
        if not self.wallet.withdraw(amount):
            return False
        success = payment_api.process_payment(amount)
        if success:
            logging.info(f"{self.name} successfully made a payment of ${amount}.")
            return True
        return False