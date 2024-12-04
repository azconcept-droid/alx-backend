#!/usr/bin/bash

wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
sudo apt -y install build-essential
make
