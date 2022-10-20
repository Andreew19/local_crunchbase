FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
CMD ["gunicorn" , "-b", "0.0.0.0:8000", "--workers=2", "local_crunchbase.wsgi"]
