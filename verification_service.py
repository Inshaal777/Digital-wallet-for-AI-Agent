import logging

class VerificationService:
    def __init__(self):
        self.verified_agents = {}

    def verify_agent(self, agent):
        if agent.name in self.verified_agents:
            logging.warning(f"{agent.name} is already verified.")
            return False
        agent.verify()
        self.verified_agents[agent.name] = agent
        logging.info(f"{agent.name} is now verified.")
        return True