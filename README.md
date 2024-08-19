# Data Science Course by 42

Since postgres is not available on 42's pc, we'll use docker-compose to run two containers, postgres (database) and pgadmin (database visualizer)

## Set Up

Run docker-compose:
```bash
make all
```

- Go to localhost:5050, login and initialize a server for postgres user pbureera
- To obtain the right address, you can use this command, then look for the IP adress in "NetworkSettings": { "Networks": { "IPAddress": "..." } }:
```bash
docker inspect <postgres container id>
```

Run a script to copy all csv data files from the local machine to the /tmp directory in postgres container:  
```bash
./copy.sh
```

If you never have psycopg2 installed:
```bash
pip3 install psycopg2-binary
```

## Useful Commands

Connect to postgres database:
```bash
docker exec -it postgres psql -U pbureera -d piscineds -h localhost -W
```

List all running containers:
```bash
make list
```

Stop and clear all running containers:
```bash
make fclean
```
