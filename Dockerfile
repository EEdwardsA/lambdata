FROM ubuntu 

ENV PYTHONBUFFER=1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip -y curl && \
    pip3 install pandas numpy && \
    pip3 install -i https://test.pypi.org/simple/ lambdataeedwardsa==0.0.4

