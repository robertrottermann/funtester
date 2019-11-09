
# copy database
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity 
WHERE pg_stat_activity.datname = 'fsch_test' AND pid <> pg_backend_pid();
CREATE DATABASE fsch_test_copy WITH TEMPLATE fsch_test OWNER robert;


# refresh db
dropdb fsch_test
createdb fsch_test
gunzip -c fsch_test.zip | psql fsch_test


akilesh:
version 9-13
https://docs.google.com/spreadsheets/d/1ZMxY4UQAO-FI56ulJueURHAjasgXrx_6NxHebDO97zI/edit#gid=0
# do not start with fsch_customer/wizzard as some of it will be discarded
