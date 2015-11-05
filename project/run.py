# project/run.py

#for local serving
# from views import app
# app.run(debug=True)

#for heroku deployment
import os
from views import app

post = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
