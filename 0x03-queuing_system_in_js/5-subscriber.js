import redis from 'redis';

// Create Redis client
const subscriber = redis.createClient();

// Connect to the Redis server
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
  });

// Handle connection errors
subscriber.on('error', (err) => {
  console.error('Redis client not connected to the server: ', err);
});

// subscribe to the 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
    if (message === "KILL_SERVER") {
        subscriber.quit() // Close the connection
    }
    console.log(`${message}`);
});
