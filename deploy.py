import os
import sys

def deploy():
    # Установка необходимых пакетов
    os.system("pip install -r requirements.txt")

    # Запуск приложения
    os.system("python main.py")

if __name__ == "__main__":
    deploy()