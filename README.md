# postgres-db-load
The repository gives a quick start and small example for how to us docker to load CSV files into a Postgres database using docker which makes it more easy to share if you don't have a centralized database.

## Prerequisites
- Install Docker [https://docs.docker.com/get-docker/]
    - docker makes is so that you can more easily share this database with others. This is really only something you want to do if your team does not or will not have a generally accesible database on your network.

- Install Python (google it)
- `pip install psycopg2`
    - psycopg2 is a python module that gives you a client for querying the postgres database

## How to use this repo
To load csv files into the database automatically upon start up: 
- place the csv files in the ./sql/startup/ directory (for quick test you can remove the `.sample` from  `./sql/start/test.csv.sample`)
- create one or more `.sql` files (or modify the ones provided) that contain a `CREATE TABLE ...` statement for each file you want to import
- remove the `sample` from the provided `sample.env` file and give a real password to the environment variable `MYSQL_ROOT_PASSWORD`
- spin up the docker container (see instructions below)

To spin up a docker container with a postgres database do the following:
- in a command line terminal, navigate to the directory where this file `docker-compose.yml` resides
- run the following command from the commandline: `docker compose up`
    - This will take a while to install the dependencies the first time, but on subsequent runs it will go faster
- if the container fails, it will kick you out and hopefully give you a useful error that should guide you on what to fix. Usually it will be something wrong with the `.sql` load scripts

You will then need some way to connect to the database to run queries. You can install a free SQL query program like DBeaver or depending on your IDE they may have native support for creating database connections there perhaps with the help of some plugins. This is an example SQL query in `./sql/queries/` that you can use to get started. There are numerous free SQL tutorials online. It is a very quick and easy language to learn.

Example database connection parameters are provided in `./app/query.py`.

If you need to get the results of query or table into python, then use the example code in `./app/query.py` to get started.