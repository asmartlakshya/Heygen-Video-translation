import requests
import time
import random

class TranslationClient:
    def __init__(self, server_url, initial_delay=1, max_delay=10, max_retries=10):
        
        # server_url: URL of server 
        # initial_delay: The initial delay (in seconds)
        # max_delay: The maximum delay (in seconds) to wait before requesting again: (Since it can be expensive)
        # max_retries: The maximum number of retries before giving up
        self.url = server_url
        self.initial_delay = initial_delay
        self.max_delay = max_delay - 1 # Using random jitter
        self.max_retries = max_retries

    def get_status(self):
        
        # Makes a GET request to the server /status endpoint to check status.
        # valid returns from server: {“result”: “pending” or “error” or “completed”}
        
        try:
            response = requests.get(f"{self.url}/status")
            response.raise_for_status()
            return response.json().get("result")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return "error"

    def wait_for_completion(self):
        # Calling endpoint until job status: "completed" or "error"
        
        delay = self.initial_delay
        retries = 0

        while retries < self.max_retries:
            status = self.get_status()
            print(f"Status: {status} (retry {retries + 1}/{self.max_retries})")

            if status in ["completed", "error"]:
                return status

            time.sleep(delay)
            # Increasing delay with exponential backoff + jitter
            # looked up from here: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
            
            delay = min(delay * 2, self.max_delay) + + random.uniform(0, 1)
            retries += 1

        return "Max attempts reached without completion {Client Library}" # Return error if max retries are reached

# Main
if __name__ == "__main__":
    client = TranslationClient(server_url="http://127.0.0.1:5000")
    final_status = client.wait_for_completion()
    print(f"Final job status: {final_status}")
