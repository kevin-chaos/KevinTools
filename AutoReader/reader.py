import win32com.client


def auto_reader(file_path=None):
    if not file_path:
        file_path = 'reader_script.txt'
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    with open(file_path, 'r', encoding="utf-8") as f:
        for s in f.readlines():
            speaker.Speak(s)


if __name__ == "__main__":
    auto_reader()