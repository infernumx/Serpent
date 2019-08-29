import subprocess
import os

subprocess.call("pip3 install -r requirements.txt", cwd=os.getcwd(), shell=True)