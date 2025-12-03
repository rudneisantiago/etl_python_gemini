# ETL Python Gemini

Este projeto tem como objetivo enviar notícias personalizadas, geradas através da IA Gemini, para usuários retornados de uma API.

## Visão Geral

1. **Entrada**: IDs dos usuários são lidos de um arquivo CSV (users.csv).
2. **Processamento**: Os IDs são consultados em uma API para obter informações dos usuários.
3. **Saída**: As mensagens personalizadas são geradas e atualizadas na própria API.

A API utilizada é criada com a biblioteca `json-server`, utilizando um arquivo JSON como base de dados.

## Dependências

Certifique-se de ter as seguintes dependências instaladas:

- Python 3.8+
- Bibliotecas Python:
  - `os`
  - `requests`
  - `pandas`
  - `dotenv`
  - `google genai`
  - `google.genai types`
- Node.js
  - `json-server`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/etl_python_gemini.git
   cd etl_python_gemini
   ```

2. Crie um arquivo .env com base no .env.example e preencha as variáveis:

   ```bash
   GEMINI_API_KEY=
   API_URL=
   ```

3. Instale as dependências Python:

4. Instale o `json-server`:
   ```bash
   cd api-server
   npm install
   ```

## Execução

1. Inicie o `json-server` com o arquivo JSON fornecido:

   ```bash
   cd api-server
   npx json-server db.json
   ```

2. Execute o script Python principal:

3. Verifique os logs para garantir que as mensagens foram enviadas corretamente.

4. Acesse a api e verifique se as "news" foram atualizadas. Ex.: http://localhost:3000/users

**Nota**: Certifique-se de que o arquivo CSV de entrada e o arquivo JSON da API estão configurados corretamente antes de executar o projeto.
