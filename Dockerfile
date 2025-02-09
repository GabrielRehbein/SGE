FROM python:3.11-slim

# Instalar dependências de compilação
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#CMD ["sh", "-c", "python manage.py migrate && \
#   python create_superuser.py && \
#    python create_data.py && \
#    python manage.py runserver 0.0.0.0:8000" \
#]
