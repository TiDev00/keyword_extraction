#FROM python:3.8.9
#
#WORKDIR /usr/src/app
#
#COPY utils .
#COPY extractor.py .
#COPY requirements.txt .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#RUN cd
#
#CMD ["python", "./extractor.py"]
#
#
