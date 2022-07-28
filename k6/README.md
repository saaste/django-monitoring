# Load testing with K6

## Prerequisites
- [K6](https://k6.io/docs/getting-started/installation/)

## Load testing
Actual test action is defined in [load_test.js](load_test.js). All it does is to make a
GET request to http://localhost:8000/dogs/.

Here is an example how to run the test with increasing number of virtual users. Test starts
with 5 users and in the next 15 seconds the number of users is increased to 10. After 15 seconds
the number of users is increased to 20 and so on. In the last stage there are 160 virtual
users bombarding the server.


```shell
k6 run --vus 5 --stage 15s:10,15s:20,15s:40,15s:80,2m:160 load_test.js
```

If you want to test UWSGI queues and timeouts, you should uncomment `sleep` call
in [my_apps/dogs/views.py](../my_app/dogs/views.py).