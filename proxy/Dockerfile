FROM nginx:latest
FROM python:3.9-slim

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]