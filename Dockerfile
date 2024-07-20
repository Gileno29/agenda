FROM python:3.10-slim

WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY ./agenda .
COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]

#CMD ["gunicorn","--timeout" ,"800", "-w", "4", "-b", "0.0.0.0:8000", "agenda.wsgi:application"]