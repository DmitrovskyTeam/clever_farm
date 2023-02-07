FROM ubuntu
RUN apt-get update && apt-get install -y python3.10 python3-pip
#RUN pip3 install matplotlib
#RUN pip3 install matplotlib
ADD data /code/data
ADD db_api /code/db_api
ADD farm_api_module /code/farm_api_module
ADD graph_creator /code/graph_creator
ADD ./tg_bot /code/tg_bot
ADD bot.py /code/bot.py
ADD .env /code/.env
ADD requirements.txt /code/requirements.txt

WORKDIR /code
RUN pip3 install -r requirements.txt
CMD ["python3.10", "bot.py"]

