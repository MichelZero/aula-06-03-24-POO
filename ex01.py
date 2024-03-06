# autor: Michel Silva
# data: 06/03/2024
# assunto: Resolver problemas em física de atrito usando funções Python

# Abordagens:
# 1. Força de atrito estática:
#     * Coeficiente de atrito estático: mu_s
#     * Força máxima de atrito estática: F_fs = mu_s * N
# 2. Força de atrito cinética:
#     * Coeficiente de atrito cinético: mu_k
#     * Força de atrito cinética: F_fk = mu_k * N
# 3. Casos:
#  * Objeto em repouso:
#    * Se F < F_fs, o objeto permanece em repouso.
#    * Se F > F_fs, o objeto começa a deslizar.
#  * Objeto em movimento:
#    * A força de atrito cinética se opõe ao movimento.

# Funções Python:
#  * Função para calcular a força de atrito estática:
def forca_atrito_estatica(mu_s, N):
  """
  Calcula a força de atrito estática.

  Argumentos:
    mu_s: Coeficiente de atrito estático.
    N: Força normal.

  Retorno:
    Força de atrito estática.
  """
  return mu_s * N


# * Função para calcular a força de atrito cinética:
def forca_atrito_cinetica(mu_k, N):
  """
  Calcula a força de atrito cinética.

  Argumentos:
    mu_k: Coeficiente de atrito cinético.
    N: Força normal.

  Retorno:
    Força de atrito cinética.
  """
  return mu_k * N

