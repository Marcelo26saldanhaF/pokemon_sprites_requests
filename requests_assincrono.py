import requests
import os
from time import time
import aiohttp
import asyncio
#assincrono

async def assyncronous_request(session,number):

    os.chdir(r'C:\Users\marce\OneDrive\Área de Trabalho\bancopython\async io\pokemons_assincronos')
    url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
    async with session.get(url) as response:
        result=await response.content.read()
        with open(f'imagem{number}.png','wb') as doc:
           doc.write(result)

            

async def main():
    async with aiohttp.ClientSession() as session:
        result=await asyncio.gather(*[assyncronous_request(session,number) for number in range(1,151) ])
        


start=time()
asyncio.run(main())
end=time()

print(f'concluido em {end-start}')

# time=" 0.6742515563964844"