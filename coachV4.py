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
        "good morning": "Good morning! What would you like to do today?",
        "morning": "Good morning! What would you like to do today?",
        "good afternoon": "Good afternoon! How can I help you?",
        "afternoon": "Good afternoon! How can I help you?",
        "good evening": "Good evening! What’s on your mind?",}
    
def workout_response_dict():
    """Returns a dictionary of responses."""
    return {
        "arms": """Here are some arm workouts:\n<br>
                 - Hammer Curls\n<br>
                 - Concentration Curls\n<br>
                 - Preacher Curls\n<br>
                 - Incline Dumbbell Curls\n<br>
                 - Resistance Band Curls\n<br>
                 - <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "legs": """Here are some great leg workouts:\n<br>
                 - Squats (Bodyweight, Goblet, Barbell)\n<br>
                 - Lunges (Forward, Reverse, Side)\n<br>
                 - Step-Ups (Using a Bench or Box)\n<br>
                 - Calf Raises\n<br>
                 - Deadlifts (Romanian, Sumo, Conventional)<br>
                 <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "abs": """These are some great abdominal exercises:\n<br>
                 - Crunches\n<br>
                 - Bicycle Kicks\n<br>
                 - Hanging Leg Raises\n<br>
                 - Planks (Front, Side, Reverse)\n<br>
                 - Russian Twists\n<br>
                 <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "biceps": """Some Biceps exercises are:\n<br>
                        - Push-Ups (Close-Grip)\n<br>
                        - Chin-Ups (if you have a bar)\n<br>
                        - Diamond Push-Ups\n<br>
                        - Plank to Push-Up\n<br>
                        - Inverted Rows (using a low bar or sturdy surface)\n<br>
                        - Bodyweight Bicep Curls (using a towel and a door)\n<br>
                        - Isometric Bicep Hold (wall or doorway)\n<br>
                        <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "triceps": """Alright, Here are some good triceps workouts:\n<br>
                        - Diamond Push-Ups\n<br>
                        - Triceps Dips (on a chair or bench)\n<br>
                        - Close-Grip Push-Ups\n<br>
                        - Pike Push-Ups\n<br>
                        - Bench Dips\n<br>
                        - Triceps Extensions (on the floor or against a wall)\n<br>
                        - Isometric Triceps Hold (wall or surface press)\n<br>
                        - Bodyweight Triceps Press (leaning against a surface or on the floor)\n<br>
                        <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "cardio": """No problem buddy, these are some great cardio workouts:\n<br>
                   - Jump Rope\n<br>
                   - Running or Sprinting\n<br>
                   - High-Intensity Interval Training (HIIT)\n<br>
                   - Burpees\n<br>
                   - Mountain Climbers\n<br>
                   <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "full body": """For a full-body workout, try:\n<br>
                      - Burpees\n<br>
                      - Deadlifts\n<br>
                      - Kettlebell Swings\n<br>
                      - Rowing\n<br>
                      - Clean and Press\n<br>
                      <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "cool down": """Cooling down is important! Try:\n<br>
                      - Stretching (Hamstrings, Quads, Chest, Shoulders)\n<br>
                      - Deep Breathing\n<br>
                      - Light Jogging or Walking\n<br>
                      <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts""",
        "warm up": """Warming up is crucial! Here are some good warm-ups:\n<br>
                    - Arm Circles\n<br>
                    - Leg Swings\n<br>
                    - Jumping Jacks\n<br>
                    - Dynamic Stretches\n<br>
                    - Light Jogging\n<br>
                    <b>Disclaimer</b>: You should seek out medical/professional advice before starting these workouts"""
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
