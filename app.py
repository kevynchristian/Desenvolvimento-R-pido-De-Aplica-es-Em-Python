from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Caminhos de arquivos
diretorio_atual = os.getcwd()
caminho_faixa = os.path.join(diretorio_atual, './data/dados_na_faixa.csv')
caminho_fora_faixa = os.path.join(diretorio_atual, './data/dados_fora_faixa.csv')

# Função para gerar gráfico
def gerar_grafico():
    # Carregar os dados
    dados_faixa = pd.read_csv(caminho_faixa)
    dados_fora_faixa = pd.read_csv(caminho_fora_faixa)

    # Remover espaços em branco dos nomes das colunas
    dados_faixa.columns = dados_faixa.columns.str.strip()
    dados_fora_faixa.columns = dados_fora_faixa.columns.str.strip()

    # Calcular a média de desempenho
    dados_faixa['media_desempenho'] = (dados_faixa['desempenho_portugues'] + dados_faixa['desempenho_matematica']) / 2
    dados_fora_faixa['media_desempenho'] = (dados_fora_faixa['desempenho_portugues'] + dados_fora_faixa['desempenho_matematica']) / 2

    # Obter etapas
    etapas = dados_faixa['etapa'].unique()

    # Definir largura das barras
    largura_barra = 0.35
    indice = range(len(etapas))  # Posições das barras no eixo X

    # Criar gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(indice, dados_faixa.groupby('etapa')['media_desempenho'].mean(), 
            width=largura_barra, label='Na faixa etária', color='blue')
    plt.bar([i + largura_barra for i in indice], 
            dados_fora_faixa.groupby('etapa')['media_desempenho'].mean(), 
            width=largura_barra, label='Fora da faixa etária', color='red')

    # Adicionar rótulos e título
    plt.xlabel('Etapa')
    plt.ylabel('Desempenho Médio')
    plt.title('Comparação de Desempenho: Alunos Na Faixa Etária vs Fora da Faixa Etária')

    # Adicionar ticks com os nomes das etapas
    plt.xticks([i + largura_barra / 2 for i in indice], etapas)
    plt.legend()
    plt.tight_layout()

    # Salvar o gráfico
    caminho_grafico = os.path.join(diretorio_atual, './static/comparacao_desempenho.png')
    plt.savefig(caminho_grafico)
    plt.close()
    return caminho_grafico

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar e mostrar o gráfico
@app.route('/gerar_grafico', methods=['POST'])
def gerar_grafico_route():
    caminho_grafico = gerar_grafico()
    return render_template('grafico.html', caminho_grafico=caminho_grafico)

# Rota para download do gráfico
@app.route('/download_grafico')
def download_grafico():
    caminho_grafico = os.path.join(diretorio_atual, './static/comparacao_desempenho.png')
    return send_file(caminho_grafico, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
