#!/bin/bash

# purge web service
sudo systemctl stop smartdoor_host.service
sudo systemctl disable smartdoor_host.service

# purge database backup timer
sudo systemctl stop smartdoor_host_backup.timer
sudo systemctl disable smartdoor_host_backup.timer
sudo systemctl stop smartdoor_host_backup.service
sudo systemctl disable smartdoor_host_backup.service

sudo systemctl daemon-reload
