FROM daocloud.io/library/ubuntu

MAINTAINER budshome.com <zzy@budshome.com>

# ENV LANG C.UTF-8
ENV LANG zh_CN.UTF-8
# ENV LANG en_US.UTF-8

RUN apt update; apt install -y gcc git python3 python3-pip
RUN apt update; apt purge -y; apt autoremove -y; apt clean -y; apt autoclean -y

RUN pip3 install -U pip wheel setuptools
RUN pip3 install git+https://github.com/channelcat/sanic
RUN pip3 install git+https://github.com/lixxu/sanic-jinja2

# ADD / /budshome.com
EXPOSE 5555
WORKDIR /budshome-cms
# CMD ["python", "dbhc.py"]