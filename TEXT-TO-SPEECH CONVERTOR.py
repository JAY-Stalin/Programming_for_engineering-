import pyttsx3
import PySimpleGUI as sg

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define the PySimpleGUI layout
layout = [
    [sg.Text("Enter text to speak:")],
    [sg.InputText()],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", "voice", default=True, key="-MALE-"), sg.Radio("Female", "voice", key="-FEMALE-")],
    [sg.Text("Select a volume rate (1-100):")],
    [sg.Slider(range=(1, 100), default_value=50, orientation="h", size=(15, 15), key="-VOLUME-")],
    [sg.Button("Speak"), sg.Button("Exit")]
]

# Create the PySimpleGUI window
window = sg.Window("Text to Speech", layout)

# Event loop to process events and get user input
while True:
    event, values = window.read()

    # Exit the app if the user closes the window or clicks the Exit button
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    # Get the text to speak and the selected voice
    text = values[0]
    voice = "english-us" if values["-MALE-"] else "english+f1"

    # Set the volume rate
    volume_rate = values["-VOLUME-"]

    # Set the pyttsx3 engine properties
    engine.setProperty("voice", voice)
    engine.setProperty("rate", volume_rate)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Close the window and exit the app
window.close()
