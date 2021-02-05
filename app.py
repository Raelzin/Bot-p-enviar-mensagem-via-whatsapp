# importar bibliotecas necessárias

import pywhatkit
import keyboard
import time
from datetime import datetime

# definir contatos, necessário colocar o número neste formato: +55DDD912345678

lista_contatos = ['']

# intervalo de envio p/ cada contato

while len(lista_contatos) >= 1:
    # enviar mensagens
    
    pywhatkit.sendwhatmsg(lista_contatos[0], 'mensagem', datetime.now().hour,datetime.now().minute + 2)
    del lista_contatos[0]
    time.sleep(15)
    keyboard.press_and_release('ctrl + w')
