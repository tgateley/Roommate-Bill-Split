from flask import Flask, render_template, requests, flash
from flask.views import MethodView
from wtforms import Form

app = Flask(__name__)


class HomePage(MethodView):
    pass


class BillFormPage(MethodView):
    pass


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass
