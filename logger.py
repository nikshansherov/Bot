from datetime import datetime as dt

def log(value):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(value)
        if value == 'C':
            file.write(f"\t Время операции: {dt.now().strftime('%d-%m-%Y %H:%M:%S')}")
            file.write('\n')