from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, Email


STATES = ["Alaska",
          "Alabama",
          "Arkansas",
          "American Samoa",
          "Arizona",
          "California",
          "Colorado",
          "Connecticut",
          "District of Columbia",
          "Delaware",
          "Florida",
          "Georgia",
          "Guam",
          "Hawaii",
          "Iowa",
          "Idaho",
          "Illinois",
          "Indiana",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Massachusetts",
          "Maryland",
          "Maine",
          "Michigan",
          "Minnesota",
          "Missouri",
          "Mississippi",
          "Montana",
          "North Carolina",
          " North Dakota",
          "Nebraska",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "Nevada",
          "New York",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Puerto Rico",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Virginia",
          "Virgin Islands",
          "Vermont",
          "Washington",
          "Wisconsin",
          "West Virginia",
          "Wyoming"]


class NewUserForm(FlaskForm):
    """Form for user"""
    username = StringField('Username', validators=[InputRequired(message='Please enter a Username'), Length(
        min=4, max=50, message='Please select a valid length of between 4 and 50 characters')])
    password = PasswordField('Password', validators=[
                             InputRequired(message='Please enter a password of at least 8 characters'), Length(
                                 min=8, max=255, message='Please select a valid length of between 8 and 255 characters')])
    email = StringField('Email Address', validators=[InputRequired(message='This field is required'), Length(
        min=6, max=255, message='Please enter a valid length between 6 and 255 characters'), Email(message='Please enter a valid email address')])
    first_name = StringField('First Name', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    last_name = StringField('Last Name', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    street_address = StringField('Street Address', validators=[
                                 InputRequired(message='This field is required')])
    apartment_number = StringField('Apartment Number', validators=[Length(
        max=255, message='Please enter a valid length under 255 characters')])
    city = StringField('City', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    state = SelectField('State', choices=[(state, state) for state in STATES], validators=[
                        InputRequired(message='This field is required')])
    zip_code = StringField('Zip Code', validators=[InputRequired(message='This field is required'), Length(
        min=5, max=20, message='Please enter a valid length between 5 and 20 characters')])


class UserLoginForm(FlaskForm):
    """Form for user"""
    username = StringField('Username', validators=[InputRequired(message='Please enter a Username'), Length(
        min=1, max=50, message='Please select a valid length of between 1 and 50 characters')])
    password = PasswordField('Password', validators=[
        InputRequired(message='Please enter a password')])
    
class EditUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    last_name = StringField('Last Name', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    street_address = StringField('Street Address', validators=[
                                 InputRequired(message='This field is required')])
    apartment_number = StringField('Apartment Number', validators=[Length(
        max=255, message='Please enter a valid length under 255 characters')])
    city = StringField('City', validators=[InputRequired(message='This field is required'), Length(
        min=1, max=255, message='Please enter a valid length between 1 and 255 characters')])
    state = SelectField('State', choices=[(state, state) for state in STATES], validators=[
                        InputRequired(message='This field is required')])
    zip_code = StringField('Zip Code', validators=[InputRequired(message='This field is required'), Length(
        min=5, max=20, message='Please enter a valid length between 5 and 20 characters')])