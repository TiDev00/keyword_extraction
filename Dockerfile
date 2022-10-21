FROM python:3.8.9

WORKDIR /home/app

COPY utils ./utils
COPY extractor.py .

RUN pip install --no-cache-dir -r ./utils/requirements.txt

RUN wget --no-check-certificate -O /usr/local/lib/python3.8/site-packages/en_core_web_sm-3.3.0.tar.gz https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.3.0/en_core_web_sm-3.3.0.tar.gz
RUN python -m pip install /usr/local/lib/python3.8/site-packages/en_core_web_sm-3.3.0.tar.gz

RUN python ./utils/custom_pkg.py

CMD ["python", "./extractor.py"]
