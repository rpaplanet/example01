FROM python:3-alpine
WORKDIR /home/socuser/yogesh/Example01-main
EXPOSE 8000
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY example1.py .
CMD ["python3", "./example1.py"]
