FROM python
WORKDIR /myapp
COPY /game.py .
RUN pip install pymysql
CMD ["python"  , "game.py"]