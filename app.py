from flask import Flask, render_template, request, flash
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from roommate_bill import roommates

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)

        bill = roommates.Bill(float(bill_form.amount.data), bill_form.period.data)
        roommate1 = roommates.Roommate(bill_form.roommate1.data, float(bill_form.days_in_house1.data))
        roommate2 = roommates.Roommate(bill_form.roommate2.data, float(bill_form.days_in_house2.data))
        return render_template("results.html",
                               name1=roommate1.name,
                               amount1=roommate1.pays(bill, roommate2),
                               name2=roommate2.name,
                               amount2=roommate2.pays(bill, roommate1))


class BillForm(Form):
    amount = StringField(label="Bill Amount: ")
    period = StringField(label="Bill-Cycle: ")

    roommate1 = StringField(label="Name: ")
    days_in_house1 = StringField(label="Days stayed in house: ")

    days_in_house2 = StringField(label="Days stayed in the house: ")
    roommate2 = StringField(label="Name: ")

    button = SubmitField(label='Submit')


app.add_url_rule("/", view_func=HomePage.as_view('home_page'))
app.add_url_rule("/bill", view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule("/results", view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
