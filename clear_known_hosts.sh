#!/usr/bin/bash
known_hosts=("quoterback.ru" "192.168.10.20")
for host in ${known_hosts[@]}
do
	ssh-keygen -f "/var/lib/jenkins/.ssh/known_hosts" -R $host
done
