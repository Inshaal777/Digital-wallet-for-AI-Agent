import asyncio
from logger import setup_logging
from agent import AI_Agent
from payment_api import PaymentAPI
from verification_service import VerificationService

async def main():
    setup_logging()

    service = VerificationService()
    payment_api = PaymentAPI()

    agent1 = AI_Agent("Agent007")
    agent2 = AI_Agent("Agent008")

    service.verify_agent(agent1)
    service.verify_agent(agent2)

    agent1.set_budget(100.0)
    agent1.wallet.deposit(150.0)

    success = agent1.make_payment(payment_api, 50.0)
    if success:
        print(f"Payment successful for {agent1.name}. Remaining balance: ${agent1.wallet.balance}")
    else:
        print(f"Payment failed for {agent1.name}.")

    # Attempt to make a payment exceeding the budget
    agent1.make_payment(payment_api, 60.0)

    # Verify a second agent and attempt a transaction
    agent2.set_budget(200.0)
    agent2.wallet.deposit(250.0)
    agent2.make_payment(payment_api, 150.0)

if __name__ == "__main__":
    asyncio.run(main())
