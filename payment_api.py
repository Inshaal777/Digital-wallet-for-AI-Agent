import logging
import asyncio

class PaymentAPI:
    async def process_payment(self, amount):
        logging.info(f"Processing payment of ${amount}...")
        await asyncio.sleep(1)  # Simulate network delay
        logging.info(f"Payment of ${amount} processed successfully!")
        return True