FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando padrão a ser executado quando o container é iniciado
CMD [ "python", "./seu_script.py" ]