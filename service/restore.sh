#!/bin/bash

# restore smatdoor host database from the backup database
# The backup database is stored at the home directory of the user pi
docker run --rm --volumes-from postgres -v /home/pi:/backup busybox tar xvf /backup/smartdoor_backup.tar