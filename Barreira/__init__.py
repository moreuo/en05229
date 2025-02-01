"""
Esse módulo implementa as barreiras do Zookeeper.
Mais informações podem ser encontradas em https://zookeeper.apache.org/doc/r3.9.3/recipes.html

As barreiras são importantes para sincronizar nós dentro de um sistemas distribuído.
Uma barreira, no Zookeeper, nada mais é do que um nó pai (ex. "/barreira") que recebe vários
nós filhos, os processos que devem ser sincronizados (ex. "/barreira/filósofo-1").

* Barreiras Comuns
Sincronizam o fim dos processos.

* Barreiras Duplas
Sincronizam o fim e o início dos processos.
"""