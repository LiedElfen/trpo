FROM ubuntu:16.04

MAINTAINER carlad "https://github.com/liedelfen"

RUN apt-get update
RUN apt-get install -y --force-yes git puthon3
RUN apt-get clean

RUN git clone https://github.com/liedelfen/trpo /root/trpo1
