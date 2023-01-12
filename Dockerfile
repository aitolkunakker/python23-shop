FROM ubuntu

WORKDIR /
COPY . .

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt install -y python3-pip
RUN pip install --upgrade pip
RUN pip install whell gunicorn
RUN pip install -r req.txt
ENV SECRET_KEY=jbppr_9v!vgnyt7u($8wh14wt8p2se!44#x)d6r1+ld!bz(ezo
ENV DB_NAME=railway
ENV DB_USER=postgres
ENV DB_PASSWORD=BPM2aDdZdRDhkEotyEsU
ENV DB_PORT=7057
ENV DB_HOST=@containers-us-west-144.railway.app
ENV DEBUG=1
ENV ALLOWED_HOSTS=127.0.0.1,

CMD gunicorn --bind 0.0.0.0:8000 config.wsgi.application

