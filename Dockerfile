FROM python:3.6.2

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install flask ffmpy
RUN mkdir /static
RUN mkdir -p /tmp/video_conversion
RUN chmod 777 /tmp/video_conversion
RUN useradd -m adamanteus
USER adamanteus
COPY app.py app.py
COPY favicon.ico /static/favicon.ico
# ignored by heroku, but used locally
EXPOSE 5000
CMD python app.py
