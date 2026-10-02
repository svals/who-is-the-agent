def get_calendar():
    meetings = [
        "9:00 AM - Product team standup",
        "11:00 AM - Identity roadmap review",
        "2:00 PM - Dentist appointment"
    ]

    return meetings


request = input("What would you like me to do? ")

if "meeting" in request.lower() or "calendar" in request.lower():
    print("\nYour meetings tomorrow:")

    for meeting in get_calendar():
        print(meeting)
else:
    print("I don't know how to do that yet.")