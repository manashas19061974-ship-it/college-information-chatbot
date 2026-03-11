import datetime
import random

# Conversation history
history = []

# Function for chatbot response
def respond(message):
    print("Chatbot:", message)
    history.append("Bot: " + message)

# Responses
greetings = [
    "Hello! How can I assist you?",
    "Hi there! What would you like to know about the college?",
    "Hey! I'm here to help you with college information."
]

courses = [
    "We offer B.Tech programs in CSE, ECE, Mechanical, Civil, and IT.",
    "Our college provides engineering programs like CSE, ECE, Mechanical, Civil, and IT."
]

faq_fees = [
    "The fee structure depends on the program. Please check the official college website for details.",
    "Fees vary by department. You can contact the admissions office for exact details."
]

faq_placement = [
    "Yes, the college provides placement assistance with many companies visiting every year.",
    "Our placement cell helps students prepare for jobs and internships."
]

faq_library = [
    "The college library has thousands of books, journals, and digital resources.",
    "Students have access to a large library and online academic databases."
]

faq_hostel = [
    "Yes, hostel facilities are available for both boys and girls.",
    "Separate hostels with basic amenities are provided for students."
]

faq_admission = [
    "Admissions are based on entrance exam scores followed by counseling.",
    "You can apply through the official admission portal of the college."
]

faq_duration = [
    "B.Tech is a 4-year undergraduate engineering program.",
    "Engineering programs typically take four years to complete."
]

print("College Chatbot: Hello! Ask me about the college.")
print("Type 'help' to see what you can ask.")
print("Type 'history' to see conversation history or 'bye' to exit.\n")

while True:
    user = input("You: ").lower()
    history.append("User: " + user)

    if user == "bye":
        respond("Goodbye! Have a great day.")
        break

    elif "help" in user:
        respond("You can ask about courses, fees, placements, hostel, library, admission, or duration of programs.")

    elif "history" in user:
        print("\nConversation History:")
        for item in history:
            print("-", item)

    elif any(word in user for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        respond(random.choice(greetings))

    elif any(word in user for word in ["course", "program", "branch"]):
        respond(random.choice(courses))

    elif any(word in user for word in ["fee", "fees", "tuition"]):
        respond(random.choice(faq_fees))

    elif any(word in user for word in ["placement", "job", "company"]):
        respond(random.choice(faq_placement))

    elif "library" in user:
        respond(random.choice(faq_library))

    elif "hostel" in user:
        respond(random.choice(faq_hostel))

    elif "admission" in user:
        respond(random.choice(faq_admission))

    elif any(word in user for word in ["duration", "years", "how long"]):
        respond(random.choice(faq_duration))

    elif "time" in user or "date" in user:
        now = datetime.datetime.now()
        respond("Current date and time is " + now.strftime("%Y-%m-%d %H:%M:%S"))

    else:
        respond("Sorry, I didn't understand that. Try asking about courses, fees, placements, hostel, or admission.")
