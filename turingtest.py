import random

# -------------------------------
# Agents
# -------------------------------

class HumanAgent:
    def respond(self, message):
        human_responses = [
            "That's interesting! Tell me more.",
            "I think emotions are what make us human.",
            "I love having conversations like this.",
            "What do you think about that?"
        ]
        return random.choice(human_responses)


class BotAgent:
    def respond(self, message):
        # Simple rule-based bot
        if "hello" in message.lower():
            return "Hello. How may I assist you?"
        elif "emotion" in message.lower():
            return "Emotion is a psychological state."
        else:
            return "Processing input. Please elaborate."


# -------------------------------
# Judge
# -------------------------------

class Judge:
    def evaluate(self, conversation):
        # Naive evaluation: if response feels structured/formal → assume bot
        bot_keywords = ["assist", "processing", "psychological state"]
        for msg in conversation:
            for word in bot_keywords:
                if word in msg.lower():
                    return "Judge Verdict: BOT"
        return "Judge Verdict: HUMAN"


# -------------------------------
# Controller
# -------------------------------

def run_turing_test():
    agent = random.choice([HumanAgent(), BotAgent()])
    judge = Judge()
    conversation_log = []

    print("Turing Test Started. Type 'exit' to stop.\n")

    while True:
        user_input = input("Judge: ")
        if user_input.lower() == "exit":
            break

        response = agent.respond(user_input)
        print("Unknown:", response)
        conversation_log.append(response)

    verdict = judge.evaluate(conversation_log)
    print("\n" + verdict)


if __name__ == "__main__":
    run_turing_test()