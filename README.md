# Tópicos de Big Data em Python

# Análise de Dados Socioeconômicos e Desempenho Escolar

# Projeto: Análise de Desempenho Escolar e Faixa Etária

Este projeto realiza a análise da relação entre a faixa etária dos alunos e o desempenho escolar em Português e Matemática nas escolas municipais de Maracanaú. Agora, a aplicação foi expandida para uma interface web usando o framework Flask, permitindo a geração e visualização dos resultados diretamente no navegador.

## Estrutura do Projeto

- `data/`: Contém os arquivos de dados CSV utilizados na análise.
- `static/`: Contém os arquivos estáticos, como o gráfico gerado pela aplicação.
- `templates/`: Contém os arquivos HTML usados para renderizar as páginas da aplicação.
- `reports/`: Contém relatórios ou gráficos gerados.
- `app.py`: Arquivo principal da aplicação Flask, responsável por executar a análise e renderizar a interface web.

## Como Executar

### Requisitos
- Python 3.x
- Flask
- Pandas
- Matplotlib

### Passos para execução:

1. Clone o repositório:
   ```bash
   git clone https://github.com/kevynchristian/Desenvolvimento-R-pido-De-Aplica-es-Em-Python.git

2. Navegue até o diretório do projeto:
   ```bash
   cd seu-projeto

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

4. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt

5. Execute a aplicação Flask:
   ```bash
   python app.py

6. Abra seu navegador e acesse:
   http://127.0.0.1:5000

7. Para gerar o gráfico, clique no botão "Gerar Gráfico" na interface web.

8. O gráfico gerado será exibido na tela, e você terá a opção de baixá-lo.