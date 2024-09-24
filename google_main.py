import speech_recognition as sr  # Import the SpeechRecognition library to recognize speech from audio input
import webbrowser  # Import the webbrowser library to open URLs in the default web browser
import pyttsx3  # Import pyttsx3 for text-to-speech functionality
import musicLibrary  # Import your custom music library which contains a dictionary of songs and their corresponding URLs
import http.client  # Import http.client to make HTTP requests to an API

# Initialize the speech recognizer
recognizer = sr.Recognizer()
# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    #Convert the given text to speech and play it.
    engine.say(text)  # Add text to the speech queue
    engine.runAndWait()  # Wait for the speech to be played

def processCommand(c):
    #Process the given command and perform the appropriate action.
    c = c.lower()  # Convert command to lowercase for case-insensitive comparison
    print(f"Processing command: {c}")  # Print the command being processed
    
    if "open google" in c:
        webbrowser.open("https://google.com")  # Open Google in the default web browser
        speak("Opening Google")  # Announce that Google is being opened
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")  # Open Facebook in the default web browser
        speak("Opening Facebook")  # Announce that Facebook is being opened
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")  # Open YouTube in the default web browser
        speak("Opening YouTube")  # Announce that YouTube is being opened
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")  # Open LinkedIn in the default web browser
        speak("Opening LinkedIn")  # Announce that LinkedIn is being opened
    elif "open github" in c:
        webbrowser.open("https://github.com")  # Open GitHub in the default web browser
        speak("Opening Github")  # Announce that GitHub is being opened
    elif c.startswith("play"):
        song = c.split(" ")[1]  # Extract the song name from the command
        if song in musicLibrary.music:
            link = musicLibrary.music[song]  # Get the URL for the song from the music library
            webbrowser.open(link)  # Open the song URL in the default web browser
            speak(f"Playing {song}")  # Announce that the song is being played
        else:
            speak("Song not found in the music library.")  # Announce that the song was not found
            print("Song not found in the music library.")  # Print an error message
    elif "check api" in c:
        speak("Checking the API now.")  # Announce that the API check is starting
        check_api()  # Call the function to check the API
    elif "exit" in c or "stop" in c:
        speak("Goodbye!")  # Announce that the program is exiting
        exit()  # Exit the program
        
def check_api():
    """
    Check the API status and print the response.
    """
    conn = http.client.HTTPSConnection("rumad-botdelive-v1.p.rapidapi.com")  # Create a connection to the API
    headers = {
        'x-rapidapi-key': "your_api_key_here",  # Replace with your API key
        'x-rapidapi-host': "rumad-botdelive-v1.p.rapidapi.com"  # Specify the API host
    }
    
    try:
        conn.request("GET", "/verifyAC", headers=headers)  # Send a GET request to the API
        res = conn.getresponse()  # Get the response from the API
        data = res.read()  # Read the response data
        response = data.decode("utf-8")  # Decode the response data to a string
        speak(f"The API responded with: {response}")  # Announce the API response
        print(f"API Response: {response}")  # Print the API response
    except Exception as e:
        speak(f"API request failed with error: {str(e)}")  # Announce the error if the request fails
        print(f"API Error: {str(e)}")  # Print the error message
    finally:
        conn.close()  # Close the connection to the API

if __name__ == "__main__":
    speak("Initializing Google...")  # Announce that Google is initializing
    print("Google is running...")  # Print a message indicating that Google is running

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Google'...")  # Print a message indicating that Google is listening
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)  # Listen for audio input
                
                try:
                    word = recognizer.recognize_google(audio)  # Recognize the speech using Google Speech Recognition
                    print(f"Recognized word: {word}")  # Print the recognized word
                    
                    if word.lower() == "hello google":
                        speak("Yes Master")  # Announce that Google is active
                        print("Google Active...")  # Print a message indicating Google is active
                        audio = recognizer.listen(source)  # Listen for the command
                        command = recognizer.recognize_google(audio)  # Recognize the command
                        processCommand(command)  # Process the recognized command
                    else:
                        print("Keyword 'Google' not recognized.")  # Print a message if the keyword is not recognized
                
                except sr.UnknownValueError:
                    print("Sorry, I did not understand that.")  # Print a message if the speech is not understood
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")  # Print a message if there is a request error
        
        except KeyboardInterrupt:
            speak("Shutting down. Goodbye!")  # Announce that the program is shutting down
            break  # Exit the loop and end the program
        except Exception as e:
            print(f"Error: {e}")  # Print any other errors 
