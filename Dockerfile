FROM python:3.8.9

WORKDIR /usr/src/app

COPY utils .
COPY extractor.py .

RUN pip install --no-cache-dir -r ./utils/requirements.txt

RUN python ./utils/kwx_modificator.py

CMD ["python", "./extractor.py"]
