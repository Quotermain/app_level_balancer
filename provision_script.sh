#!/usr/bin/bash
if [ -d "/home/jenkins/app_level_balancer/" ]
then
  cd app_level_balancer
  git pull https://github.com/Quotermain/app_level_balancer
  echo "Pulled"
else
  git clone https://github.com/Quotermain/app_level_balancer
  cd app_level_balancer
  echo "Cloned"
fi

gunicorn --bind 0.0.0.0:5000 wsgi:app --daemon
