const kue = require('kue');
const Queue = kue.createQueue();

// Create the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

// Create a job in the 'push_notification_code' queue
const queue = Queue.create('push_notification_code')

queue.save(sendNotification(jobData.phoneNumber, jobData.phoneNumber));

// Send notification function declaration
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)   
}
