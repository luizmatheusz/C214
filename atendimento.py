import requests

# Função que calcula 
def calc_predio(nSala):
    nSala = int(nSala)
    if(nSala >= 1 and nSala <= 5):
        return '1'
    
    elif(nSala >= 6 and nSala <= 10):
        return '2'
    
    elif(nSala >= 11 and nSala <= 15):
        return '3'
    
    elif(nSala >= 16 and nSala <= 20):
        return '4'
    
    elif(nSala >= 21 and nSala <= 25):
        return '6'

def get_atendimento():
    response = requests.get(f"http://api.inatel.com/atendimento").json() # URL hipotética para obtenção das informações
    
    try:
        nPredio = calc_predio(response['sala']) # Cálculo do número do prédio com base no número da sala
        response['predio'] = [nPredio]
    except:
        response = {}
    
    return response