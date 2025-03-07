"""
My first app
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Oiiii AMOOOR!!!! Primeiramente gostaria de dizer que te amo muito grandusculamente grandusculo (eu realmente nao vivo sem voce)')

st.write('To vindo aqui te mostrar parte dos meus estudos para a criacao de um portifolio que vai ajudar a gente a ganhar um dinheirinho daqui um tempo. '
         'Por favor, nao se incoode com os errinhos de portugues :) (o teclado e americano)')

st.write('Here is our first attempt at using data to create a table: ')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' %i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['a', 'b', 'c']
)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [25, 25] + [-15.788899064724513, -47.88929213361725],
    columns= ['lat', 'lon']
)

st.map(map_data)

