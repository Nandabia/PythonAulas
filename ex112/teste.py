from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
# moeda.resumo(p, 20, 12) vai mudar a porcentagem de aumento e redução
