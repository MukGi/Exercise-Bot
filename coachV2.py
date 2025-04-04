"""This is an updated version of the Coach's brain"""

import random
from nltk.tokenize import word_tokenize  
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

neg_word = ["no", "not", "never", "don't", "wont", "can't", "doesn't", "n't"]
muscle_groups = ["arms", "legs", "abs", "biceps", "triceps", "cardio", "full body"]

def greetings_dict():
    return {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What would you like to know?",
        "hey": "Hey! Need help with something?",
        "good morning": "Good morning! Ready to get started?",
        "good afternoon": "Good afternoon! How can I help you?",
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
    """Basically detects if a user does not want to do a workout."""
    for word in tokens:
        if word in neg_word:
            return True
    return False

def alt_choice(excluded_workout):
    """If user rejects a workout, suggest another one"""
    alternatives = [group for group in muscle_groups if group != excluded_workout]
    return f"Okay, would you prefer {alternatives[random.randint(0,len(muscle_groups)-2)]} workouts instead?"

def get_bot_response(user_input, response_dict):
    """Processes the user input and returns an appropriate response."""
    response_dict= workout_response_dict()
    greetings = greetings_dict()
    normalized_input = normalize_input(user_input)
    tokens = normalize_input(user_input)
    normalized_workout_dict = {WordNetLemmatizer().lemmatize(key): value for key, value in response_dict.items()}
    normalized_greetings = {WordNetLemmatizer().lemmatize(key): value for key, value in greetings.items()}
    
    """Normalizing the muscle group array
    - Without this normalization, the bot cannot detect certain words in the muscle groups array. 
    """
    normalized_muscle_groups = {WordNetLemmatizer().lemmatize(m): m for m in muscle_groups}

    
    """Respond to greeting if any"""
    for greeting in greetings:
        if greeting in normalized_input:
            return f"{normalized_greetings[greeting]}"
    
    """Respond to exercise after checking for rejection"""
    for norm_group, original in normalized_muscle_groups.items():
        if norm_group in tokens or original in tokens:  
            if check_negation(tokens):
                return alt_choice(original)
            return normalized_workout_dict.get(original, " I don't have info on that muscle group.")
         
    return " I have no information on that."


def main3():
    """Runs the chatbot in a loop."""
    response_dict = workout_response_dict()
    exit_commands = {"exit", "bye", "quit"}
    
    while True:
        user_chat = input("User: ").strip().lower()
        if user_chat in exit_commands:
            print(" Adios!")
            break
        print(get_bot_response(user_chat, response_dict))

if __name__ == "__main__":
    main3()
