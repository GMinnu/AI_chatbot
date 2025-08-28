# Simple Activity Chatbot without NLTK - using basic string operations

activities = {
    "hiking": ["hike", "mountain", "trail", "nature", "walk"],
    "cooking class": ["cook", "kitchen", "recipe", "baking"],
    "yoga": ["yoga", "meditation", "stretch", "relax"],
    "painting workshop": ["paint", "art", "brush", "color"],
    "concert": ["music", "concert", "band", "live"],
    "movie night": ["movie", "film", "cinema", "watch"]
}

def simple_tokenize(text):
    # Simple tokenization using string methods
    import re
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.split()

def suggest_activity(user_input):
    user_words = simple_tokenize(user_input)
    suggestions = []
    
    for activity, keywords in activities.items():
        if any(word in user_words for word in keywords):
            suggestions.append(activity)
    
    if suggestions:
        return f"Based on what you said, I suggest: {', '.join(suggestions)}."
    else:
        return "Sorry, I couldn't find any activity matching your interests. Could you tell me more?"

def chatbot():
    print("Welcome to the Activity Suggestion Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have fun exploring activities!")
            break
        response = suggest_activity(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
