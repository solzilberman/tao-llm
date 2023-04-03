import openai
import re
import httpx
import os
from dotenv import load_dotenv
import sys
from io import StringIO
import json
import subprocess


def wikipedia(q):
    return httpx.get(
        "https://en.wikipedia.org/w/api.php",
        params={"action": "query", "list": "search", "srsearch": q, "format": "json"},
    ).json()["query"]["search"][0]["snippet"]


def python_repl(what):
    # try:
    #     old_stdout = sys.stdout
    #     redirected_output = sys.stdout = StringIO()
    #     exec(what)
    #     sys.stdout = old_stdout
    #     if len(redirected_output.getvalue()) > 0:
    #         return str(redirected_output.getvalue())
    #     else:
    #         return "Warning: No output from Python code"
    # except Exception as e:
    #     return str(e)

    what = what.replace(";", "\n")
    with open("tmp.py", "w") as f:
        f.write(what)

    f = open("tmp.out", "w")
    result = subprocess.run(["python3", "tmp.py"], stdout=f, stderr=f)
    f.close()

    with open("tmp.out", "r") as f:
        data = f.read()

    os.system("rm tmp.py")
    os.system("rm tmp.out")
    return data


def terminal(what: str):
    f = open("tmp.out", "w")
    result = subprocess.run(what, shell=True, stdout=f, stderr=f)
    f.close()

    with open("tmp.out", "r") as f:
        data = f.read()

    os.system("rm tmp.out")
    return data
