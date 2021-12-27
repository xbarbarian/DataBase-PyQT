import subprocess
import time
process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер, k - запустить клиенты x - закрыть все окна:')
    if action == 'q':
        break
    elif action == 's':
        # Запускаем сервер!
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'k':
        try:
            clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
            # Запускаем клиентов:
            time.sleep(0.5)
            for i in range(clients_count):
                process.append(
                    subprocess.Popen(f'python client.py -n test{i}', creationflags=subprocess.CREATE_NEW_CONSOLE))
        except:
            pass

    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()
            victim.terminate()
