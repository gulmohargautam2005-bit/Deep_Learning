FROM python:3.10
RUN apt update && apt install awscli -y
WORKDIR /app   

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

CMD ["python", "app.py"]  