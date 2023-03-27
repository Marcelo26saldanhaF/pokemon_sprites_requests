import concurrent.futures
import os
import requests
from time import time



def request_multiprocess(number):
    os.chdir(r'C:\Users\marce\OneDrive\Área de Trabalho\bancopython\async io\pokemon_mutiprocess')
    url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png'
    result=requests.get(url,stream=True)
    with open(f'imagem_{number}.png','wb') as doc:
        for chunck in result.iter_content():
            doc.write(chunck)


lista=[i for i in range(1,151)]

if __name__=="__main__":
        start=time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(request_multiprocess,lista)
        
        end=time()

        
        print(f'tempo para concluir {end-start}')


# tempo='5.542802572250366'

