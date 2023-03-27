import requests
import os
from time import time

#syncronous

def syncronous_request(diretorio):

    for number in range(1,151):
        os.chdir(diretorio)
        url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
        results=requests.get(url,stream=True)
        with open(f'imagem{number}.jpg','wb') as doc:
            for i in results.iter_content():
                doc.write(i)
                
        


start=time()
syncronous_request(r"C:\Users\marce\OneDrive\Área de Trabalho\bancopython\async io\pokemons_sincrono")
end=time()

print(f'concluido em {end-start}')

#tempo="concluido em 26.831228256225586"

   


