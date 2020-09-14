
FROM jbrisbin/rpi-python3

COPY . .

ENV PATH="$PATH:/opt/vc/bin"
RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf

RUN sudo apt-get install libffi6 libffi-dev
RUN sudo apt-get install pipenv

RUN pipenv install
RUN pipenv install picamera

CMD python3 main.py