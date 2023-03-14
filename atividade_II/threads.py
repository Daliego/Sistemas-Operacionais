import threading

def imprimirNUmeros():
    for i in range(40):
        print(f"Sou a atividade 1 no nível {i}");

def main():
    myThread = threading.Thread(target=imprimirNUmeros);

    myThread.start();
    for i in range(20):
        print(f"Sou a atividade 2 no nível {i}");

    myThread.join()

    print("terminou o uso das thread");

main()