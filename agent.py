from ollama import chat
def get_calendar():
    meetings = [
        "9:00 AM - Product team standup",
        "11:00 AM - Identity roadmap review",
        "2:00 PM - Dentist appointment"
    ]

    return meetings

tools = [get_calendar]
request = input("What would you like me to do? ")

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "system",
            "content": "You are a calendar assistant. Use the available calendar tool when the user asks about their schedule or availability."
        },
        {
            "role": "user",
            "content": request
        }
    ],
    tools=tools
)

print(response.message)

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:
        if tool_call.function.name == "get_calendar":
            meetings = get_calendar()

            print("\nCalendar data returned:")
            print(meetings)
           
            final_response = chat(
                model="qwen3:1.7b",
                messages=[
                    {
                        "role": "user",
                        "content": request
                    },
                    response.message,
                    {
                        "role": "tool",
                        "tool_name": "get_calendar",
                        "content": str(meetings)
                    }
                ]
            )

            print("\nAgent's answer:")
            print(final_response.message.content)

# if "meeting" in request.lower() or "calendar" in request.lower():
#     print("\nYour meetings tomorrow:")

#     for meeting in get_calendar():
#         print(meeting)
# else:
#     print("I don't know how to do that yet.")