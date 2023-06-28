# Required Libraries:
# - spaCy (for NLP processing)
# - numpy (for numerical operations)
# - random (for random selection)

import spacy
import numpy as np
import random

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Define a list of sample motions
motions = [
    'Walk forward',
    'Jump',
    'Wave',
    'Spin around',
    'Clap hands'
]

# Function to generate motion based on text input
def generate_motion(text):
    # Process the text using spaCy
    doc = nlp(text)
    
    # Get the verb from the text
    verb = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    
    # Choose a random motion from the available list
    motion = random.choice(motions)
    
    # Generate the final motion text
    final_motion = f'{verb[0]} and {motion}'
    
    return final_motion

# Example usage
input_text = "I want to dance"
motion_output = generate_motion(input_text)
print(motion_output)
