def calcular_vazao_maxima(N, R, L, tpoll):
  """
  Calcula a vazão máxima de um canal de difusão.

  Args:
    N: Número de nós.
    R: Taxa de transmissão em bps.
    L: Tamanho do quadro em bits.
    tpoll: Atraso do polling em segundos.

  Returns:
    A vazão máxima em Mbps.
  """

  # Calculando a vazão usando a fórmula
  vazao_bps = L / (L/R + tpoll)
  vazao_Mbps = vazao_bps / (10**6)

  return round(vazao_Mbps, 2)

# ctes para conversão
ms  = 10**-3
Mbps = 10**6
# Dados do problema
N = 5
R = 1 * Mbps
L = 12_000
tpoll = 3 * ms

# Calculando a vazão máxima
vazao_maxima = calcular_vazao_maxima(N, R, L, tpoll)

print("A vazão máxima do canal de difusão é:", vazao_maxima, "Mbps")
