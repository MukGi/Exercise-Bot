from nltk.tokenize import word_tokenize  
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

NEGATION_WORDS = {"no", "not", "never", "don't", "wont", "can't", "doesn't"}
WORKOUT_GROUPS = ["arms", "legs", "abs", "biceps", "triceps", "cardio", "full body"]

def get_response_dict():
    """Returns a dictionary of responses."""
    return {
        "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "arms": "Here are some arm workouts:\n- Hammer Curls\n- Preacher Curls\n- Incline Dumbbell Curls",
        "legs": "Here are some great leg workouts:\n- Squats\n- Lunges\n- Step-Ups\n- Calf Raises",
        "abs": "These are great ab exercises:\n- Crunches\n- Bicycle Kicks\n- Hanging Leg Raises",
        "biceps": "Some Biceps exercises:\n- Chin-Ups\n- Diamond Push-Ups\n- Inverted Rows",
        "triceps": "Here are some triceps workouts:\n- Triceps Dips\n- Close-Grip Push-Ups\n- Pike Push-Ups",
        "cardio": "Great cardio workouts:\n- Jump Rope\n- HIIT\n- Mountain Climbers",
        "full body": "Full-body workout:\n- Burpees\n- Deadlifts\n- Rowing\n- Clean and Press",
        "cool down": "Cooling down is important! Try:\n- Stretching\n- Deep Breathing\n- Light Jogging",
        "warm up": "Warming up is crucial! Try:\n- Arm Circles\n- Leg Swings\n- Jumping Jacks",
    }

def normalize_input(user_input):
    """Tokenizes, lemmatizes, and stems user input."""
    token_list = word_tokenize(user_input.lower())
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    normalized_words = set()
    for word in token_list:
        normalized_words.add(lemmatizer.lemmatize(word))
        normalized_words.add(stemmer.stem(word))
    
    return normalized_words, token_list  # Return both lemmatized words & raw token list

def detect_negation(tokens):
    """Detects if the user is negating something."""
    for word in tokens:
        if word in NEGATION_WORDS:
            return True
    return False

def suggest_alternative(excluded_workout):
    """Suggests another workout group if user rejects one."""
    alternatives = [group for group in WORKOUT_GROUPS if group != excluded_workout]
    return f"Okay, would you prefer {alternatives[0]} workouts instead?"

def get_bot_response(user_input, response_dict):
    """Processes the user input and returns an appropriate response."""
    normalized_input, tokens = normalize_input(user_input)

    # Check for greetings
    for greeting in response_dict["greeting"]:
        if greeting in normalized_input:
            return "Hello! How can I help with your workout today?"

    # Check if user wants or rejects a workout
    for workout in WORKOUT_GROUPS:
        if workout in normalized_input:
            if detect_negation(tokens):
                return suggest_alternative(workout)
            return response_dict.get(workout, "I don't have information on that workout yet.")

    return "I'm not sure about that. Try asking about a specific muscle group or workout!"
