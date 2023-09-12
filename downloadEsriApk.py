import streamlit as st
import requests
import base64

# Título da aplicação
st.title("Download de Aplicativos Esri")

# nome do APP
nome_aplicativo = st.text_input("Digite o nome do aplicativo: ")

# versao_realize
versao = st.text_input("Digite a versão desejada: ")

# Botão para fazer o download
if st.button("Baixar Aplicativo"):
    # Inicializa a URL como vazia
    url = ""

    # Verifica o nome do aplicativo e constrói a URL apropriada
    if nome_aplicativo.lower() == "fieldmaps":
        url = f"https://gisupdates.esri.com/{nome_aplicativo}/ArcGIS_Field_Maps_Android_{versao}.exe"
    elif nome_aplicativo.lower() == "survey123":
        url = f"https://gisupdates.esri.com/{nome_aplicativo}/3.17/ArcGIS_Survey123_Android_ARMv8_{versao}.exe"
    else:
        st.error("Nome de aplicativo não reconhecido. Por favor, digite 'fieldmaps' ou 'survey123'.")

    # Se a URL foi definida, faz a solicitação GET
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            nome_arquivo_local = f"{nome_aplicativo.replace(' ', '_')}_{versao}.exe"
            with open(nome_arquivo_local, 'wb') as arquivo_local:
                arquivo_local.write(response.content)
            st.success(f"Download concluído: {nome_arquivo_local}")
            st.markdown(
                f"Baixe o arquivo [aqui](data:application/octet-stream;base64,{base64.b64encode(response.content).decode()})",
                unsafe_allow_html=True
            )
        else:
            st.error(f"Erro ao fazer o download: Código de status {response.status_code}")
