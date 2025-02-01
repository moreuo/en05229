from kazoo.client import KazooClient


class BarreiraDupla:
    """Barreiras que sincronizam o começo e o fim dos processos."""

    def __init__(self): ...

    def barrier_enter(self): ...

    def barrier_leave(self): ...
