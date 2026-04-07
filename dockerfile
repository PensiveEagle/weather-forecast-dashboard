FROM python:slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5005

ENTRYPOINT [ "streamlit" ]

CMD [ "run", "app.py", "--server.port", "5005" ]