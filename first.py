from flask import Flask, render_template, url_for, request, redirect
# import requests
import json 
import csv

app = Flask(__name__)
print(__name__) 

@app.route("/")
def home():
    return render_template('./index.html')

@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename) 

def append_dict_to_file(dictionary, filename="file.txt"):
    try:
        with open(filename, "a") as file:
            # Convert dictionary to a JSON string and append it to the file
            json.dump(dictionary, file)
            file.write("\n")  # Add newline to separate multiple dictionary entries
    except Exception as e:
        print(f"Error while appending to file: {e}")

def write_to_csv(data):
    try:
        with open('database.csv', "a", newline='') as database2:
            # Convert dictionary to a JSON string and append it to the file
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message]) 
    except Exception as e:
        print(f"Error while appending to database : {e}")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


# @app.route("/index.html")
# def home_index():
#     return render_template('./index.html')


# @app.route("/about.html")
# def about():
#     return render_template('./about.html')

# @app.route("/components.html")
# def components():
#     return render_template('./components.html')

# @app.route("/contact.html")
# def contacts():
#     return render_template('./contact.html')

# @app.route("/works.html")
# def works():
#     return render_template('./works.html')

# @app.route("/work.html")
# def work():
#     return render_template('./work.html')

# @app.route("/thankyou.html")
# def thankyou():
#     return render_template('./thankyou.html')

# @app.route("/<username>")
# def hello_world2(username=None):
#     # print(url_for('static', filename='bolt.ico'))
#     return render_template('./index.html', name=username)

# @app.route('/blog/<blogname>')
# def blog_name(blogname=None):
#     return render_template('./blog.html',blog=blogname)

# @app.route("/blog")
# def blog():
#     return "<p>this is a blog</p>"

# @app.route("/blog/2020/dogs")
# def blog_dog():
#     return "<p>this is a blog of dogs in 2020</p>"