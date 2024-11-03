
import requests
import json

def cotacao(escolha=1):
    moeda = 0
    if escolha == 1:
        moeda = 'USDBRL'
    elif escolha == 2:
        moeda = 'EURBRL'
    elif escolha == 3:
        moeda = 'BTCBRL'
    else:
        return 'Moeda inválida!'

    url = 'https://economia.awesomeapi.com.br/json/last/'+ moeda[0:3] +'-'+ moeda[3:6]

    
    #Capturando a cotação
    cotacao = requests.get(url).content

    print(cotacao)
    #Extraindo a cotação
    dic = json.loads(cotacao)


    #Exibindo os resultados em tela
    return float(dic[moeda]["bid"])

print("Cotacao - Dolar - ", cotacao(1))
print("Cotacao - Euro - ",cotacao(2))
print("Cotacao - BitCoin - ",cotacao(3))