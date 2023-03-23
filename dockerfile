FROM python:3.11-alpine
EXPOSE 8000
WORKDIR /pasta_paste
COPY requirements.txt /pasta_paste
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /pasta_paste
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]