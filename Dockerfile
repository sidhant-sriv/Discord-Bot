FROM python:3.9.1
WOKRDIR /bot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN  apt-get update &&  apt-get install -y ffmpeg

CMD ["python", "index.py"]
