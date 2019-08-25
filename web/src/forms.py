from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class CarForm(FlaskForm):
    FUEL_TYPE = {"Petrol": 1, "Diesel": 0}
    TRANSMISSION_TYPE = {"Automatic": 1, "Manual": 0}
    FUEL_SELECTION = [(1, "Petrol"), (2, "Diesel")]
    TRANSMISSION_SELECTION = [(1,"Automatic"), (2,"Manual")]
    COLOR_SELECTION = [ (1,"Regular"), (2,"Metallic")]
    car_age = IntegerField('Car Age (In Years)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    car_fuel = SelectField(label='Fuel Type', choices=FUEL_SELECTION, validators=[DataRequired()])
    car_doors = IntegerField('Number of Doors', validators=[DataRequired(), NumberRange(min=1, max=6)])
    car_cc = IntegerField('Car CC', validators=[DataRequired(), NumberRange(min=1, max=3000)])
    car_horsepower = IntegerField('Car HP', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    car_transmission = SelectField(label='Transmission Type', choices= TRANSMISSION_SELECTION, validators=[DataRequired()])
    car_odometer = IntegerField('Odometer (in Kilometers)', validators=[DataRequired(), NumberRange(min=1, max=10000000)])
    car_weight = IntegerField('Car Weight (in Kilograms)', validators=[DataRequired(), NumberRange(min=1, max=10000)])
    car_color = SelectField(label='Color Type', choices=COLOR_SELECTION,validators=[DataRequired()])
    predict = SubmitField('Predict!')

