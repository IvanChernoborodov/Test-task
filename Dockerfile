FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /static
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/
RUN pip install -r requirements.txt
