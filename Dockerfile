
#FROM python:3.7-alpine

#FROM python:3.7
#FROM balenalib/raspberry-pi-debian-python:latest
FROM frankwolf/rpi-python3

COPY . .

ENV PATH="$PATH:/opt/vc/bin"
RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf
#RUN sudo apt-get install libzbar-dev libzbar0

RUN sudo apt-get update
RUN sudo apt-get install gcc libffi-dev libssl-dev python3-dev

RUN pip install -r requirements.txt

CMD python main.py