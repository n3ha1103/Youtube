import speech_recognition as sr
import pyttsx3
import webbrowser
from googleapiclient.discovery import build

# Initialize text-to-speech engine
engine = pyttsx3.init()

# YouTube API setup
API_KEY = ''  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Function to convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to user's voice input"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print(f"User said: {user_input}")
        return user_input.lower()
    except Exception as e:
        print(f"Error: {e}")
        return ""

def search_and_play_youtube(query):
    """Search YouTube and play the first result"""
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,
        type="video"
    )
    
    response = request.execute()
    
    if response["items"]:
        video = response["items"][0]
        title = video["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}" 
        
        speak(f"Now playing: {title}")
        webbrowser.open(video_url)
        return True
    else:
        speak("Sorry, I couldn't find any matching videos.")
        return False

def get_trending_by_genre_and_language(genre, language):
    """Get trending music based on genre and language"""
    query = f"trending {genre} music {language}"
    return search_and_play_youtube(query)

def main():
    speak("Hello! What song would you like to play?")
    
    song_name = listen()
    
    if song_name:
        # User provided a song name
        if not search_and_play_youtube(song_name):
            speak("Let me find something else for you.")
            # Ask for genre and language if song not found
            speak("What genre would you like?")
            genre = listen() or "popular"
            
            speak("What language do you prefer?")
            language = listen() or "english"
            
            get_trending_by_genre_and_language(genre, language)
    else:
        # User didn't provide a song name
        speak("I didn't catch that. Let me play something trending.")
        speak("What genre would you like?")
        genre = listen() or "popular"
        
        speak("What language do you prefer?")
        language = listen() or "english"
        
        get_trending_by_genre_and_language(genre, language)

if __name__ == "__main__":
    main()