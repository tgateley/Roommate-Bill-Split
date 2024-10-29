from flask import Flask, render_template, request, flash
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    amount = StringField(label="Bill Amount: ")
    period = StringField(label="Bill-Cycle: ")
    roommate1 = StringField(label="Name: ")
    days_in_house1 = StringField(label="Days stayed in house: ")
    roommate2 = StringField(label="Name: ")
    days_in_house2 = StringField(label="Days stayed in the house: ")

    button = SubmitField(label='Submit')



app.add_url_rule("/", view_func=HomePage.as_view('home_page'))
app.add_url_rule("/bill", view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule("/result", view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
