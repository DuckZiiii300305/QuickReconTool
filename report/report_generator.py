from jinja2 import Environment, FileSystemLoader
import os

def generate_report(target, data):
    env = Environment(loader=FileSystemLoader("report"))
    template = env.get_template("template.html")

    html = template.render(data=data)

    with open(f"results/{target}/report.html", "w") as f:
        f.write(html)