from PIL import Image

# Load the image
image = Image.open("input_image.jpg")

# Resize the image to a specific width and height
width, height = 800, 600
resized_image = image.resize((width, height))

# Save the resized image
resized_image.save("preprocessed_image.jpg")




from PIL import Image

# Load the image
image = Image.open("input_image.jpg")

# Define the cropping region (coordinates: left, upper, right, lower)
cropping_coords = (100, 100, 500, 400)

# Crop the image
cropped_image = image.crop(cropping_coords)

# Save the cropped image
cropped_image.save("preprocessed_image.jpg")




from PIL import ImageEnhance

# Load the image
image = Image.open("input_image.jpg")

# Enhance the image by adjusting brightness and contrast
enhancer = ImageEnhance.Brightness(image)
enhanced_image = enhancer.enhance(1.5)  # Increase brightness by a factor of 1.5

enhancer = ImageEnhance.Contrast(enhanced_image)
enhanced_image = enhancer.enhance(1.2)  # Increase contrast by a factor of 1.2

# Save the enhanced image
enhanced_image.save("preprocessed_image.jpg")




pip install dlib pyttsx3


import cv2
import dlib
import pyttsx3

# Load the shape predictor model
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the image and text
image_path = "avatar_image.jpg"
text_input = "Hello, how are you?"

# Load the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect facial landmarks
detector = dlib.get_frontal_face_detector()
faces = detector(gray)
if len(faces) == 0:
    print("No faces found in the image.")
    exit()
face = faces[0]
landmarks = shape_predictor(gray, face)

# Get the mouth region landmarks (change the indices according to your specific model)
mouth_landmarks = landmarks.parts()[48:68]

# Convert the text to speech
engine.save_to_file(text_input, "speech_output.wav")
engine.runAndWait()

# Play the generated speech audio
# You'll need to install a suitable audio player and provide its path
audio_player = "/path/to/audio/player"
audio_file = "speech_output.wav"
cv2.waitKey(1000)  # Wait for 1 second before playing the audio (adjust as needed)
cv2.destroyAllWindows()
import subprocess
subprocess.run([audio_player, audio_file])

# Animate the mouth based on the speech
for landmark in mouth_landmarks:
    cv2.circle(image, (landmark.x, landmark.y), 2, (0, 0, 255), -1)

# Display the animated image
cv2.imshow("Animated Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
