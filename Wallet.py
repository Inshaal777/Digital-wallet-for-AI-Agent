import uuid
import logging

class DigitalWallet:
    def __init__(self):
        self.balance = 0.0
        self.id = str(uuid.uuid4())
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            logging.error("Deposit amount must be positive.")
            return False
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        logging.info(f"Deposited ${amount} to wallet {self.id}.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            logging.error("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            logging.error("Insufficient funds.")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")
        logging.info(f"Withdrew ${amount} from wallet {self.id}.")
        return True

    def get_transaction_history(self):
        return self.transaction_history