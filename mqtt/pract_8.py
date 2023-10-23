"""
На любом языке программирования реализуйте программу (скрипт), которая бы
каждые 5 секунд упаковывала последние полученные данные в файлы формата
JSON и XML. В одной записи должно быть 6 полей: 4 показаний датчиков, время
формирования файла, номер чемодана (последние две цифры IP-адреса).
"""

import time
from datetime import datetime
from pickle import dump

import paho.mqtt.client as mqtt

HOST = "192.168.2.27"
PORT = 1883
KEEPALIVE = 5
STAND_NUMBER = 27

SAVE_INTERVAL = 1

SUB_TOPICS = {
    '/devices/wb-msw-v3_21/controls/Current Motion': 'motion',
    '/devices/wb-ms_11/controls/Temperature': 'temperature',
    '/devices/wb-mir_19/controls/Input Voltage': 'voltage',
}

DATA_DICT = {}
data = []


def on_connect(client, userdata, flags, rc):
    """ Функция, вызываемая при подключении к брокеру """
    if rc != 0:
        raise Exception(f"Connection code {str(rc)}")

    print("Succesfully connected!")

    for topic in SUB_TOPICS.keys():
        client.subscribe(topic)


def on_message(client, userdata, msg):
    """ Функция, вызываемая при получении сообщения от брокера по одному из отслеживаемых топиков """
    payload = msg.payload.decode()  # Основное значение, приходящее в сообщение, например, показатель температуры
    topic = msg.topic  # Топик, из которого пришло сообщение, поскольку функция обрабатывает сообщения из всех топиков

    param_name = SUB_TOPICS[topic]

    DATA_DICT[param_name] = payload
    DATA_DICT['time'] = str(datetime.now())
    DATA_DICT['stand_number'] = STAND_NUMBER


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, KEEPALIVE)

    last_save_time = time.time()

    client.loop_start()

    current = time.time()
    end = current + (60 * 10)

    while True:
        current_time = time.time()
        if current_time - last_save_time >= SAVE_INTERVAL:
            last_save_time = current_time
            data.append(DATA_DICT)
            print(len(data))

        if time.time() > end:
            print("finish")
            break

    with open("file.bin", "wb") as f:
        dump(data, f)


if __name__ == "__main__":
    main()
