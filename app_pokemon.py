import streamlit as st
import json
import requests

st.set_page_config(layout="wide")

with open('pokemon_index.json', 'r', encoding='utf-8') as arquivo:
    nomes_pokemons = json.load(arquivo)

nome = st.selectbox('Escolha um Pokemon', nomes_pokemons.values())

url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
dados_pokemon = requests.get(url).json()

co11, co12, co13 = st.columns(3)

peso = dados_pokemon['weight'] /10
altura = dados_pokemon['height'] /10
imc = round(peso / (altura** 2 ))

with co11:
    st.image(dados_pokemon['sprites']['front_default'], width=400)
    st.write('Normal') 

with co12:
    st.audio(dados_pokemon['cries']['latest'])
    st.audio(dados_pokemon['cries']['legacy'])


with co13:
    st.image(dados_pokemon['sprites']['front_shiny'], width=400)
    st.write('Shiny')


co11, co12, co13 = st.columns(3)
with co11:
    st.metric('Altura', f'{altura} M')

with co12:
    st.metric('IMC', imc)

with co13:
    st.metric('Peso', f'{peso} KG')