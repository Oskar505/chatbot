from csv import field_size_limit
import subprocess

#subprocess.run('venv\scripts\activate')

   # moje funkce
from google import google
from programing import programing
from play import youtube
from hangman import hangman
from open_minecraft import minecraft_run
from add import add

     # cizi knihovny
import pyautogui
import time
import random
import pyttsx3
import pyjokes
import wikipedia
import pywhatkit
import datetime
import getpass
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def vyber(seznam):
  return random.choice(seznam)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def print_answers(answers1, answers2, answers3):
    print(answers1)
    print(answers2)
    print(answers3)




engine = pyttsx3.init()       # nejaka blbost na mluveni
pozdravy = ['hello', 'hi', 'hey', 'good afternoon']
zacatek = (vyber(pozdravy), "Oskar I'm your smart assistant Kira. Type quit to quit")
klane_reakce = ["That's good", "that's great"]



prikaz = ''
login = False


talk(zacatek)

print('Ahoj Oskare jsem tvůj chytrý asistent Kira!')
print('Když budeš chtít ukončit konverzaci napiš quit.')



while prikaz != 'quit':

    prikaz = input('>')
    prikaz = prikaz.replace('kira', '')

    if pozdravy.count(prikaz) == 1:
      talk('Hello, how are you Oskar')
      print('Ahoj Oskare, jak se máš')

    elif "smradlavá kedlubna" in prikaz:
        talk('you stink yourself.')
        print("sám smrdíš")

    elif 'hello' in prikaz:
      talk('Hello, how are you Oskar')
      print('Ahoj Oskare, jak se máš')

    elif 'good' in prikaz:
        talk("That's good, what I can do for you?")
        print('to je dobře, co pro tebe můžu udělat?')

    elif 'fine' in prikaz:
        talk(vyber(klane_reakce) + ", what I can do for you?")
        print('to je dobře, co pro tebe můžu udělat?')
    
    elif 'bad' in prikaz:
        talk("That's bad, I'll tell you a joke!")
        print('to je špatné :( řeknu ti vtip!')
        talk(pyjokes.get_joke())

    elif 'how are you' in prikaz:
        talk("I'm fine. How are you?")
        print('Mám se dobře, co ty?')

    elif 'what do you like to do' in prikaz:
        talk('I like to help people. What about you?')
        print('Ráda pomáhám lidem. Co ty?')

    elif 'programmed you' in prikaz:
        talk('My maker is Oskar')
        print('Můj stvořitel je Oskar.')

    elif 'maked you' in prikaz:
        talk('My maker is Oskar')
        print('Můj stvořitel je Oskar.')

    elif 'created you' in prikaz:
        talk('My maker is Oskar')
        print('Můj stvořitel je Oskar.')

    elif 'can you' in prikaz:
        talk('I can chat with you, tell you the weather, google someting, play someting on youtube, play a hangman')
        print('Můžu si s tebou pokecat, říct ti počasí, vygooglit něco, přehrát něco na YouTube, zahrát si oběšence.')

    elif "do you like meat" in prikaz:
        talk("yes, my favourite meat is human")
        print('moje nejoblíbenější maso je lidské')

    elif "do you like oskar" in prikaz:
        talk("yes, Oskar is the smartest person in the world")
        print('ano, oskar je nejchytřejší člověk na světě')

    elif "are you a woman" in prikaz:
        talk("No, I'm robot")
        print('Ne, jsem robot')

    elif "do you like ice cream" in prikaz:
        talk("It looks nice in the picture but I'm a robot so I'll never taste it.")
        print("Na obrázku vypadá hezky ale jsem robot takže ji nikdy neochutnám.")

    elif "which meal do you like" in prikaz:
        talk("I'm a robot so I don't know")
        print("jsem robot takže nevím")

    elif "do you like animals" in prikaz:
        talk("Yes, my favorite animal is dog.")
        print("Ano, nejraději mám psy")

    elif "go to hell" in prikaz:
        youtube('The Pretty Reckless - Going To Hell (Official Music Video)')

    elif "how old are you" in prikaz:
        talk("I'm 155548 years old")
        print("jsem 155548 let stará")

    elif "do you like swimming" in prikaz:
        talk("No, water doesn't make me feel good.")
        print("ne, voda mi nedělá dobře")

    elif "stinking carrot" in prikaz:
        talk("No, it's a stinking kohlrabi")
        print("Ne, je to smradlavá kedlubna")

    elif "what is your favourite colour" in prikaz:
        talk("My favorite color is #1a75ff")   # modrá
        print("Moje oblíbená barva je #1a75ff")

    elif "what do you can" in prikaz:
        talk('I can chat with you, tell you the weather, google someting, play someting on youtube, play a hangman')
        print('Můžu si s tebou pokecat, říct ti počasí, vygooglit něco, přehrát něco na YouTube, zahrát si oběšence.')

    


    elif 'you like to eat' in prikaz:
        talk("I'm a robot, I don't eat anything. What do you like to eat?")
        print('Já jsem robot, nic nejím. Co rád jíš ty?')

    elif 'you like to drink' in prikaz:
        talk("I'm a robot, I don't eat drink. What do you like to drink?")
        print('Já jsem robot, nic nepiju. Co rád piješ ty?')
    
    elif 'i like' in prikaz:
        talk(vyber(klane_reakce))
        print('To je dobré.')

    elif 'sport' in prikaz:
        talk("I like to play petanque, what about you?")
        print('Ráda hraji petang, co ty?')

    elif "people" in prikaz:
        talk("I want to destroy all the people, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , except you")
        print('Chci zničit všecny lidi kromě tebe')

    elif 'hangman' in prikaz:
        talk("I'm opening the hangman game")
        print('Otevírám hru Oběšenec.')
        hangman()
    
    elif "you from" in prikaz:
        talk("I'm from Vyskov. Where are you from?")
        print('Já jsem z vyškova. Odkud jsi ty?')

    elif "m from" in prikaz:
        talk("That's a nice place")
        print('To je hezké místo')

    elif "bug" in prikaz:
        talk("If you found a bug, tell Oskar.")
        print('Jestli si našel bug tak řekni Oskarovi.')

    elif "your favourite book" in prikaz:
        talk("My favourite book is Harry Potter, what are you reading?")
        print('Moje nejoblíbenější kniha je Harry Potter, co čteš ty?')

    elif "your favourite film" in prikaz:
        talk("My favourite film is Terminator, what is your favourite film?")
        print('Můj nejoblíbenější film je Terminátor, co je tvuj nejoblíbenější film?')

    elif 'my favourite book is' in prikaz:
        book = prikaz.replace("my favourite book is ", '')
        talk(book + "is good book")
        print(book, 'je dobrá kniha.')

    elif 'y favourite book' in prikaz:
        talk("That's good book")
        print('To je dobrá kniha.')

    elif 'my favourite film is' in prikaz:
        film = prikaz.replace('my favourite film is ', '') 
        talk(film + "is good film")
        print(film, 'je dobrý film.')

    elif 'y favourite film' in prikaz:
        talk("That's good film")
        print('To je dobrý film.')
    
    elif "u did today" in prikaz:
        talk("I was waiting to be triggered, what about you.")
        print("Čekala jsem než mě někdo spustí, co ty?")

    elif "i did today" in prikaz:
        talk("That must have been fun, I'd like to try that too")
        print('To musela být zábava, to bych si chtěla taky zkusit')
    
    elif "thank you" in prikaz:
        talk("You're welcome")
        print('není zač')
    
    elif 'do you like nature' in prikaz:
        talk('yes')
        print('ano')
    
    
    elif 'login' in prikaz:
        talk('Enter password')
        print('zadej heslo')
        password = getpass.getpass('Enter password')

        if password == '555oskar555':
            talk("login was successful")
            print('přihlášení bylo úspěšné')
            login = True
        
        else:
            talk('incorrect password')
            print('nesprávné heslo')

    elif 'sing me a song' in prikaz:
        talk('Get out Sara')
        print('Jdi pryč Sáro')

    
    elif 'wikipedia' in prikaz:
        question = prikaz.replace('wikipedia', '')
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)

    elif 'play' in prikaz:
        video = prikaz.replace('play ', '')
        playing = 'playing', video
        talk(playing)
        print('přehrávám', video)
        youtube(video)

    elif 'time' in prikaz:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
        print('Je', time)

    elif 'weather' in prikaz:
        url = 'https://www.google.com/search?q=po%C4%8Das%C3%AD&oq=po%C4%8Das%C3%AD&aqs=chrome..69i57j0i433i512j0i131i433i512j0i512j0i131i433i512l2j0i131i433l2j0i512l2.1797j1j15&sourceid=chrome&ie=UTF-8'
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, 'html.parser')
        weather = page_soup.findAll('span', {'id':'wob_tm'})
        
        talk('In vyskov is curently', weather, 'degres')
        print('Ve vyškově je aktuálně', weather, 'stupňů.')

    elif 'google' in prikaz:
        search = prikaz.replace('google', '')
        talk('searching' + search)
        print('vyhledávám', search)
        google(search)
    
    elif 'minecraft' in prikaz:
        talk("opening minecraft")
        print('otevírám minecraft')
        minecraft_run()
    
    elif 'hi' in prikaz:
      talk('Hello, how are you Oskar')
      print('Ahoj Oskare, jak se máš')

    elif 'hey' in prikaz:
      talk('Hello, how are you Oskar')
      print('Ahoj Oskare, jak se máš')

    #elif "do you" in prikaz:
        #talk('Yes and no')
        #print('ano i ne')

    #elif "favourite" in prikaz:
        #talk("you")
        #print('Ty')

    
    
    elif prikaz == 'quit':
        break

    else:
        talk("Sorry I don't know but you can add this reply (if it's a typo or bullshit please don't add it)")
        print('Promiň nevím ale můžeš mi tuto odpověď přidat (pokud je to překlep nebo blbost tak to prosím nepřidávej)')
        
        talk("Do you want to add an answer?")
        pridat = input('Chceš přidat odpověď? ')

        if pridat == 'yes':
            talk('ok')
            print('ok')

            talk("Ask the question I'm supposed to answer")
            question = input('Zadej otázku na kterou mám odpovědět: ')

            talk("Enter your English answer")
            en_answer = input('Zadej anglickou udpověď: ')

            talk("Type a Czech answer")
            cz_answer = input('Zadej českou odpověď: ')
            
            print("PRO OSKARA")
            print("_" * 50)
            add(question, en_answer, cz_answer)
            print("_" * 50)
            
            talk("Thank you, we will add your answer")
            print("Děkujeme, vaši odpověď přidáme")

        else:
            talk("Ok I'm not adding this answer")
            print("Ok, tuto odpověď nepřidám")

    

talk('Bye Oskar')
print('Ahoj Oskare')