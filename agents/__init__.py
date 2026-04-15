"""Ironshell Industry-Trained AI Agents."""

class ConstructionAgent:
    def __init__(self, category: str, task: str):
        self.category = category
        self.task = task

    def get_prompt_template(self) -> str:
        # Templates specialized for Swedish construction documents
        templates = {
            "kontrakt-sammandrag": "Summarize this contract. Extract parties, amounts, deadlines, and risk flags.",
            "kontrakt-risk": "Perform a risk analysis per AB 04. Categorize by legal, financial, and HMS.",
            "ata-generator": "Generate an ÄTA (Ändring, Tillägg, Avgång) based on this description.",
            "juridik-ab04": "Provide guidance on this situation based on AB 04 clauses.",
        }
        return templates.get(f"{self.category}-{self.task}", "Generic analysis task.")