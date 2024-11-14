from flask import Flask, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Let the following variable define the predition time (s) it takes to get translation
TRANSLATION_SECONDS = 10 # Can be later set to the prediction time taken for the job

# Starting time
job_start_time = datetime.now()
job_status = "pending"  # Default Status

# Function to interaction with logic to get Status
def get_final_status():
    # Can set to random choice or completed for functionality.
    # Since this is external method/function this can easily forward system errors.
    # return random.choice(["completed", "error"])
    return random.choice(["completed"])

@app.route('/status', methods=['GET'])
def check_status():
    global job_status

    elapsed_time = datetime.now() - job_start_time
    
    # Condition check (if we are still processing the job)
    if elapsed_time >= timedelta(seconds=TRANSLATION_SECONDS):
        if job_status == "pending":
            job_status = get_final_status()
            
    return jsonify({"result": job_status})

def run_server():
    # for integration test
    app.run(port=5000, debug=False)

if __name__ == '__main__':
    app.run(debug=True)
