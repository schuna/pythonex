import asyncio
import logging
import socket

logger_format = '%(asctime)s:%(threadName)s:%(message)s'
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%H:%M:%S")
HOST = '127.0.0.1'
PORT = 9999
TERMINATE = False


async def threaded(client_socket, addr):
    global TERMINATE
    logging.info(f'Connected by : {addr[0]} : {addr[1]}')

    while not TERMINATE:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            logging.info(f"Received from {addr[0]}:{addr[1]} : {decoded_data}")

            if "term" in decoded_data:
                TERMINATE = True

            logging.info(f"Send to {addr[0]}:{addr[1]} : {data.decode('utf-8')}")
            client_socket.send(data)
        except ConnectionResetError as e:
            logging.exception(e)
            break
    logging.info(f'Disconnected by {addr[0]}:{addr[1]}')
    client_socket.close()


async def serve():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    background_tasks = set()
    logging.info('server start')

    while not TERMINATE:
        logging.info('wait')
        client_socket, addr = server_socket.accept()

        task = asyncio.create_task(threaded(client_socket, addr))
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)
        await asyncio.sleep(1)

    server_socket.close()


if __name__ == '__main__':
    asyncio.run(serve())
