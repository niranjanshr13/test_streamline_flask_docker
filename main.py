#!/usr/bin/python3
from flask import Flask


@app.route("/",strict_slashes=False)
def index():
  return 'ok'

if __name__ == '__main__':
    app.debug = False
    app.run()
