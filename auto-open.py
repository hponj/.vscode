import webbrowser
import keyboard

# Daftar URL yang ingin Anda buka
urls = [
    'https://www.figma.com/',
]

# Buka setiap URL dalam tab baru
for url in urls:
    while not keyboard.press("k"):
        webbrowser.open_new_tab(url)
