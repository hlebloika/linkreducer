from flask import Flask, render_template, request, redirect
import string, random

app = Flask(__name__)
match_urls = {}

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        original_url = request.form['input_link']
        link_id = "".join([random.choice(string.ascii_letters) for i in range(6)])
        short_url="http://35.179.15.24/" + link_id
        match_urls[link_id] = original_url
        return "<p>" + short_url + "</p>"
    return render_template("base.html")

@app.route("/<link_id>")
def redirect_to_original_url(link_id):
    url_to = match_urls[link_id]
    return redirect(url_to)

