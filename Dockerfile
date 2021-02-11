FROM python:3.6

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY ./src /usr/src/app/
EXPOSE 5000
CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0"]
