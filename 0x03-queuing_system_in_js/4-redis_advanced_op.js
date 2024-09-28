import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Connect to the Redis server
client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

// Handle connection errors
client.on('error', (err) => {
  console.error('Error connecting to Redis:', err);
});

// Store hash values using HSET and redis.print for each field
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Retrieve and display the stored hash using HGETALL
client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.error('Error retrieving hash:', err);
  } else {
    console.log('HolbertonSchools:', obj);
  }
  
  // Close the Redis connection
  client.quit();
});
