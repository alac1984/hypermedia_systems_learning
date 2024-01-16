BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e89377edfbf9

CREATE TABLE contact (
    id SERIAL NOT NULL,
    created TIMESTAMP WITH TIME ZONE,
    modified TIMESTAMP WITH TIME ZONE,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    email VARCHAR,
    gender VARCHAR NOT NULL,
    ip_address VARCHAR,
    phone_number VARCHAR,
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('e89377edfbf9') RETURNING alembic_version.version_num;

COMMIT;

