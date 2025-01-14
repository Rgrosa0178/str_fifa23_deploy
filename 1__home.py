import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime
import openai

# para carregar os dados do df. esse if significa que se não há dados no sessio state, executa os filtros
if 'data' not in st.session_state:
    df_data = pd.read_csv(
        "datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    # filtra jogadores com contrato valido na data de hoje
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

# cria título da página
st.markdown('# FIFA23 OFFICIAL DATASET! ⚽️')
# cria sidebar e coloca texto. dentro dos colchetes pode ser colocado links
st.sidebar.markdown(
    'Desenvolvido por [https://www.instagram.com/rodrigoguirosa/] Rodrigo Guimarães Rosa')

# cria botão para acessar páginas
btn = st.button('Acesse os dados no Kaggle')
# quando clicar botão será direcionado para a pagina descrita
if btn:
    webbrowser.open_new_tab(
        'https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')


st.markdown(
    """
 O conjunto de dados
 de jogadores de futebol de 2023 fornece informações
 abrangentes sobre jogadores de futebol profissionais.
 O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos
 do jogador, características físicas, estatísticas de jogo, detalhes do contrato e
 afiliações de clubes.

 Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para
 analistas de futebol, pesquisadores e entusiastas interessados em explorar vários
 aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de
 desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e
 desenvolvimento do jogador ao longo do tempo.""")