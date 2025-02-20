""" 
ASISTENTE POR VOZ
"""
import pyttsx3 as tts               #importa las librerias que hemos descargado previamente 
import speech_recognition as sr     #no vienen con python
import datetime

#https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
#removing sensitive data from project
#https://git-scm.com/book/en/v2/Git-Branching-Rebasing

def audio_a_texto():

    #Objeto para reconocer el audio, (estas librerias funcionan con poo)
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as source:  #with palabra reservada para abrir cosas(dispositivos y ficheros)

        #Tiempo de espera hasta que se activa el micro  / desde que la funcion arranca hasta que se activa el micro, no es insta
        r.pause_threshold = 0.8 #si funciona bajar un poco el t hasta encontrar punto 
            #llamamos la pausa en el objeto con el que estamos trabajando
        
        #Mensaje al usuario para que sepa que ya puede hablar
        print("Ya puedes hablar. ")

        #Variable para guardar el audio
        audio = r.listen(source)    #r es el objeto y escucha al source(la fuente)

        try:
            text = r.recognize_google(audio, lenguage="es")
            
            #mostrar en pantalla el audio capturado
            print("Voz reconozida: ", text)
            return text
        except sr.UnknownValueError: #que no pueda usar el micro o no funciona
            print("El micro no funciona.")
            return "Error"  #no hace falta seguir ejecutando
        
        except sr.RequestError:  #que el micro funcione pero falle alguna de las instrucciones, cuando no puede generar el texto
            print("Falla la transcripcion del texto.")
            return "Error"
        
        except:
            print("Error no identificado")
            return "Error"
        
# audio_a_texto()

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

def respuesta_maquina(text):

    #Iniciar el motor de pyttsx3, normalmente variable engine
    engine = tts.init() #iniciamos la libreria

    #Ajustes
    # rate = engine.getProperty("rate")   #velocidad, asignar no hace falta, en todo caso para guardar el valor original
    engine.setProperty("rate", 150)

    # volumen = engine.getProperty("volume")  #volumen
    engine.setProperty("volume", 1)

    engine.setProperty("voice", id1)  #voz

    engine.say(text)    #lo que queremos que diga

    engine.runAndWait()   #no queremos que la aplicacion finalize nadamás ejecutarse una vez, queremos poder indicarle mas cosas que decir

# respuesta_maquina("hello i'm a bot ")
# engine = tts.init()                         #hay que iniciar la libreria
# for voz in engine.getProperty("voices"):    #para ver que voces estan instaladas en la maquina, de aqui sacamos id1 e id2
#     print(voz)

def decir_dia_semana():

    dia_actual = datetime.date.today()
    # print(dia)
    dia_semana = dia_actual.weekday()   #devuelve el numero de dia
    print(dia_semana)

    #nombres de los dias
    dias_esp = ("lunes","martes","miércoles","jueves","viernes","sábado","domingo")    #tupla

    respuesta_maquina(f"Hoy es {dias_esp[dia_semana]}")
# decir_dia_semana()

def decir_la_hora():

    #guardar la hora
    hora_actual = datetime.datetime.now()   #objeto timpo datetime, se le puede pedir propiedades
    # print(hora_actual)
    hora = f"En este momento son las {hora_actual.hour} horas, {hora_actual.minute} minutos y {hora_actual.second} segundos."   #lo que va a decir
    respuesta_maquina(hora)

# decir_la_hora()

def saludo_inicial():

    hora_actual = datetime.datetime.now().hour  #sólo la hora
    #momento del dia
    if 6 < hora_actual < 14:
        momento = "Buenos días"
    elif 14 <= hora_actual < 20:
        momento ="Buenas tardes"
    else:
        momento = "Buenas noches"
    saludo = f"{momento}, soy Axela, tu asistente personal"
    respuesta_maquina(saludo)
    respuesta_maquina("En que te puedo ayudar?")

# saludo_inicial()

#funcion que lanza las demás
def funcion_principal():

    #que empieze saludando, y que solo salude cuando arranca
    saludo_inicial()
    
    #bucle infinito para que escuche lo que le vamos a  pedir

    activo = True
    while activo:

        peticion = audio_a_texto().lower()
        print(peticion)

        if peticion == "silencio":  #para terminar el bucle
            activo = False

funcion_principal()