FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /todoservice -p
WORKDIR /todoservice
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENV FLASK_APP todoservice/app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
