import streamlit as st

#configura a página para ocupar todo espaço horizontal da tela
st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
    )
#lê e traz os dados filtrados do df da aba home.py 
df_data = st.session_state['data']

#constroi seletor filtrando pela coluna clubes
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

#filtra todos os jogadores que aparecem no df por clube
df_players = df_data[(df_data['Club'] == club)]
#escolher jogadores pelo nome e indexa
players = df_players["Name"].value_counts().index
#constroi seletor filtrando pela coluna jogadores
player = st.sidebar.selectbox("Jogador", players)

#grava na variável as estatíticas com nome dos jogadores conforme sua localização no índice 
player_stats = df_data[df_data["Name"] == player].iloc[0]
#imprime na tela a imagem do jogador filtrado no sidebar
st.image(player_stats["Photo"])
#imprime nome do jogador filtrado no sidebar
st.title(player_stats["Name"])
#imprime nome do clube do jogador **para negritar
st.markdown(f"**Clube:** {player_stats['Club']}")
#imprime a posição do jogador 
st.markdown(f"**Posição:** {player_stats['Position']}")

#constrói colunas 
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
#cria linha 
st.divider()

#cria um titulo na pagina menor do que a função st.title  
st.subheader(f"Overall {player_stats['Overall']}")
#constrói uma imagem de progresso que varia conforme a nota do overall do jogador
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
