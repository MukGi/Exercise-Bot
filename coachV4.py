"""This is an updated version of the Coach's brain"""

import random
from nltk import pos_tag
from nltk.tokenize import word_tokenize  
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


neg_word = ["no", "not", "never", "don't", "wont", "can't", "doesn't", "n't"]
yes_words = ["yes", "yeah", "yep", "sure", "ok", "okay", "alright", "yup", "definitely", "sounds good"]


muscle_groups = ["arms", "legs", "abs", "biceps", "triceps", "cardio", "full body"]

def greetings_dict():
    return {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What would you like to know?",
        "hey": "Hey! Need help with something?",
        "good morning": "Good morning! Ready to get started?",
        "morning": "Good morning! Ready to get started?",
        "good afternoon": "Good afternoon! How can I help you?",
        "afternoon": "Good afternoon! How can I help you?",
        "good evening": "Good evening! What’s on your mind?",}
    
def workout_response_dict():
    """Returns a dictionary of responses."""
    return {
        "arms": """Here are some arm workouts:\n
                 - Hammer Curls\n
                 - Concentration Curls\n
                 - Preacher Curls\n
                 - Incline Dumbbell Curls\n
                 - Resistance Band Curls""",
        "legs": """Here are some great leg workouts:\n
                 - Squats (Bodyweight, Goblet, Barbell)\n
                 - Lunges (Forward, Reverse, Side)\n
                 - Step-Ups (Using a Bench or Box)\n
                 - Calf Raises\n
                 - Deadlifts (Romanian, Sumo, Conventional)""",
        "abs": """These are some great abdominal exercises:\n
                 - Crunches\n
                 - Bicycle Kicks\n
                 - Hanging Leg Raises\n
                 - Planks (Front, Side, Reverse)\n
                 - Russian Twists""",
        "biceps": """Some Biceps exercises are:\n
                        - Push-Ups (Close-Grip)\n
                        - Chin-Ups (if you have a bar)\n
                        - Diamond Push-Ups\n
                        - Plank to Push-Up\n
                        - Inverted Rows (using a low bar or sturdy surface)\n
                        - Bodyweight Bicep Curls (using a towel and a door)\n
                        - Isometric Bicep Hold (wall or doorway)""",
        "triceps": """Here are some triceps workouts:
                        - Diamond Push-Ups\n
                        - Triceps Dips (on a chair or bench)\n
                        - Close-Grip Push-Ups\n
                        - Pike Push-Ups\n
                        - Bench Dips\n
                        - Triceps Extensions (on the floor or against a wall)\n
                        - Isometric Triceps Hold (wall or surface press)\n
                        - Bodyweight Triceps Press (leaning against a surface or on the floor)""",
        "cardio": """Here are some great cardio workouts:\n
                   - Jump Rope\n
                   - Running or Sprinting\n
                   - High-Intensity Interval Training (HIIT)\n
                   - Burpees\n
                   - Mountain Climbers""",
        "full body": """For a full-body workout, try:\n
                      - Burpees\n
                      - Deadlifts\n
                      - Kettlebell Swings\n
                      - Rowing\n
                      - Clean and Press""",
        "cool down": """Cooling down is important! Try:\n
                      - Stretching (Hamstrings, Quads, Chest, Shoulders)\n
                      - Deep Breathing\n
                      - Light Jogging or Walking""",
        "warm up": """Warming up is crucial! Here are some good warm-ups:\n
                    - Arm Circles\n
                    - Leg Swings\n
                    - Jumping Jacks\n
                    - Dynamic Stretches\n
                    - Light Jogging"""
    }

def normalize_input(user_input):
    """Normalizing user input."""
    token_list = word_tokenize(user_input.lower())
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    normalized_words = set()
    for word in token_list:
        normalized_words.add(lemmatizer.lemmatize(word))
        normalized_words.add(stemmer.stem(word))
    
    return normalized_words

def check_negation(tokens):
    """Basically detects if a user does not want to do a workout.
        This process is more accurate with the part-of-speech tagging to read more into the context
    """
    # for word in sentence:
    #     if word in neg_word:
    #         return True
    # return False
    tagged = pos_tag(tokens)
    for i, (word, tag) in enumerate(tagged):
        if word.lower() in neg_word:
            if i + 1 < len(tagged):
                next_word, next_tag = tagged[i + 1]
                if next_tag.startswith('VB') or next_word.lower() in muscle_groups:
                    return True
    return False

def check_confirmation(tokens):
    for word in tokens:
        if word.lower() in yes_words:
            return True
    return False


def alt_choice(excluded_workout):
    """If user rejects a workout, suggest another one"""
    alternatives = [group for group in muscle_groups if group != excluded_workout]
    responses = [
        lambda: f"Okay, would you prefer {random.choice(alternatives)} or {random.choice(alternatives)} workouts instead?",
        lambda: f"How about {random.choice(alternatives)} workouts instead?",
        lambda: f" {random.choice(alternatives)} workouts might be more suited for you",
        lambda: f"Sure, we can skip that! Maybe try {random.choice(alternatives)} instead?",
        lambda: f"No worries — how about working on {random.choice(alternatives)} today?",
        lambda: f"Got it. Let's pivot to {random.choice(alternatives)} workouts!",
        lambda: f"If {excluded_workout} isn't your vibe, maybe {random.choice(alternatives)} is?",
        lambda: f"Alright, let's switch things up. How does {random.choice(alternatives)} sound?",
        lambda: f"We can change that. Would you be into {random.choice(alternatives)} instead?",
        lambda: f"Cool cool, not feeling {excluded_workout}? Let's try {random.choice(alternatives)} or {random.choice(alternatives)}.",
        lambda: f"No biggie — {random.choice(alternatives)} workouts might be more your style!",
        lambda: f"Skipping {excluded_workout}? Maybe you'd enjoy {random.choice(alternatives)} more!",
        lambda: f"Understood! Let's focus on {random.choice(alternatives)} this time."
    ]
    return random.choice(responses)()

def get_bot_response(user_input, response):
    """Processes the user input and returns an appropriate response."""
    response = workout_response_dict()
    greetings = greetings_dict()
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize and normalize user input
    token_list = word_tokenize(user_input.lower())
    lemmatized_tokens = set(lemmatizer.lemmatize(token) for token in token_list)

    # Respond to greeting
    for greeting in greetings:
        if greeting in user_input.lower():
            return greetings[greeting]

    #Check if any muscle group is mentioned
    for muscle in muscle_groups:
        muscle_lemma = lemmatizer.lemmatize(muscle)
        if muscle in token_list or muscle_lemma in lemmatized_tokens or muscle in user_input.lower():
            if check_negation(token_list):
                return alt_choice(muscle)
            elif check_confirmation(token_list):
                
                return f"Alrighty, Here's what I recommend for {muscle}:\n{response.get(muscle)}"
            return response.get(muscle, "Sorry, I don’t have info on that muscle group.")

    return "I have no information on that."
     



def main4():
    """Runs the chatbot in a loop."""
    response = workout_response_dict()
    exit_commands = {"exit", "bye", "quit"}
    
    while True:
        user_chat = input("User: ").strip().lower()
        if user_chat in exit_commands:
            print(" Adios!")
            break
        print(get_bot_response(user_chat, response))

if __name__ == "__main__":
    main4()
