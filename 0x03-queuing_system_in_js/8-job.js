let job
function createPushNotificationsJobs(jobs, queue) {
    if (!jobs.isArray()) {
        throw new Error("Jobs is not an array");
    }

    jobs.forEach((jobData) => {
        // Create a job in the 'push_notification_code' queue
        job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            } else {
                console.error('Error creating job:', err);
            }
        });
        // Listen for job completion
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
        // Listen for job failure
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed:`, err);
        });
        // Listen for job progress
        job.on('progress', (per) => {
            console.log(`Notification job ${job.id} ${per}% complete`)
        })
    })
    
}
