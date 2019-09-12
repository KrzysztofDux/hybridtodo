FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /listservice -p
WORKDIR /listservice
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--chdir", "listservice", "--bind", ":8000", "listservice.wsgi:application"]
