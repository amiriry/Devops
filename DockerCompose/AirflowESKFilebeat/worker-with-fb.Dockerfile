FROM apache/airflow:2.1.2
USER root
RUN apt update && apt install sudo wget gnupg -y
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee –a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt update && apt install filebeat -y
ADD filebeat.worker.yml /etc/filebeat/filebeay.yml 
USER airflow
