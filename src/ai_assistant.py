# AI Support Assistant (Clean configuration)
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

def ask_gpt(prompt):
    return "AI response"
