import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

with open('reader_script.txt', 'r', encoding="utf-8") as f:
    for s in f.readlines():
        speaker.Speak(s)
