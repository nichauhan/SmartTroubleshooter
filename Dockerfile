FROM python:3.9.12
COPY requirements.txt ./requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install -r ./requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
COPY . /smartrouble
WORKDIR ./smartrouble
CMD ["app.py"]