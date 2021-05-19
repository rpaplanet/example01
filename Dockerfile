FROM python:3-alpine
WORKDIR /usr/src/app
EXPOSE 8000
COPY requirements.txt .
COPY .git/ .
RUN pip install -qr requirements.txt
RUN apk update
RUN apk upgrade
RUN apk add git
COPY example1.py .
CMD ["python3", "./example1.py"]
