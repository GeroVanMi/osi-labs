import os
import socket
import argparse
import subprocess
from datetime import datetime

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 16400  # Port to listen on (non-privileged ports are > 1023)
LOG_DIR_PATH = './../log/'
LOG_FILE_PATH = f'{LOG_DIR_PATH}/log.txt'


def install():
    print('Running install procedure...')
    if not os.path.exists(LOG_DIR_PATH):
        subprocess.run([f'mkdir {LOG_DIR_PATH}'], shell=True)
    subprocess.run([f'touch {LOG_FILE_PATH}'], shell=True)
    print('Created log file. Completed.')

    # We do not have `sudo` rights, so this code doesn't work.
    # subprocess.run(['sudo chattr =a log.txt'], shell=True)
    # print('Set permissions.')


def log_file_exists():
    return os.path.exists(LOG_FILE_PATH)


def start_service():
    if not log_file_exists():
        raise OSError("Log file does not exist! Please run with --install [--i] option first.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Started log server. Now listening for entries.")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(f"Received log entry: {data}")
                with open(LOG_FILE_PATH, mode='a') as file:
                    date = datetime.now()
                    file.write(f"{date.strftime('%d.%m.%Y %H:%M:%S')}: " + data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--install', '--i',
        action='store_true',
        dest='install_mode_is_enabled',
        help='Runs the installation pipline. Mandatory on the first run.'
    )

    args = parser.parse_args()

    if args.install_mode_is_enabled:
        install()
    else:
        start_service()
