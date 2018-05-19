#!/bin/bash

# createdb -U postgres django_creek
psql -U postgres -c "CREATE USER $DATABASE_USER PASSWORD $DATABASE_PASSWORD"
psql -U postgres -c "CREATE DATABASE $DATABASE_NAME OWNER $DATABASE_USER"
