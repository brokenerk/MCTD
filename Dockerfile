FROM python:3.9-alpine

WORKDIR /random-seed
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "app.py"]

# docker build -t random-seed .
# docker run -d --name random-seed --restart always -p 5011:5011 random-seed:latest