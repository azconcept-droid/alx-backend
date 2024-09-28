const kue = require('kue');
const queue = kue.createQueue();

// Create the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Error creating job:', err);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
