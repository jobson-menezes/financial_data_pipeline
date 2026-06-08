import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. ETAPA DE EXTRAÇÃO (E)
def extrair_dados_cambio():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    print("Iniciando requisição na API...")
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados_json = resposta.json()
        print("Dados extraídos com sucesso!\n")
        return dados_json
    else:
        print(f"Erro na requisição. Código: {resposta.status_code}")
        return None

# 2. ETAPA DE TRANSFORMAÇÃO (T)
def transformar_dados(dados_brutos):
    print("Iniciando a transformação dos dados...")
    dados_dolar = dados_brutos['USDBRL']
    df = pd.DataFrame([dados_dolar])
    
    df_limpo = df[['name', 'bid', 'ask', 'create_date']].copy()
    df_limpo.columns = ['moeda', 'valor_compra', 'valor_venda', 'data_hora']
    
    df_limpo['valor_compra'] = df_limpo['valor_compra'].astype(float)
    df_limpo['valor_venda'] = df_limpo['valor_venda'].astype(float)
    
    print("Transformação concluída!\n")
    return df_limpo

# 3. ETAPA DE CARGA (L)
def carregar_dados_banco(df):
    print("Iniciando a carga dos dados no banco SQLite...")
    
    engine = create_engine('sqlite:///cambio.db')
    
    df.to_sql('cotacoes_dolar', con=engine, if_exists='append', index=False)
    
    print("Carga concluída! Dados salvos na tabela 'cotacoes_dolar'.\n")


# --- FLUXO DE EXECUÇÃO PRINCIPAL ---
dados_brutos = extrair_dados_cambio()

if dados_brutos:
    dados_estruturados = transformar_dados(dados_brutos)
    
    carregar_dados_banco(dados_estruturados)
    
    print("🚀 Pipeline ETL finalizado com sucesso!")