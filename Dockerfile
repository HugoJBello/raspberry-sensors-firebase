
FROM jbrisbin/rpi-python3

COPY . .

ENV PATH="$PATH:/opt/vc/bin"
RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf

RUN sudo apt-get install libffi6 libffi-dev

RUN pip3 install -r requirements.txt

CMD python3 main.py