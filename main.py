# Завдання 1
# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Хрестики — нулики». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч.
# import socket
# import threading
#
# server_socket = socket.socket(socket.AF_INET,
#                               socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 8080))
# server_socket.listen()
#
# clients = []
# words = []
#
# def broadcast(message):
#     for client in clients:
#         client.send(message.encode('utf-8'))
#
# def handle_client(client):
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             if message:
#                 if message == 'start':
#                     if len(clients) == 2:
#                         broadcast('Гра почалась.')
#                     else:
#                         client.send('Зачекайте поки приєднається ще один гравець.'.encode('utf-8'))
#                 elif message.startswith('слово:'):
#                     word = message.split(":")[1].strip()
#                     if word not in words:
#                         words.append(word)
#                         broadcast(f'Гравець {clients.index(client) + 1} сказав слово: {word}')
#                     else:
#                         client.send("Це слово вже було сказане".encode('utf-8'))
#                 elif message == 'exit':
#                     broadcast('Гра завершилась')
#                     break
#         except:
#             clients.remove(client)
#             break
#
# while True:
#     client_socket, _ = server_socket.accept()
#     clients.append(client_socket)
#     client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#     client_thread.start()


# Завдання 2
# Реалізуйте клієнт-серверний додаток з можливістю надсилати файли. Один користувач ініціює надсилання файлу, другий
# підтверджує. Після підтвердження починається надсилання.
# Якщо відправка була вдалою, повідомте про це відправника.
import socket
import os

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 55555))
server_socket.listen()

print('Підключення серверу ... ')

while True:
    client_socket, client_address = server_socket.accept()
    print(f"З'єднання з {client_address} встановлено.")

    filename = client_socket.recv(1024).decode('utf-8')
    print(f"Отриманий запит на файл: {filename}")

    if os.path.exists(filename):
        client_socket.send("Файл існує. Підтвердьте отримання".encode('utf-8'))
        confirmation = client_socket.recv(1024).decode('utf-8')

        if confirmation == 'підтверджено':
            with open(filename, 'rb') as file:
                file_data = file.read(1024)
                while file_data:
                    client_socket.send(file_data)
                    file_data = file.read(1024)
            print('Файл відправлено успішно.')
    else:
        client_socket.send("Файл не знайдено.".encode('utf-8'))

    client_socket.close()


