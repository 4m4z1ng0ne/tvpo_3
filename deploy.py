import os
import subprocess
import sys

def deploy():
    try:
        # Остановка текущего приложения (если оно запущено)
        print("Stopping current application...")
        subprocess.run(["pkill", "-f", "your_app.py"], check=False)  # Не проверяем код возврата, так как процесс может не существовать
        
        # Обновление зависимостей (если требуется)
        print("Updating dependencies...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        
        # Применение миграций базы данных (если используется Django)
        print("Applying database migrations...")
        subprocess.run(["python", "manage.py", "migrate"], check=True)
        
        # Сбор статических файлов (если используется Django)
        print("Collecting static files...")
        subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)
        
        # Запуск приложения
        print("Starting application...")
        subprocess.Popen(["python", "your_app.py"])  # Замените на имя вашего основного файла
        
        print("Deployment completed successfully!")
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error during deployment: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(deploy())