from flask import Flask, request, render_template
import data

app = Flask(__name__,  static_url_path='', static_folder="frontend/static", template_folder="frontend/templates")

@app.route('/table')
def page_table():
    
    return render_template("table.html")

@app.route('/faq')
def page_faq():
    return render_template("faq.html")

@app.route('/bar')
def page_bar():
    return render_template("bar.html", graphJSON=data.create_bar())

@app.route('/line')
def page_line():
    return render_template("bar.html", graphJSON=data.create_line())

@app.route('/sunburst')
def page_sunburst():
    return render_template("bar.html", graphJSON=data.create_sunburst())


