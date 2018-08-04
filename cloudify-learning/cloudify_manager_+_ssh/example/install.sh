#!/usr/bin/env bash

cat > app.py <<- EOF
#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
EOF

pip install Flask --user --verbose
FLASK_APP=app.py nohup flask run --host=0.0.0.0 > /dev/null 2>&1 & echo $! > app.py.pid
sleep 5
