from flask import Flask, render_template, redirect, url_for, request

import subprocess

app = Flask(__name__)

app.config["SECRET_KEY"] = "HAVEFUN!"

# Default route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        numbers = request.form.get("numbers")
        show_ans = request.form.get("show-ans")
        print("numbers:", numbers)
        to_input = ["./solver"]
        numbers_arr = numbers.split()
        to_input += numbers_arr
        to_input.append(show_ans)
        print(to_input)
        output = subprocess.run(to_input, stdout = subprocess.PIPE, universal_newlines = True).stdout
        output = output[:-1] # remove endline at the end of output
        return redirect(url_for('home'))

    return render_template("index.html")

    
if __name__ == "__main__":
    app.run(debug=True)



# print(output)