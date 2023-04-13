# This module is used to get the CPU and from my server.
import psutil
# This module is used to create and style the application. 
from flask import Flask, render_template

# Application code for the Home Path.
app = Flask(__name__)
# Function will show the users running this path, then define CPU, memory and message as variables.
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Utilisation detected. Please scale up"
# Using code from the HTML file using parameters.       
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)
    
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0')   
    