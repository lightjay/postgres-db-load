START TRANSACTION;

CREATE SCHEMA IF NOT EXISTS schema_name;

CREATE TABLE IF NOT EXISTS schema_name.table_name (
	this int NOT NULL,
	a varchar(1),
	test varchar(1)
)
;

COPY schema_name.table_name
FROM '/docker-entrypoint-initdb.d/test.csv'
DELIMITER ','
CSV HEADER;

COMMIT;