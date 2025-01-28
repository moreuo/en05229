import threading
import time

from kazoo.client import KazooClient

# Conexão com o ZooKeeper
zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()

# Nó da barreira
barrier_path = "/barreira"
zk.ensure_path(barrier_path)


def philosopher(name):
    while True:
        print(f"{name} está pensando...")
        time.sleep(2)  # Pensando

        print(f"{name} está tentando comer...")
        zk.create(f"{barrier_path}/{name}", ephemeral=True)  # Entrar na barreira

        # Esperar outros filósofos liberarem a barreira
        time.sleep(2)

        zk.delete(f"{barrier_path}/{name}")  # Sair da barreira
        print(f"{name} terminou de comer e voltou a pensar.")


# Simulação de 5 filósofos
threads = []
for i in range(5):
    t = threading.Thread(target=philosopher, args=(f"Filósofo-{i + 1}",))
    threads.append(t)
    t.start()

# Aguarde a execução
for t in threads:
    t.join()

# Finalizar ZooKeeper
zk.stop()
