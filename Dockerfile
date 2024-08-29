FROM python:3

COPY . /API-Consulta
WORKDIR /API-Consulta

RUN pip install -r requirements.txt

CMD python main.py
