import requests
import pandas as pd
import json

limit = 10
# Função para extrair dados da API;
def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao extrair os dados da API: {response.status_code}")
        return None
    
#load
def load_data(data, path):
    id = data["id"]
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file) #converte para json e escreve no arquivo diretamente

    
def loop_data(endpoint):
    url = "https://dummyjson.com/" + endpoint
    i = 1
    
    while True:
        data = extract_data(url + "/" + str(i))
        if data and i < limit:
            load_data(data, "raw/" + endpoint)
        elif i >= limit:
            break
            
        else:
            print(f"Erro ao extrair dados do endpoint: {endpoint}")
            break
        i += 1  



#for endpoint in endpoints:
 #  loop_data(endpoint)


def transform_data_json_to_csv(endpoint, i):
    print(f"transormando {endpoint}/{i}.json para csv")
    with open(f"raw/{endpoint}/{i}.json", "r") as file:
        data = json.load(file)
        #convertendo o json para CSV
    df = pd.DataFrame([data])
    df.to_csv(f"curated/{endpoint}/{i}.csv", index=False)    
    
def load_to_single_csv(endpoint):
    df_total = pd.DataFrame()
    for i in range(1, limit + 1):
        try:
            df = pd.read_csv(f"curated/{endpoint}/{i}.csv")
            df_total = pd.concat([df_total, df], ignore_index = True)
        except FileNotFoundError:
            print(f"O arquivo {i}.csv não foi encontrado!")    
    df_total.to_csv(f"load/{endpoint}_final.csv", index=False) 
    print(f"{endpoint}_final.csv salvo na pasta 'load'")   

def etl_pipeline(endpoint):
    loop_data(endpoint) #extract

    for i in range(1, limit + 1):
        transform_data_json_to_csv(endpoint, i) #transform

    load_to_single_csv(endpoint) #junta todos os arquivos




endpoints = ["user", "products"]

for endpoint in endpoints:
    etl_pipeline(endpoint)