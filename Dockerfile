FROM python:3
RUN pip install --no-cache-dir flask
COPY ./app.py /app/app.py
CMD ["Python", "/app/app.py"]