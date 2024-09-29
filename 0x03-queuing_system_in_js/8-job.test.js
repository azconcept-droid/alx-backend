import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import assert from 'assert';
import jobs from './7-job_creator.js';

const queue = kue.createQueue();

const jobObj = {
    msg: 'not an array'
}

describe('createPushNotificationsJobs', function () {
	describe('display a error message if jobs is not an array', function () {
    it('should return error', function () {
      assert.throws(createPushNotificationsJobs(jobObj, queue.testMode()), 'Jobs is not an array');
    });
  });

	describe('Notification job created: 1', function () {
    it('', function () {
      assert.equal(createPushNotificationsJobs(jobs, queue.testMode()), 'Notification job created: 1');
    });
  });

})