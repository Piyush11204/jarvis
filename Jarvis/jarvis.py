from http import client
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import openai
import pyttsx3
# import webbrowser
import smtplib
import random
# import speech_recognition as sr
import wikipedia
# import datetime
import wolframalpha
import os
import sys

from jarvis3 import myCommand

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = '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'

def speak(text):
    """Function to speak the provided text"""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Function to wish the user based on the current time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I assist you today?")

def listen():
    """Function to listen for voice commands"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm unable to process your request at the moment.")
        return ""

def ask_openai(question):
    """Function to interact with OpenAI's GPT-3 API"""
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    """Main function to handle voice commands"""
    wish_me()
    while True:
        command = listen()
        if "hello" in command:
            speak("Hi there!")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        elif "what's the time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
        elif "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break
        elif "Open Aniwatch" in command:
            webbrowser.open('https://aniwatch.com/')

        else:
            speak("Let me look that up for you...")
            response = ask_openai(command)
            speak(response)

if __name__ == '__main__':

    while True:
    
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("piyushkrishna11@gmail.com", 'Piyush@11')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            # music_folder = Your_music_folder_path
            # music = [music1, music2, music3, music4, music5]
            # random_music = music_folder + random.choice(music) + '.mp3'
            # os.system(random_music)
                  
            speak('you can do it on youtube..')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        



    #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