from ollama import chat

response = chat(
    model="qwen3:1.7b",
    messages=[
    {
        "role": "system",
        "content": "You are a calendar assistant. Help users understand their schedules. If you don't have access to calendar data, say so clearly. Keep responses brief."
    },
    {
        "role": "user",
        "content": "Am I free at 11 AM tomorrow?"
    }
]
)

print(response.message.content)