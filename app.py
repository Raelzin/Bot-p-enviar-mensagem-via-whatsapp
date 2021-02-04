# importar bibliotecas necessárias

import pywhatkit
import keyboard
import time
from datetime import datetime

# definir contatos, necessário colocar o número neste formato: +5585912345678

contatos = ['']

# intervalo de envio p/ cada contato

while len(contatos) >= 1:
    # enviar mensagens
    
    pywhatkit.sendwhatmsg(contatos[0], 'mensagem', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(15)
    keyboard.press_and_release('ctrl + w')
