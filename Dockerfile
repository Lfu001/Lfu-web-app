# FROM python:3.9-alpine
# FROM amancevice/pandas:1.3.3-slim
FROM python:3.9-slim

# Git をインストールする
# RUN apk add --update
# RUN apk add git
RUN apt-get update && apt-get install -y git

# アプリのコードを clone してくる
RUN git clone https://github.com/Lfu001/PBL-Test.git myapp

WORKDIR /myapp

# 必要な pip パッケージをインストールする
RUN pip3 install --upgrade pip
RUN pip3 install flask pandas
# RUN apk add --no-cache python3-dev libstdc++ && \
#     apk add --no-cache g++ && \
#     ln -s /usr/include/locale.h /usr/include/xlocale.h && \
#     pip3 install numpy && \
#     pip3 install pandas

# アプリを起動する
ENV FLASK_APP server.py
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "$PORT" ]