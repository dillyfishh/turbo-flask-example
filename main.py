from flask import Flask, render_template, session, abort
from threading import Thread
from time import sleep
from turbo_flask import Turbo
import uuid

# Setup Flask application
app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "ExampleSecretKey"  # Replace with your actual secret key

# Setup Turbo-Flask
turbo = Turbo(app)

# Keep track of users currently uploading files
uploading_users = set()

@turbo.user_id
def get_userid():
    # Return the user's session ID
    return session['user_id']

@app.route("/")
def home():
    # Assign a new user id if not already present in the session
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('home.html', userid=session['user_id'])

@app.route("/upload_file")
def upload_file():
    # Assign a new user id if not already present in the session
    if 'user_id' not in session:
      session['user_id'] = str(uuid.uuid4())
        
    # Get current user id
    user_id = session['user_id']

    # Check if the user is already uploading a file
    if user_id in uploading_users:
        abort(403)  # If so, send a "Forbidden" response
    else:
        uploading_users.add(user_id)  # Otherwise, mark the user as currently uploading

    def update_progress():
        with app.app_context():
            # Simulate uploading 30 files
          simulated_file_count = 30
          
          for i in range(simulated_file_count):
              print(f"Uploading File - {i}")
              # Simulate a delay
              sleep(1)
              # Push the current progress to the client
              try:
                turbo.push(turbo.replace(render_template('progress-bar.html', value=i+1, max=simulated_file_count), 'progress-bar'), to=user_id)
              except:
                pass
          # Remove the user from the uploading set when the upload is complete
          uploading_users.remove(user_id)
    
    # Start a new thread to handle the upload process
    Thread(target=update_progress).start()
    
    # Send a successful response
    return "", 200
