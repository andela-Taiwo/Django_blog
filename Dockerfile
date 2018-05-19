FROM python:3-onbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]