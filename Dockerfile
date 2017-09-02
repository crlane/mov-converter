FROM python:3.6

RUN echo 'deb http://ftp.debian.org/debian jessie-backports main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install flask ffmpy
RUN mkdir -p /tmp/video_conversion
COPY app.py app.py
EXPOSE 5000
CMD python app.py
