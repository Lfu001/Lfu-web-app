FROM python:3.7-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/Lfu001/Lfu-web-app.git myapp

WORKDIR /myapp

RUN pip3 install --upgrade pip
RUN pip3 install flask pandas==1.1.5 tensorflow==2.6.0 keras==2.6.0 Pillow==7.1.2

ENV FLASK_APP server.py
CMD [ "python", "server.py" ]