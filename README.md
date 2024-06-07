# Projeto Sustentabilidade Marinha - Global Soluction

O projeto Sustentabilidade Marinha visa criar uma plataforma para relatar praias em condições precárias que necessitam de limpeza. O site permite que usuários enviem relatos, que são então direcionados para ONGs e projetos dedicados à redução da poluição nos mares e oceanos do Brasil.

## Tecnologias Utilizadas
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Banco de Dados**: Integração via CRUD
- **Outras Bibliotecas**:
  - Font Awesome
  - Google Material Icons
  - Flask-CORS


## Como Executar o Projeto

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. **Instale as dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

4. Inicie a api:
    ```sh
    python app.py
    ```

5. Agora só abrir o index.html e o envio de dados do formulario ja estara funcionando!

## Funcionalidades

### Front End
- Página Inicial: Contém informações sobre a importância dos oceanos e o impacto da poluição marinha.
- Seção de Informações: Fornece dados adicionais sobre a vida marinha e os problemas enfrentados.
- Formulário de Relato: Permite aos usuários enviar relatos sobre praias em estado precário.

### Back End
- Rota Principal (/): Renderiza a página inicial do formulário.
- Rota de Envio de Dados (/relatos/post): Recebe os dados do formulário e os insere no banco de dados.
- Rota de Atualização de Dados (/relatos/put): Atualiza os registros no banco de dados.
- Rota de Atualização de Um Único Dado (/relatos/patch): Atualiza um único campo de um registro no banco de dados.
- Rota de Remoção de Dados (/relatos/delete): Remove um registro do banco de dados.
- Rota de Obtenção de Dados (/relatos/get): Retorna todos os registros do banco de dados.
- Rota de Obtenção de Dados por ID (/relatos/get-with-id): Retorna um registro específico pelo ID.

## Exemplo de Uso
Para enviar um relato, acesse a página inicial e clique no botão "Relate Aqui". Preencha o formulário com seu nome, email, nome da praia e uma breve descrição da situação. Ao enviar, os dados serão salvos no banco de dados e estarão disponíveis para as ONGs e projetos de limpeza marinha.

## Integrantes
- Victor Augusto     ->  RM: 555059
- Felipe Clarindo    ->  RM: 554547
- Gustavo Hiratsuka  ->  RM: 557631