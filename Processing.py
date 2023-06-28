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
motions = {
    'head': [
        'Nod',
        'Shake',
        'Tilt',
        'Turn'
    ],
    'lip': [
        'Open',
        'Close',
        'Smile',
        'Pucker',
        'Kiss'
    ]
}

# Function to generate motion based on text input
def generate_motion(text):
    # Process the text using spaCy
    doc = nlp(text)
    
    # Get the verb from the text
    verb = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    
    # Choose a random head motion from the available list
    head_motion = random.choice(motions['head'])
    
    # Choose a random lip motion from the available list
    lip_motion = random.choice(motions['lip'])
    
    # Generate the final motion text
    final_motion = f'{verb[0]} with {head_motion} head and {lip_motion} lips'
    
    return final_motion

# Example usage
input_text = "I want to speak"
motion_output = generate_motion(input_text)
print(motion_output)
    
