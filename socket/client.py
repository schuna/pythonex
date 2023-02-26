import asyncio
import logging
import socket

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")
HOST = '127.0.0.1'
PORT = 9999

TERMINATE = False


async def send_data(client_socket):
    global TERMINATE
    logging.info(f"send data ... from {client_socket.__repr__()}")
    await asyncio.sleep(1)
    while not TERMINATE:
        message = input('Enter Message: ')
        if message == 'quit':
            TERMINATE = True
        try:
            logging.info(f'send to the server: {message}')
            client_socket.send(message.encode())
            data = client_socket.recv(1024)
            logging.info(f'received from the server: {repr(data.decode())}')
        except ConnectionResetError as e:
            logging.exception(e)
            break


async def client():
    background_tasks = set()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    logging.info(f'Connecting to {HOST}:{PORT}')

    task = asyncio.create_task(send_data(client_socket))
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)

    while not TERMINATE:
        logging.info(f"sleep before terminating")
        await asyncio.sleep(1)

    client_socket.close()


if __name__ == '__main__':
    asyncio.run(client())
