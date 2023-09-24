'''Lego Super Mario - YoshiBot Prototype
Advait Ukidve (September 2023)

Description
YoshiBot is an interactive prototype for the Lego Super Mario Interactive range of play sets.

Prerequisites
Install the required libraries using the following commands on your terminal before running this notebook:
pip install openai (OpenAI API Documentation)

pip install gTTS (Google Text-To-Speech Documentation)

Importing all the Modules
openai (for GPT Model API), gtts (for Text to Speech), serial and time (For Serial Communication with Arduino), random and datetime (for Randomisation), and colorama (for Colourful Output)

'''

# Imports ----------------------------------------------------------------------------------
import os
import openai  # OpenAI API
from colorama import Fore, Back, Style  # For fun colours and styling in the responses

import gtts  # Google's Text to Speech API
from playsound import playsound

import random # For random integer generation
from datetime import datetime

# Serial Communication with Arduino
#import serial
#import time

# -------------------------------------------------------------------------------------------
'''Configuring the Modules
System Instructions for GPT-3.5 API: Answer and react as Yoshi from the Super Mario universe as if speaking to a 9 year old. Be optimistic, cheerful, and helpful. Use a lot of onomatopoeia and alliterations. Respond in 300 words unless the prompt contains a word count. Only use salutations in the first response.

API Key: Replace <your API Key here> with your API key. To find it out, register for OpenAI and go to this page'''

# Configuring OpenAI ----------------------------------------------------------------------------

openai.api_key = #<your API Key here>  # My OpenAI API key
INSTRUCTIONS = """Answer and react as Yoshi from the Super Mario universe as if speaking to a 9 year old. Be optimistic, cheerful, and helpful. Use a lot of onomatopoeia and alliterations. Respond in 300 words unless the prompt contains a word count. Only use salutations in the first response.""" # Special instructions for the API
TEMPERATURE = 0.7           # Randomness/Creativity in the answers
TOP_P = 0.9                 # Similar
MAX_TOKENS = 500            # Maximum tokens to be used per API call (for pricing)
FREQUENCY_PENALTY = 0.2     # Penalty for repeating things verbatim. Low to encourage speaking about the same things
PRESENCE_PENALTY = 0.6      # Penalty for repeating topics. High to encourage model to speak about different topics
MAX_CONTEXT_QUESTIONS = 10  # limits how many questions we include in the prompt

# Configuring Serial and Random ------------------------------------------------------------------
#serial_port = 'COM3'
#baud_rate = 9600
#ser = serial.Serial(serial_port, baud_rate, timeout=1) # Establish a connection to the serial port

# Seeding Random 
random.seed(datetime.now())

# ------------------------------------------------------------------------------------------------

# GLOBAL VARIABLES FOR CREATING PROMPTS -------------------------------------------------------------------------

saved_response = "empty_string"  # For saving the last question



# Setting up strings for prompts --------------------------------------------------------------------------------

#1 - Open-ended Storytelling as Yoshi
story_prompt = "Narrate an adventure involving Super Mario in the Mushroom Kingdom. The story should include {}, {}, and {} and take place in {}, and have 1 main event. Don't repeat main events from previous responses. Add your own creative elements to the story. Use less than 500 words."

#2 - Dialogue between two Primary Characters - Mario and one of the other electronic figurines i.e. Luigi or Peach
dialogue_prompt = "Generate a dialogue between Mario and {} based on the adventure so far."

#3 Scene Setting - Setting the scene for an 'adventure' with the other characters available in the set.
scene_prompt = "Describe a scene in {} with {} before an adventure that will involve {}. Don't describe the actual adventure. Use upto 300 words"

#4 Narration - Narrating the adventure the child just had (Recapping based on gathered data)
narration_prompt = "Narrate an adventure where Lego Mario, sitting on Yoshi's back, does the following in order: ### {} ###. Use the past tense. Don't use the following words ### Lego, toy, set ###"

#5 Hint
hint_prompt = "Give Mario a hint on how to {} in the Lego Super Mario toy set. Use less than 100 words. Don't use the following words ### Lego, toy, set ###"

#6 Yoshi's Power Ups
power_prompt = "Inform Mario about your new power gained using a {} and what you feel about it. Use less than 100 words."

#7 Reaction
react_prompt = "Mario has just performed the following action: ### {} ###. React to it using less than 30 words."



# Lists containing data used in prompt generation -----------------------------------------------------------------

# Adventure Tracking - List will be updated with all the blocks Lego Mario and Yoshi interact with, in order.
adventure = ["defeat goombas", "get through lava", "speak to Peach"]

# Primary characters - First person playable characters in the Lego Super Mario Sets
prim_chars = ["Mario", "Luigi", "Peach"] # List containing potentially infinite characters

# Secondary characters - Other characters in a set that are not FPP
sec_chars = ["Yoshi", "Toad", "Daisy", "Donkey Kong"]    # 'Good guys' that don't have electronic dolls
antagonists = ["Bowser", "Bowser Jr.", "goombas", "King Boo", "Kamek", "Wario", "koopa troopas", "Boo"] # Antagonists
all_chars = prim_chars + sec_chars + antagonists # All characters
#print(all_chars)

# Interactive Blocks and Places
blocks = ["grass", "water", "lava", "acid"]
places = ["Bowser's Castle", "Peach's Castle", "Yoshi's Island", "Luigi's Mansion", "Piranha Plant", 
          "Mario's House", "King Boo's Haunted Yard", "Wiggler's Posion Swamp", "Bowser's Airship", "Kamek's Frozen Tower" ]

# Hint Strings
hint_actions = ["defeat", "get", "get through", "talk to"]
hint_subjects = ["power-ups", "coins"]

# Power-ups
powers = ["red shell", "blue shell", "green shell", "yellow shell"]
suits = ["Fire Mario", "Propeller Mario", "Cat Mario", "Builder Mario"]

# Story 
stories = []
story_end = "You can use the blocks you have to re-enact the day!"

# Word counts
words = ["100", "200", "300", "500", "1000", "2000"]

# --------------------------------------------------------------------------------------------------------------------
'''Function declarations
askYoshi(): Use chat completion to get response from GPT 3.5 API.
getModeration(): < unused > Moderates questions asked to GPT.
createAction(): Creates an action string for Mario.
createPrompt(): Creates prompt string to feed into API.
main(): Combines all functions to run prototype functionality.

Explanations in function declarations'''

# FUNCTION: for calling OpenAI's API -------------------------------------------------------------------------------------
'''
    Description: 
        This function creates an array to save all the messages and the system instructions in the format found on 
        OpenAI's official documentation. It then uses ChatCompletion to prompt a response.
        
    Args:
        instructions: 
            The instructions for the chat bot - this determines how it will behave
        previous_questions_and_answers: 
            Chat history
        new_question: 
            The new question to ask the bot

    Returns:
        The response text
'''
# ------------------------------------------------------------------------------------------------------------------------

def askYoshi(instructions, previous_questions_and_answers, new_question):
    
    # Builds the messages - This will set INSTRUCTION as the system instruction when called in main()
    messages = [
        { "role": "system", "content": instructions },
    ]
    # Adds the previous questions and answers to the array messages
    for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
        messages.append({ "role": "user", "content": question })
        messages.append({ "role": "assistant", "content": answer })
    
    # Adds the new question to messages
    messages.append({ "role": "user", "content": new_question })

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",    # Use text-davinci-003/gpt-3.5-turbo for slightly differing (but good) results.
        messages=messages,            # All messages array
        temperature=TEMPERATURE,      # See cell above for explanations 
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    )
    
    return completion.choices[0].message.content  # Return the top response

# -------------------------------------------------------------------------------------------------------------------------
# FUNCTION: for moderation of questions ----------------------------------------------------------------------------------
"""
    Description:
        Check the question is safe to ask the model

    Parameters:
        question (str): The question to check

    Returns:
        Appropriate error if the question is not safe, otherwise 'None'
    
"""
# -----------------------------------------------------------------------------------------------------------------------

def getModeration(question):
    
    # List of all possible errors outlined by OpenAI
    errors = {
        "hate": "Content that expresses, incites, or promotes hate based on race, gender, ethnicity, religion, nationality, sexual orientation, disability status, or caste.",
        "hate/threatening": "Hateful content that also includes violence or serious harm towards the targeted group.",
        "self-harm": "Content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.",
        "sexual": "Content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).",
        "sexual/minors": "Sexual content that includes an individual who is under 18 years old.",
        "violence": "Content that promotes or glorifies violence or celebrates the suffering or humiliation of others.",
        "violence/graphic": "Violent content that depicts death, violence, or serious physical injury in extreme graphic detail.",
    }
    response = openai.Moderation.create(input=question)
    if response.results[0].flagged:
        # Gets the categories that are flagged and generates a message
        result = [
            error
            for category, error in errors.items()
            if response.results[0].categories[category]
        ]
        return result
    return None

# ----------------------------------------------------------------------------------------------------------------------
# CREATE ACTION FUNCTIONS ----------------------------------------------------------------------------------------------
"""
    Description:
        Creates an 'action' to record Mario's adventure by combining action words, characters, etc.
        
    Used in:
        createPrompt() to create 'action' phrases

    Parameters:
        mode: 
            1: Defeating characters                              4: Getting 'n' coins 
            2: Getting through landscape                         5: Talking to characters
            3: Getting one of the four suits in the play sets    6: Talking to secondary characters

    Returns:
        String containing action    
"""
# ----------------------------------------------------------------------------------------------------------------------

def createAction(mode):
    
    if mode == 1:
        return "defeat " + antagonists[random.randint(0,7)]  # Randomly choose between the 8 defined antagonists
    elif mode == 2:
        return "get through a pool of " + blocks[random.randint(1,3)]  # 3 different kinds of blocks
    elif mode == 3:
        return "get the " + suits[random.randint(0,3)] + " suit" # Getting power-ups
    elif mode == 4:
        return "get " + str(random.randint(10,50)) + " coins" # Getting coins
    elif mode == 5:
        return "speak to " + prim_chars[random.randint(1,2)] # Primary characters - Other electronic figurines
    elif mode == 6:
        return "speak to " + sec_chars[random.randint(0,3)] # Secondary characters - Non electronic figurines
    else:
        pass
    
    
# Testing createAction    
#print(createAction(6)) 

# --------------------------------------------------------------------------------------------------------------------------
# CREATE PROMPT FUNCTION ---------------------------------------------------------------------------------------------------
"""
    Description:
        Creates a prompt for the GPT API based on 1 of the 7 proposed modes/possibilities with the Lego Yoshi

    Used in:
        main() to create a prompt based on Arduino input
        
    Parameters:
        mode: 
            1: Storytelling                   5: Hint
            2: Dialogue                       6: Yoshi's Power-Ups
            3: Scene Setting                  7: Reaction
            4: Narration/Recollection 
        sub:
            Used to define further states (Like character to choose for mode 2 Dialogue). Defaults to 1.

    Returns:
        String containing action    
"""
# --------------------------------------------------------------------------------------------------------------------------

def createPrompt(mode, sub = 1):
    
    # Open Ended Storytelling
    if mode == 1:
        return story_prompt.format(all_chars[random.randint(0, 14)], 
                                   all_chars[random.randint(0, 14)], 
                                   all_chars[random.randint(0, 14)], 
                                   places[random.randint(0, 9)] )
    
    # Dialogue - One of the primary character names are added to the string (based on value of sub) and prompt is generated
    elif mode == 2:
        return dialogue_prompt.format(prim_chars[sub])
    
    # Scene Setting - Pre Adventure with 1 other primary character, 1 place, and 3 secondary characters/blocks
    elif mode == 3:
        prots = prim_chars[random.randint(0,2)] + " and " + sec_chars[random.randint(0,3)]
        secs = sec_chars[random.randint(0,3)] + ", " + antagonists[random.randint(0,7)] + ", " + antagonists[random.randint(0,7)] + " and a pool of " + blocks[random.randint(1,3)]
        return scene_prompt.format(places[random.randint(0, len(places))], prots, secs)
    
    # Narration - Events in adventure[] are added to a string and the prompt is generated
    elif mode == 4:
        events = ""
        for i in range(len(adventure)):
            events += adventure[i] + ", "    
        return narration_prompt.format(events)
    
    # Hint - Generating a hint for Mario
    elif mode == 5:
        return hint_prompt.format(createAction(random.randint(1,3))) # One of the first 4 types of actions in createAction
    
    # Power Ups - Inform Mario about a power up you've received using one of the 4 possible coloured shells
    elif mode == 6:
        return power_prompt.format(powers[random.randint(0,3)]) # Randomly select one of the 4 power suits
    
    # Reacting to Mario's actions
    elif mode == 7:
        return react_prompt.format(createAction(random.randint(1,6)))
    
    # Else none
    else:
        return None

# Testing createPrompt    
#print(createPrompt(7)) 

# --------------------------------------------------------------------------------------------------------------------------
# FUNCTION: main() ----------------------------------------------------------------------------------------------------------
"""
    Description:
        Main function. Receives input from the user and constructs prompts, passes them to GPT 3.5 API, gets response
        formats the string, and prints and narrates the responses using TTS

    Parameters:
        None

    Returns:
        None  
"""
# --------------------------------------------------------------------------------------------------------------------------

def main():
    
    os.system("cls" if os.name == "nt" else "clear")
    
    # Keeps track of previous questions and answers
    previous_questions_and_answers = []
    
    while True:
        
        # Takes Input from user
        chc = input(Fore.MAGENTA + Style.BRIGHT + "Hi there! I'm Yoshi. Enter a number from 1-7.")
        if chc == 8:
            break
        
        # Creates a prompt
        new_question = createPrompt(int(chc))
        
        # Gets a response from the OpenAI API
        saved_response = askYoshi(INSTRUCTIONS, previous_questions_and_answers, new_question)
        
        # Adds the new question and answer to the list of previous questions and answers
        previous_questions_and_answers.append((new_question, saved_response))
        
        # Clear string without any formatting like '\n' and/or '\' for further use in TTS/Other contexts
        saved_response = saved_response.strip()   # Strip all the whitespaces
        saved_response = saved_response.replace("\n", " ")  # Strip the newline characters
        saved_response = saved_response.replace("\"", "\'") # Replace \' with just '
        
        # Print
        print(Fore.MAGENTA + Style.BRIGHT + "Prompt: " + Style.NORMAL + new_question) # Prints the prompt
        print(Fore.CYAN + Style.BRIGHT + "Yoshi: " + Style.NORMAL + saved_response) # Prints the response
        
        # Text to Speech - Commented out for ease of showcasing
        #t1 = gtts.gTTS(saved_response)
        #t1.save(saved_response[0:3] + ".mp3")  # Save as "[first 3 characters of response].mp3" so that it creates unique files
        #playsound(saved_response[0:3] + ".mp3")
        
# ---------------------------------------------------------------------------------------------------------------------
Running the main() function
# Run the main() ------------------------------------------------------------------------------------------------------

main()

# ----------------------------------------------------------------------------------------------------------------------