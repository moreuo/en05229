from kazoo.client import KazooClient


class BarreiraSimples:
    """Barreiras que sincronizam somente a saída de processos."""

    def __init__(self): ...

    def barrier_wait(self): ...
