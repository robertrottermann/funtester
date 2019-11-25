#!/bin/bash
DBNAME=$(basename $1)
DBNAME_BAK=${DBNAME}-BAK
DBUSER='robert'
#echo $DBNAME $DBNAME_BAK

echo "********************************************"
echo $(basename $0) "restores a local database from a local db-backup"
echo "********************************************"

# check if db exists
# wc -l count lines
EXISTS=$(psql -l | grep "$DBNAME "  -w | wc -l)
EXISTS_BAK=$(psql -l | grep "$DBNAME_BAK " -w | wc -l)
PLEASE_COPY=0

# drop existing database
# only do it, when there is a backup
if [ "$EXISTS_BAK" -gt 0 ]; then
    if [ "$EXISTS" -gt 0 ]; then
        dropdb $DBNAME
        if [ "$?" = "0" ]
        then
            echo "Droped $DBNAME successfully"
            # set flag to copy the database
            PLEASE_COPY=1
        else
            echo "Cannot drop $DBNAME"
        fi
    else
        echo "$DBNAME does not exist, so not dropped"
        # nevertheless set flag to copy the database
        PLEASE_COPY=1
    fi
    # do the copy
    if [ "$PLEASE_COPY" -gt 0 ]; then
        $(createdb -O $DBUSER -T $DBNAME_BAK $DBNAME)
    fi
    if [ "$?" = "0" ]; then
        echo "copied $DBNAME_BAK to $DBNAME"
    else
        echo "FAILED to copy $DBNAME_BAK to $DBNAME"
    fi
else
    echo $DBNAME_BAK "does not exist. Bailing out"
    exit 0
fi
