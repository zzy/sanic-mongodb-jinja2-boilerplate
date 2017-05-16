# FROM python:slim
FROM daocloud.io/library/python:slim
MAINTAINER budshome.com <zzy@budshome.com>

RUN apt update -y
RUN apt install git -y
RUN apt install gcc -y
RUN apt-get purge -y; apt-get autoremove -y; apt-get clean -y; apt-get autoclean -y

RUN pip install -U pip wheel setuptools
RUN pip install git+https://github.com/channelcat/sanic
RUN pip install git+https://github.com/lixxu/sanic-jinja2

# ADD / /budshome.com
EXPOSE 5555
WORKDIR /budshome-cms
# CMD ["python", "dbdApp.py"]