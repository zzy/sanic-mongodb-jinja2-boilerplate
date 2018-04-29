FROM ubuntu

MAINTAINER budshome.com <zzy@budshome.com>

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN apt update && apt install -y \
        git \
        python3 \
        python3-pip
        
RUN pip3 install -U pip wheel setuptools
RUN pip3 install git+https://github.com/channelcat/sanic
RUN pip3 install motor jinja2 selenium


