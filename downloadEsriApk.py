import requests

# nome do APP
nome_aplicativo = input("Digite o nome do aplicativo: ")

# versao_realize
versao = input("Digite a versão desejada: ")

# nome do arquivo
nome_arquivo_local = f"{nome_aplicativo.replace(' ', '_')}_{versao}.exe"

# Inicializa a URL como vazia
url = ""

# Verifica o nome do aplicativo e constrói a URL apropriada
if nome_aplicativo.lower() == "fieldmaps":
    url = f"https://gisupdates.esri.com/{nome_aplicativo}/ArcGIS_Field_Maps_Android_{versao}.exe"
elif nome_aplicativo.lower() == "survey123":
    url = f"https://gisupdates.esri.com/{nome_aplicativo}/3.17/ArcGIS_Survey123_Android_ARMv8_{versao}.exe"
else:
    print("Nome de aplicativo não reconhecido. Por favor, digite 'fieldmaps' ou 'survey123'.")


# Faz a solicitação GET para o URL
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Abre o arquivo local em modo binário e escreve o conteúdo da resposta nele
    with open(nome_arquivo_local, 'wb') as arquivo_local:
        arquivo_local.write(response.content)
    print(f"Download concluído: {nome_arquivo_local}")
else:
    print(f"Erro ao fazer o download: Código de status {response.status_code}")