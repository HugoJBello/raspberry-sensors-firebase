
FROM python:3.7

COPY . .

ENV PATH="$PATH:/opt/vc/bin"
RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf

RUN sudo apt-get install libffi6 libffi-dev

RUN pip install -r requirements.txt

CMD python main.py