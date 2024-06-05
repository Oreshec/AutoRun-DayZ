import time
import keyboard as kb
import os
import multiprocessing
import signal


def main():
    time.sleep(3)  # Время, что бы открыть игру
    kb.press("w+shift")  # Зажимаем клавишу
    # time.sleep(0.5)  # Время, которое персонаж должен бежать
    # keyboard.release("W")  # Отжимаем клавишу
    # keyboard.release("w+shift")


def hook(pid):
    kb.release("w+shift")
    while True:
        if kb.is_pressed('ctrl + 1'):
            os.kill(pid, signal.SIGTERM)
            os._exit(1)


if __name__ == '__main__':
    pid = os.getpid()
    multiprocessing.Process(target=main).start()
    multiprocessing.Process(target=hook, args=[pid]).start()
