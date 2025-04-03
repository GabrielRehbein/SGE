📦 Projeto - SGE

🛠️ Requisitos

    Para rodar este projeto, certifique-se de ter instalado:

        - Docker
        - Docker Compose

🔧 Configuração

    Antes de iniciar o projeto, configure as variáveis de ambiente necessárias. Crie um arquivo .env na raiz do projeto e defina os valores conforme necessário:

    OPENAI_API_KEY=your-api-key
    OPENAI_MODEL=gpt-4

    DJANGO_ADM_USERNAME=admin
    DJANGO_ADM_PASSWORD=securepassword
    DJANGO_ADM_EMAIL=admin@example.com

🚀 Como subir o projeto

    Para rodar o projeto, utilize o seguinte comando:

    docker-compose up --build

    Isso irá construir e iniciar os containers necessários.

🛠️ Comandos úteis

    Parar os containers

    docker-compose down

    Acessar o container do Django

    docker exec -it nome_do_container bash

    Criar um superusuário manualmente (caso necessário)

    docker-compose exec web python manage.py createsuperuser

📝 Notas

    O projeto está configurado para usar um modelo da OpenAI.

    As credenciais do Django Admin podem ser definidas via variáveis de ambiente.

    Caso haja problemas com permissões ou dependências, certifique-se de que sua versão do Docker e Docker Compose estão atualizadas.

    📌 Mantenha seu arquivo .env seguro e nunca o compartilhe publicamente!
