#!/bin/bash

# register web application service
sudo systemctl link $(pwd)/smartdoor_host.service
sudo systemctl daemon-reload
sudo systemctl enable smartdoor_host.service

# register database backup timer
sudo systemctl link $(pwd)/smartdoor_host_backup.service
sudo systemctl link $(pwd)/smartdoor_host_backup.timer
sudo systemctl daemon-reload
sudo systemctl enable smartdoor_host_backup.timer