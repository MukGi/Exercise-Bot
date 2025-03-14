from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *

class ChatBrain():
    def bot_response(user_input):
        """Response Dictionary/Database"""
        response_dict = {
            "arm": "Here are some biceps workouts",
            "legs": "That's fine, here are some Leg workouts",
            "abs": "These are some great Abdominal exercises",
            "biceps": """Some Biceps exercises are:
                            -Push-Ups (Close-Grip)
                            -Chin-Ups (if you have a bar)
                            -Diamond Push-Ups
                            -Plank to Push-Up
                            -Inverted Rows (using a low bar or sturdy surface)
                            -Bodyweight Bicep Curls (using a towel and a door)
                            -Isometric Bicep Hold (wall or doorway)""",

            "triceps": """Here are some triceps workouts:
                            -Diamond Push-Ups
                            -Triceps Dips (on a chair or bench)
                            -Close-Grip Push-Ups
                            -Pike Push-Ups
                            -Bench Dips
                            -Triceps Extensions (on the floor or against a wall)
                            -Isometric Triceps Hold (wall or surface press)
                            -Bodyweight Triceps Press (leaning against a surface or on the floor)""",

        }

        """Setup Up for Normalization with NLTK"""
        tokenList = word_tokenize(user_input)
        lematized_list = []
        lemmatizer = WordNetLemmatizer()
        ps = PorterStemmer()

        """Normalized Dictionary"""
        normalized_dict = {}
        for key, value in response_dict.items():
            lem_key=lemmatizer.lemmatize(key)
            normalized_dict[lem_key]=value

        """ Normalization """
        for word in tokenList:
            lematized_list.append(lemmatizer.lemmatize(word.lower()))
            lematized_list.append (ps.stem(word.lower()))

        """ Processing Giving input """
        for word in lematized_list:
            if word in response_dict:
                return(f"Chatbot: {normalized_dict[word]}")
        return (f"Chatbot: I have no information on that")

while True:
    user_chat = input("User:")
    if user_chat in ["exit,bye, quit"]:
        print("Chatbot: Adios")
    print(ChatBrain.bot_response(user_chat))



