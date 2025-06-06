# # Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.  
# # Licensed under the GNU General Public License v3.0.  
# # See LICENSE file in the repository root for full license text.

# import os
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def welcome():
#     # Render the welcome page with animated "Team SPY" text
#     return render_template("welcome.html")

# if __name__ == "__main__":
#     # Default to port 5000 if PORT is not set in the environment
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)


# Copyright (c) 2025 devgagan : https://github.com/Shivaay20005.
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    # Redirect directly to your Telegram profile
    return redirect("https://t.me/Shivaay20005", code=302)

if __name__ == "__main__":
    # Default to port 5000 if PORT is not set in the environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)