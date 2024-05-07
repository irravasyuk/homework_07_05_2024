# import socket
#
# client_socket = socket.socket(socket.AF_INET,
#                               socket.SOCK_STREAM)
#
# client_socket.connect(('127.0.0.1', 8080))
#
# while True:
#     message = input('Чекаємо на ще одного гравця. Нажміть (start) для початку гри: ')
#     client_socket.send(message.encode('utf-8'))
#
#     server_response = client_socket.recv(1024).decode('utf-8')
#     print(server_response)
#
#     if server_response == 'Гра завершилась':
#         break
#
#     if server_response == 'Гра почалась.':
#         while True:
#             word = input('Ваш хід. Напишіть слово: ')
#             client_socket.send(f"слово: {word}".encode('utf-8'))
#             response = client_socket.recv(1024).decode('utf-8')
#             print(response)
#             if response == 'Це вже слово було':
#                 continue
#             elif response.startswith('Гравець'):
#                 break
#
# client_socket.send('Завершено'.encode('utf-8'))
# client_socket.close()


#2
import socket

client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 55555))

filename = input('Введіть назву файлу для запиту: ')
client_socket.send(filename.encode('utf-8'))

response = client_socket.recv(1024).decode('utf-8')
print(response)

if response == 'Такий файл існує. Підтвердьте отримання.':
    confirmation = input('Ви хочете отримати файл (так/ні) ?')
    if confirmation.lower() == 'так':
        client_socket.send('підтверджено'.encode('utf-8'))

        with open(filename, 'wb') as file:
            while True:
                file_data = client_socket.recv(1024)
                if not file_data:
                    break
                file.write(file_data)

        print('Файл успішно отримано.')
    else:
        print('Сталась помилка при отриманні.')

client_socket.close()






















