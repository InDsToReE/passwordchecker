import itertools
import string
import time
import sys
import random
import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name or "Alex" in voice.name or "Google" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 140)  # Kecepatan lebih cepat
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def hacker_effect(text, delay=0.001, overwrite=False):
    if overwrite:
        sys.stdout.write("\r" + " " * 100 + "\r")  # Hapus baris sebelumnya
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if not overwrite:
        print()

def print_boxed_text(title, content):
    box_width = max(len(line) for line in content.split('\n')) + 6
    border = "╔" + "═" * box_width + "╗"
    print(border)
    print(f"║ {title.center(box_width - 2)} ║")
    print("╠" + "═" * box_width + "╣")
    for line in content.split("\n"):
        print(f"║ {line.ljust(box_width - 2)} ║")
    print("╚" + "═" * box_width + "╝")

def brute_force_password(password):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempt_count = 0
    found_chars = ['_'] * len(password)
    
    sys.stdout.write("\033[92m[CRACKING PASSWORD] >> " + "_" * len(password) + "\033[0m")
    sys.stdout.flush()
    
    for index in range(len(password)):
        for char in chars:
            attempt_count += 1
            found_chars[index] = char
            attempt_password = ''.join(found_chars)
            sys.stdout.write("\r\033[92m[CRACKING PASSWORD] >> " + attempt_password + "\033[0m")
            sys.stdout.flush()
            time.sleep(0.05)
            if attempt_password[:index+1] == password[:index+1]:
                break
    
    print()
    return attempt_count, ''.join(found_chars)

# Tambahkan while loop di bagian utama program
while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    speak("Welcome To Password Cracker")
    hacker_effect("\033[96m██████╗  █████╗ ███████╗ ██████╗███████╗██████╗ \033[0m")
    hacker_effect("\033[96m██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗\033[0m")
    hacker_effect("\033[96m██████╔╝███████║███████╗██║     █████╗  ██████╔╝\033[0m")
    hacker_effect("\033[96m██╔═══╝ ██╔══██║╚════██║██║     ██╔══╝  ██╔══██╗\033[0m")
    hacker_effect("\033[96m██║     ██║  ██║███████║╚██████╗███████╗██║  ██║\033[0m")
    hacker_effect("\033[96m╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝\033[0m")
    time.sleep(1)

    device_info = "CPU: Intel Core i7\nRAM: 16GB\nOS: Linux/Windows/Mac"
    author_info = "Author: Riski\nGitHub: github.com/InDsToReE"
    hacker_effect("\033[91mSYSTEM INITIALIZING...\033[0m", delay=0.009)
    time.sleep(0.1)
    hacker_effect("\033[93mLOADING CYBER MODULES...\033[0m", delay=0.009)
    time.sleep(0.1)
    print_boxed_text("DEVICE SPECIFICATIONS", device_info)
    print_boxed_text("SCRIPT INFORMATION", author_info)

    hacker_effect("\033[96mSYSTEM BOOTING COMPLETE.\033[0m", delay=0.009)
    time.sleep(0.1)
    hacker_effect("\033[92mREADY TO DEPLOY PASSWORD CRACKER\033[0m", delay=0.009)
    time.sleep(0.1)
    password = input("\n\033[95mENTER TARGET PASSWORD: \033[0m")
    hacker_effect("\n\033[94mPROCESSING...\033[0m", delay=0.009)
    time.sleep(1)

    attempts, cracked_password = brute_force_password(password)

    if cracked_password:
        hacker_effect(f"\n\033[92m[ACCESS GRANTED] PASSWORD FOUND: {cracked_password}\033[0m")
        hacker_effect(f"\033[94m[TOTAL ATTEMPTS] {attempts}\033[0m")
    else:
        speak("Access Denied")
        hacker_effect("\n\033[91m[ACCESS DENIED] PASSWORD NOT FOUND\033[0m")
    
    # Tambahkan prompt untuk melanjutkan atau keluar
    lanjut = input("\n\033[95mIngin mencoba lagi? (y/n): \033[0m").lower()
    if lanjut != 'y':
        speak("Thank you for using Password Cracker")
        hacker_effect("\n\033[92mTerima kasih telah menggunakan Password Cracker!\033[0m")
        break
