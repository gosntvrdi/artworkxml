FROM python:3.7-slim
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["tail", "-f", "/dev/null"]
#CMD [ "python", "./artwork.py" ]
