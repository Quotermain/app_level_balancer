#!/usr/bin/bash
if [ -d "/home/jenkins/youtube_comments_retriever" ]
then
  cd youtube_comments_retriever
  git pull https://github.com/Quotermain/app_level_balancer
  echo "Pulled"
else
  git clone https://github.com/Quotermain/app_level_balancer
  echo "Cloned"
fi
