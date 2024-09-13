import requests

def calc_predio(nPredio):
    return (nPredio-1)/5

def get_atendimento():
    response = requests.get(f"http://api.inatel.com/atendimento").json() # URL hipotética para obtenção das informações
    nPredio = calc_predio(int(response['sala'])) # Cálculo do número do prédio com base no número da sala
    response['predio'] = [nPredio]
    return response