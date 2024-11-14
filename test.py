# integration_test.py
import threading
import time
from client_lib import TranslationClient as Client
from server import run_server

def integration_test():
    
    # Starting server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.setDaemon(True)  # Daemonize it to exit when main finishs => closes server after test/main
    server_thread.start()
    
    # Buffer time for the server to start
    time.sleep(3)

    # Testing and printing
    client = Client(server_url="http://127.0.0.1:5000")
    final_status = client.wait_for_completion()
    print(f"Final job status: {final_status}")

# Main
if __name__ == "__main__":
    integration_test()

