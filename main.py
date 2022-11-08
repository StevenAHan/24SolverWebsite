from flask import Flask, render_template

import subprocess

output = subprocess.run(["./solver", "1", "5", "5", "5", "y"], stdout = subprocess.PIPE, universal_newlines = True).stdout
output = output[:-1] # remove endline at the end of output
print(output)