from os import path
from settings import BASE_DIR
import argparse

VIEWS_PATH = r"/home/pythonist/PycharmProjects/TryDjango/Article/views.py"
print(BASE_DIR)
BASE_TEMPLATE = """{% extends "base.html" %}

{% block content %}

{% endblock %}"""

args = argparse.ArgumentParser()
args.add_argument("-f", required=True, type=str, help="path to the file")
args.add_argument("-i", required=False, default=True, type=bool)
args.add_argument("-o", required=False, default=True, type=bool, help="overwrite file")
parser = args.parse_args()


def CreateViewFile(file_path):
    if path.exists(file_path) and not parser.o:
        print("File already exists")
    else:
        with open(VIEWS_PATH, "+a") as f:
            f.write(
                """
def {}(request):
    return render(request, "{}.html")
            
            """.format(
                    file_path, file_path
                )
                + ""
            )


def CreateHTMLFile(file_path):
    if path.exists(file_path) and not parser.o:
        print("File already exists")
    else:
        with open(file_path, "+w") as f:
            f.write(BASE_TEMPLATE)
            CreateViewFile(parser.f)
            f.close()
            print("File created")


TEMPLATE_PATH = BASE_DIR / "templates"
NEW_TEMPLATE = path.join(TEMPLATE_PATH, parser.f + ".html")
CreateHTMLFile(NEW_TEMPLATE)
