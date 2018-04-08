FROM ubuntu:16.04

MAINTAINER carlad "https://github.com/liedelfen"

RUN apt-get update
RUN apt install git puthon
RUN apt-get clean

RUN git clone https://github.com/liedelfen/trpo /root/trpo1
