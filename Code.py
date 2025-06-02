import serial
import time
from pynput.keyboard import Controller

# Cria o controlador do teclado
keyboard = Controller()

# Tenta abrir a porta COM5
try:
    arduino = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)
except serial.SerialException:
    print("Erro: Não foi possível abrir a porta COM5.")
    exit()

print("Conectado ao Arduino! ✅")

while True:
    if arduino.in_waiting > 0:
        linha = arduino.readline().decode('utf-8').strip()
        print("Recebido:", linha)

        if linha == "Azul":
            keyboard.press('a')
            time.sleep(0.1)  # segura a tecla por 100ms
            keyboard.release('a')
        if linha == "Roxo":
            keyboard.press('s')
            time.sleep(0.1) 
            keyboard.release('s')
        if linha == "Verde":
            keyboard.press('d')
            time.sleep(0.1) 
            keyboard.release('d')
        if linha == "Vermelho":
            keyboard.press('f')
            time.sleep(0.1)  
            keyboard.release('f')
        if linha == "Amarelo":
            keyboard.press('g')
            time.sleep(0.1)  
            keyboard.release('g')

