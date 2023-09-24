
import time
import threading
import pyautogui
import keyboard


def autoclicker():
    while not exit_signal.is_set():
        if click_signal.is_set():
            pyautogui.click()
        time.sleep(0.01)


def start_clicking(e):
    click_signal.set()
    print("Auto Clicker started with 'F' key.")


def stop_clicking(e):
    click_signal.clear()
    print("Auto Clicker stopped with 'G' key.")


def exit_program(e):
    exit_signal.set()
    click_signal.set()  
    print("Exiting the Auto Clicker with 'P' key.")
    exit()


click_signal = threading.Event()
exit_signal = threading.Event()


keyboard.on_press_key('f', start_clicking)
keyboard.on_press_key('g', stop_clicking)
keyboard.on_press_key('p', exit_program)


click_thread = threading.Thread(target=autoclicker)
click_thread.start()


click_thread.join()
