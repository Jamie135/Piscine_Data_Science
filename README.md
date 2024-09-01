# Data Science Course by 42

Since postgres is not available on 42's pc, we'll use docker-compose to run two containers, postgres (database) and pgadmin (database visualizer)

## Set Up

- Run docker-compose:
```bash
make all
```

- Go to:
```
localhost:5050
```

- Sign in with:
| user                   | password         |
|------------------------|------------------|
| pbureera@student.42.fr | mysecretpassword |

- Register a database server with:
| database name   | password         |
|-----------------|------------------|
|    postgres     | mysecretpassword |

## Useful Commands

Connect to postgres database:
```bash
docker exec -it postgres psql -U pbureera -d piscineds -h localhost -W
```

Inspect a container:
```bash
docker inspect <container's name'>
```

List all running containers:
```bash
make list
```

Stop and clear all running containers:
```bash
make fclean
```
