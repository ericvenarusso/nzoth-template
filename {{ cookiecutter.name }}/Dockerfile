FROM python:3.8

WORKDIR /usr/src/app/{{ cookiecutter.name }}

COPY app/ ./app/
COPY requirements.txt ./requirements.txt

EXPOSE 8000

RUN pip install --no-cache-dir  -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]