FROM python:3.9.12
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
COPY . /smartrouble
WORKDIR ./smartrouble
CMD ["app.py"]