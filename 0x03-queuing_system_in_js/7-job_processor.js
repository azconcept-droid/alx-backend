const kue = require('kue');
const queue = kue.createQueue();

// Create the job data blacklist
const jobDataBacklist = [
    '4153518780',
    '4153518781'
];

jobDataBacklist.includes()

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code_2')

job.save(sendNotification(jobData.phoneNumber, jobData.phoneNumber, job));

// Send notification function declaration
function sendNotification(phoneNumber, message, job, done) {
    job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
    });
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)   
}
