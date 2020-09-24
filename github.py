import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib     #For email

voice_use = pyttsx3.init('sapi5')  #We can use the ms windows voice
voices = voice_use.getProperty('voices') 
# print(voices[0].id)
voice_use.setProperty('voice',voices[0].id)

def speak(audio):
    voice_use.say(audio)
    voice_use.runAndWait()

def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("How may I help you")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    sever.starttls()
    server.login('XXXXXXX@gmail.com','user-password')
    server.sendmail('XXXXXXX@gmail.com',to,content)
    server.close()

def takeCommand():
    '''
    It takes microphone input form the user and returns string as output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        done = r.recognize_google(audio, language='en-in')
        print(f"User said: {done}\n")

    except Exception as e:
        # print(e)    
        print("Say that again...")  
        return "None"
    return done

if __name__ == "__main__":
    
    GreetMe()
    while True:
        done = takeCommand().lower()

        #Logic for excuting tasks:
        if 'wikipedia' in done:
            speak('Searching Wikipedia.....')
            done = done.replace("wikipedia","")    
            results = wikipedia.summary(done,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in done:
            webbrowser.open("youtube.com")

        elif 'open hackerrank' in done:
            webbrowser.open("hackerrank.com")

        elif 'open google' in done:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'open eclipse' in done:
            path = "D:\\My Work(Programming)\\Java\\eclipse"
            os.startfile(path)

        elif 'play music' in done:
            music_dir = 'E:\\old'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) #Start file will open it

        elif 'the time' in done:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            print(time)

        elif 'open code blocks' in done:
            path = 'C:\\Users\\Dell\\Desktop\\CodeBlocks\\codeblocks.exe'
            os.startfile(path)

        elif 'email to NAME' in done:

            try:
                speak("What should I write?")
                content = takeCommand()
                to = XXX@gmail.com  #Reciever's mail ID
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, unable to send your email")

        elif 'leave' in done:
            speak("Okay")
            exit()
