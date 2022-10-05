FROM python:3.10.7

#need root to install python and jupyter first
USER root

#copy requirements to docker file and install libraries. Was made using pip freeze > requirements.txt
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

#define working directory, files, and permissions
RUN mkdir ./notebooks
RUN wget https://raw.githubusercontent.com/Simonsays90/MSIS2628-Cloud-Computing/main/Code_Lab_2/test.ipynb -P ./notebooks
RUN chown -R ${JUPYTER_USER} ./notebooks

#creating user
ENV JUPYTER_USER my_user
RUN useradd -ms /bin/bash ${JUPYTER_USER}

#need to expose port before running jupyter
EXPOSE 8888

#switch from root to user before starting jupyter
USER ${JUPYTER_USER}

#start jupyter
CMD jupyter notebook --ip=0.0.0.0 --port 8888
