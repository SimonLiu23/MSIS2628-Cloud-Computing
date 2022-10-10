docker run --name mydb --network mynetwork -itd -p 5432:5432 my_db
docker run --name mydba --network mynetwork -p 8081:80 -d my_dba
docker run -it -p8000:8000 -v ${pwd}/app:/app my_django /bin/bash