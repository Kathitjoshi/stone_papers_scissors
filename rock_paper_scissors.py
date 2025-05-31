import pyttsx3
import speech_recognition as sr
import time

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)  # Convert text to speech
    engine.runAndWait() # Wait for the speech to finish

def get_voice_input(player):
    r = sr.Recognizer() # Initialize recognizer for voice input
    mic = sr.Microphone() # Use the default microphone as the audio source
    with mic as source:
        speak(f"{player}, it's your turn. Say Stone, Paper, or Scissors.")
        print(f"{player}, please say 'Stone', 'Paper', or 'Scissors'...")
        r.adjust_for_ambient_noise(source) # Adjust for ambient noise
        audio = r.listen(source) # Listen for the player's input

    try:
        choice = r.recognize_google(audio).lower() # Recognize speech using Google Web Speech API
        if 'stone' in choice:
            return 1
        elif 'paper' in choice:
            return 2
        elif 'scissor' in choice:
            return 3
        else:
            speak("I didn't understand. Defaulting to Stone.")
            return 1
    except sr.UnknownValueError:
        speak("Couldn't hear you. Defaulting to Stone.")
        return 1

# Welcome message
print("\n🎮 Welcome to Rock, Paper, Scissors - Voice Edition! 🎮")
speak("Welcome to Rock, Paper, Scissors. Let's begin!")

# Get choices from both players via voice
x = get_voice_input("First Player")
time.sleep(1)
y = get_voice_input("Second Player")
time.sleep(1)

# Show and speak choices
choices = {1: "Stone", 2: "Paper", 3: "Scissors"}
print(f"\n🧑 First Player chose: {choices[x]}")
print(f"🧑 Second Player chose: {choices[y]}")
speak(f"First Player chose {choices[x]}")
speak(f"Second Player chose {choices[y]}")

# Decide winner
print("\n📢 RESULT:")
speak("And the result is...")

if x == y:
    result = "It's a tie! Both players chose the same."
elif (x == 1 and y == 2):
    result = "Second player won! Paper beats stone."
elif (x == 1 and y == 3):
    result = "First player won! Stone beats scissors."
elif (x == 2 and y == 1):
    result = "First player won! Paper beats stone."
elif (x == 2 and y == 3):
    result = "Second player won! Scissors beats paper."
elif (x == 3 and y == 1):
    result = "Second player won! Stone beats scissors."
else:
    result = "First player won! Scissors beats paper."

print("🎉 " + result)
speak(result)

print("\n🏁 Thanks for playing! 🕹️")
speak("Thanks for playing. Goodbye!")
