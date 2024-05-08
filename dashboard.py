from filer import Filer
import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Dashboard Sólida Construções Ltda', layout='wide')

if __name__ == '__main__':
    filer = Filer()
    df = filer.run(filename='./spreadsheets-dashboard/nfe.xlsx')
    df_destinatarios = filer.run(filename='./spreadsheets-dashboard/nfe-destinatarios.xlsx')
    df_resultado = pd.merge(df, df_destinatarios,left_on='Número da NF-e', right_on='Número da NF-e', how='left')

    with st.sidebar:
        st.header("Dashboard Sólida Construções Ltda. ")
        st.subheader("""
            Dashbooard pensado para visualizar e analisar os dados da planilha de dados com notas ficais e averiguar possíveis problemas que estão afetando a empresa com o cancelamento de notas.
        """)
    col1,col2 = st.columns(2,gap='large', )
    col3, col4 = st.columns(2, gap='large')
    col5, col6 = st.columns(2, gap='large')
    
    col3.divider()
    col4.divider()
    col5.divider()
    col6.divider()

    # gráfico de pizza para situação
    contagem_situacoes = df_resultado['Situação'].value_counts().reset_index()
    contagem_situacoes.columns = ['Situação', 'Quantidade']
    fig = px.pie(contagem_situacoes,values='Quantidade', names="Situação", title="Situação das NF-e")
    col1.plotly_chart(fig, use_container_width=True)

    # gráfico de barra horizontal pra apresentar a razoes pelos cancelamentos
    df_filtered = df_resultado[df_resultado['Situação'] == 'Cancelado']
    fig = px.bar(df_filtered, y="Motivo de cancelamento", title="Motivo de cancelamento", orientation="h")
    col2.plotly_chart(fig, use_container_width=True)

    # Situação dos itens por marca
    fig = px.bar(df_resultado, x='Marca',color='Situação', title='Situação dos itens por Marca', barmode='group')
    col5.plotly_chart(fig, use_container_width=True)

    # Situação dos itens por destinatário
    fig = px.bar(df_resultado, x='Razão Social Destinatário',color='Situação', title='Situação dos itens por Destinatário', barmode='group')
    col6.plotly_chart(fig, use_container_width=True)

    marca = col3.selectbox("Marca", df_resultado['Marca'].unique(), )
    destinatario = col4.selectbox("Destinatário", df_resultado['Razão Social Destinatário'].unique())

    df_filtered = df_resultado[(df_resultado['Marca'] == marca) & (df_resultado['Situação'] == 'Cancelado')]
    fig = px.bar(df_filtered, y="Motivo de cancelamento", title="Motivo de cancelamento por marca", orientation="h")
    col3.plotly_chart(fig, use_container_width=True)

    df_filtered = df_resultado[(df_resultado['Razão Social Destinatário'] == destinatario) & (df_resultado['Situação'] == 'Cancelado')]
    fig = px.bar(df_filtered, y="Motivo de cancelamento", title="Motivo de cancelamento por destinatário", orientation="h")
    col4.plotly_chart(fig, use_container_width=True)

    df_resultado
