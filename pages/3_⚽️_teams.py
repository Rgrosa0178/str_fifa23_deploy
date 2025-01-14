import streamlit as st


st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)
#lê e traz os dados filtrados do df da aba home.py 
df_data = st.session_state["data"]

#constroi seletor filtrando pela coluna clubes
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

#filtra apenas por clubes que estão armazenados nos selectbox da linha anterior e o .set_index (índice 0) será o nome do jogador
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

#coloca imagem do clube e no markdown o nome bem grande do clube 
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

#imprime colunas selecionadas pelas strings abaixo.
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

#deixa a apresentação dos dados dentro do DF mais visuais e usa o dataframe, data elements, st.column_config da biblioteca streamlit
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })