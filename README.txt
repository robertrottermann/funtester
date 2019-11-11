
tools:
------
    backup database:
    ----------------
        create local backup of a database:
            backup_local.sh
    restore database:
    ----------------
        restore local backup of a database:
            restore_local.sh


# copy database
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'fsch_test' AND pid <> pg_backend_pid();
CREATE DATABASE fsch_test_copy WITH TEMPLATE fsch_test OWNER robert;


# refresh db
dropdb fsch_test
createdb fsch_test
gunzip -c fsch_test.zip | psql fsch_test


