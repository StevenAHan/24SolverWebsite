from flask import Flask, render_template, redirect, url_for, request, flash

import subprocess
import logging
import sys

app = Flask(__name__)

app.config["SECRET_KEY"] = "HAVEFUN!"

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# Default route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        numbers = request.form.get("numbers")
        show_ans = request.form.get("show-ans")
        if(numbers == "" or show_ans == ""):
            flash("Incorrect Inputs")
        to_input = ["./solver"]
        numbers_arr = numbers.split()
        to_input += numbers_arr
        to_input.append(show_ans)
        output = subprocess.run(to_input, stdout = subprocess.PIPE, universal_newlines = True).stdout
        output = output[:-1] # remove endline at the end of output
        outputs = output.split("\n")
        outputs[0] += " for " + str(numbers)
        if(len(outputs) - 1 > 0):
            outputs.insert(1, "Number of Solution(s): " + str(len(outputs) - 1))
        return render_template("index.html", outputs = outputs)

    return render_template("index.html", outputs = [""])

    
if __name__ == "__main__":
    app.run(debug=True)



# print(output)