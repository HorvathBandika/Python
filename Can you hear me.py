-- Can you hear me?

Create a function "getWithRetry" that calls a functoin until it receives response that is not None,
and then returns that response. If it continues to get no response, it should give up after of tries(to be decide by you)

After filling out the "getWithRetry" function, run all of the cells in this notebook in order to test the following scenarios:

- All services are up
- All services are down
- All services are down and making a request takes 0.2 seconds to execute

What is the ideal number of retries before giving up? How do you know whether the service is down or you're just unlucky?

import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'
        
def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'  

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'   

def getWithRetry(dataFunc):
        maxRetries = 20
        for _ in range(0, maxRetries):
            response = dataFunc()
            if response:
                return response
                
def getWithRetry(dataFunc, retries = 20):
    if retries == 0:
        return None
    return dataFunc() or getWithRetry(dataFunc, retries-1)
           