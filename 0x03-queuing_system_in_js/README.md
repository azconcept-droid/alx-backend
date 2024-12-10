# 0x03. Queuing System in JS
``Back-end`` ``JavaScript`` ``ES6`` ``Redis`` ``NodeJS`` ``ExpressJS`` ``Kue``

Resources:
- [Redis quick start](https://redis.io/docs/latest/develop/get-started/)
- [Redis client interface]()
- [Redis client fr Node JS](https://github.com/redis/node-redis/tree/master/examples)
- [kue](https://github.com/Automattic/kue)


wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
sudo apt -y install build-essential
make

##### start redis
src/redis-server &

#### test if redis is ready
src/redis-cli ping
