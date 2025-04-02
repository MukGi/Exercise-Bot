"""This is an updated version of the Coach's brain"""

from nltk.tokenize import word_tokenize  
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

neg_word = {"no", "not", "never", "don't", "wont", "can't", "doesn't"}
muscle_groups = ["arms", "legs", "abs", "biceps", "triceps", "cardio", "full body"]
def get_response_dict():
    """Returns a dictionary of responses."""
    return {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What would you like to know?",
        "hey": "Hey! Need help with something?",
        "good morning": "Good morning! Ready to get started?",
        "good afternoon": "Good afternoon! How can I help you?",
        "good evening": "Good evening! What’s on your mind?",
        "arm": """Here are some arm workouts:
                 - Hammer Curls
                 - Concentration Curls
                 - Preacher Curls
                 - Incline Dumbbell Curls
                 - Resistance Band Curls""",
        "legs": """Here are some great leg workouts:
                 - Squats (Bodyweight, Goblet, Barbell)
                 - Lunges (Forward, Reverse, Side)
                 - Step-Ups (Using a Bench or Box)
                 - Calf Raises
                 - Deadlifts (Romanian, Sumo, Conventional)""",
        "abs": """These are some great abdominal exercises:
                 - Crunches
                 - Bicycle Kicks
                 - Hanging Leg Raises
                 - Planks (Front, Side, Reverse)
                 - Russian Twists""",
        "biceps": """Some Biceps exercises are:
                        - Push-Ups (Close-Grip)
                        - Chin-Ups (if you have a bar)
                        - Diamond Push-Ups
                        - Plank to Push-Up
                        - Inverted Rows (using a low bar or sturdy surface)
                        - Bodyweight Bicep Curls (using a towel and a door)
                        - Isometric Bicep Hold (wall or doorway)""",
        "triceps": """Here are some triceps workouts:
                        - Diamond Push-Ups
                        - Triceps Dips (on a chair or bench)
                        - Close-Grip Push-Ups
                        - Pike Push-Ups
                        - Bench Dips
                        - Triceps Extensions (on the floor or against a wall)
                        - Isometric Triceps Hold (wall or surface press)
                        - Bodyweight Triceps Press (leaning against a surface or on the floor)""",
        "cardio": """Here are some great cardio workouts:
                   - Jump Rope
                   - Running or Sprinting
                   - High-Intensity Interval Training (HIIT)
                   - Burpees
                   - Mountain Climbers""",
        "full body": """For a full-body workout, try:
                      - Burpees
                      - Deadlifts
                      - Kettlebell Swings
                      - Rowing
                      - Clean and Press""",
        "cool down": """Cooling down is important! Try:
                      - Stretching (Hamstrings, Quads, Chest, Shoulders)
                      - Deep Breathing
                      - Light Jogging or Walking""",
        "warm up": """Warming up is crucial! Here are some good warm-ups:
                    - Arm Circles
                    - Leg Swings
                    - Jumping Jacks
                    - Dynamic Stretches
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



def get_bot_response(user_input, response_dict):
    """Processes the user input and returns an appropriate response."""
    normalized_input = normalize_input(user_input)
    normalized_dict = {WordNetLemmatizer().lemmatize(key): value for key, value in response_dict.items()}
    
    for word in normalized_input:
        if word in normalized_dict:
            return f" {normalized_dict[word]}"
    
    return " I have no information on that."

def main():
    """Runs the chatbot in a loop."""
    response_dict = get_response_dict()
    exit_commands = {"exit", "bye", "quit"}
    
    while True:
        user_chat = input("User: ").strip().lower()
        if user_chat in exit_commands:
            print(" Adios!")
            break
        print(get_bot_response(user_chat, response_dict))

if __name__ == "__coach__":
    main()
