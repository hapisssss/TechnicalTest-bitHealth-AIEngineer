from typing import List


class AnswerGeneration:

    def answer(self, context: List[str]) -> str:
        if not context:
            return "Sorry, I don't know."
        return f"I found this: '{context[0][:100]}...'"