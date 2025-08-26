import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode

mouse = MouseController()
stop_key = KeyCode(char='k')
running = True

def on_press(key):
    global running
    if key == stop_key:
        running = False
        return False

print("O programa começará em 5 segundos...")
time.sleep(5)

with Listener(on_press=on_press) as listener:
    print("Segurando clique esquerdo... pressione 'k' para parar.")
    mouse.press(Button.left)  # segura uma vez só
    while running:
        time.sleep(0.01)  # pausa mínima (alivia CPU)k
    mouse.release(Button.left)
    listener.join()

print("Programa finalizado.")

