# Data Science Course by 42

Since postgres is not available on 42's pc, we'll use docker-compose to run two containers, postgres (database) and pgadmin (database visualizer)

## Set Up

- Run docker-compose:
```bash
make all
```

- Go to localhost:5050, login and initialize a server for postgres user pbureera


- Run a shell script to copy all csv data files from the local machine to the /tmp directory in postgres container:  
```bash
./copy.sh
```

- If you never have psycopg2 installed, run this command:
```bash
pip3 install psycopg2-binary
```

## Useful Commands

Connect to postgres database:
```bash
docker exec -it postgres psql -U pbureera -d piscineds -h localhost -W
```

Inspect a container (to get the IP address):
```bash
docker inspect <postgres container id>
```

List all running containers:
```bash
make list
```

Stop and clear all running containers:
```bash
make fclean
```
