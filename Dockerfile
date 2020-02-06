FROM python:3.7-slim
COPY ../../Desktop /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD python ./videoFileLocationDB.py