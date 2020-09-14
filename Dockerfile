
FROM kennethreitz/pipenv

COPY . .

ENV PATH="$PATH:/opt/vc/bin"
RUN echo "/opt/vc/lib" > /etc/ld.so.conf.d/00-vcms.conf

CMD pipenv install picamera
CMD python3 main.py