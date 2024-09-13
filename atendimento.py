import requests

def calc_predio(response):
    nPredio = (int(response['sala'])-1)/5
    return nPredio

def get_atendimento():
    response = requests.get(f"http://api.inatel.com/atendimento").json() # URL hipotética para obtenção das informações
    nPredio = calc_predio(response) # Cálculo do número do prédio com base no número da sala
    response['predio'] = [nPredio]
    return response