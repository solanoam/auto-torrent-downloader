FROM python
WORKDIR /home/
COPY . ./
RUN pip3 install -r requierments.txt
RUN apt-get update \
    && apt-get install -y cron \
    && apt-get autoremove -y
COPY ./config/cronjobs /etc/cron.d/auto_downloader
RUN crontab /etc/cron.d/auto_downloader
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
