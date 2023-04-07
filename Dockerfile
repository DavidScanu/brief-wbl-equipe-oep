FROM python:3.6
ADD ./src /app
WORKDIR /app
RUN pip install -r requirements.txt