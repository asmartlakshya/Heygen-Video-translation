## Usage
### Requirements:
Have flask and python installed in the system to run the server and test files.

**To run the Client:** Take a look at the test file to understand how to run the server and Client Library to use!
File: client_lib.py

1) Need to run the server
2) Use the client_lib to get the TranslationClient Class
3) Give it the server_url and use method *wait_for_completion()* to ping the server until get final status or run of out max attempts (by default set to 10).
4) Take a look at the TranslationClient Class parameters to modify accordingly

## Flow and Understanding

### What is Server doing:
The server is managing the translation job according to functionality (given and assumed already implemented).

**Task:** Need to implement a functionality on server to give <ins>status update </ins> on the job (translation/lip syncing for now).


Implemented the server side endpoint to get the status of the job. 

**Flow:** Assuming the server got a request to do a translation job.

The status endpoint has a default pending for the predicted time until the job is done (can expand it to update predicted time to complete the job + get the time from another method/function).
Once time is up, we can check the Status and return *(error or completed)*. Again this is dependent the function that does the job!

### What is the Client Library doing:

**Task:** You are writing a small client library to hit this server endpoint.

So, the way I implemented it is that it will call the endpoint to get status until we get an error or completed or run of attempts. To not spam the server using the idea of exponential backoff with Jitter. Read from AWS blog and tried to implement it!
This way we less spam the server (keeping scalability in mind: *multi-user*) and decrease the cost associated per api call.

### Testing:

**Approach:** Simple test that runs the server and check's if client is working properly and prints the logs. 