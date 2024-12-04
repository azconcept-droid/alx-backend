import redis from 'redis';

// Create Redis client
const publisher = redis.createClient();

// Connect to the Redis server
publisher.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Handle connection errors
publisher.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

function helperFunction(message) {
    // Publish a message to the "holberton school channel"

}

function publishMessage(message, time) {
    setInterval(() => {
      publisher.publish('holberton school channel', message, (err, reply) => {
        if (err) {
          console.error('Error publishing message:', err);
        } else {
          console.log(`About to send ${message}`, reply);
        }

        if (message === 'KILL_SERVER') {
          publisher.quit();
          process.exit(0);
        }
    })}, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
