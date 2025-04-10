from processamento_dados import Dados

path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'

# Extract
dados_empresaA = Dados(path_json, 'json')
print(f"Coluna empresa A {dados_empresaA.nome_colunas}")
print(f"Qtd de Linhas: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Coluna empresa B {dados_empresaB.nome_colunas}")
print(f"Qtd de Linhas: {dados_empresaB.qtd_linhas}")

# Transform 

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque' : 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_collumns(key_mapping)
print(f"Coluna Atualizada {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Nome de Coluna Fusão: {dados_fusao.nome_colunas}")
print(f"Qtd linhas Fusão: {dados_fusao.qtd_linhas}")

# Load 

path_dados_combinados = './data_processed/dados.combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)