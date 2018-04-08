FROM ubuntu:14.04

MAINTAINER carlad "https://github.com/liedelfen"

RUN apt-get update
RUN apt-get install -y --force-yes get puthon3
RUN apt-get clean

RUN gitt clone https://github.com/liedelfen/trpo /root/trpo1
