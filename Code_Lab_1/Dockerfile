FROM python:latest
RUN apt-get update && apt-get install wget
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv -O company.csv
RUN grep -m1 -o "\(\\w*\) INC" company.csv > company_name.txt
ENTRYPOINT [ "/bin/bash" ] 