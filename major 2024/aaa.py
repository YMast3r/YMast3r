import speech_recognition as sr

def escuchar_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiental
        audio = recognizer.listen(source, timeout=5)

    try:
        texto = recognizer.recognize_google(audio, language='en-US')  # Reconocer el audio usando Google Speech Recognition
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print(f"Error al obtener resultados del servicio de reconocimiento de voz; {e}")
        return ""

# Escuchar durante 10 segundos
texto_escuchado = escuchar_audio()

print("Texto escuchado:", texto_escuchado)
