# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    filename = input("Ingrese el nombre del archivo: ")
    
    with open(filename, "r") as f:
        n = int(f.readline())
        monitor = temp_monitor.init(n)
        for i in range(n):
            temp = float(f.readline())
            monitor = temp_monitor.add_reading(monitor, temp)
    print(temp_monitor.longest_rising_streak(monitor))
    pass


if __name__ == "__main__":
    main()
