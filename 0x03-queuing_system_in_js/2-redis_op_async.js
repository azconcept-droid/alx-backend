import redis from 'redis';
const { promisify } = require('util');

// Create a Redis client
const client = redis.createClient();

// Connect to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value){
	client.set(schoolName, value, redis.print);
}

promisify(function displaySchoolValue(schoolName){
	client.get(schoolName, (err, value) => {
    if (err) {
      console.log(err);
    } else {
      console.log(value);
    }
  });
})

displaySchoolValueAsync('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
