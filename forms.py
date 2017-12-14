from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class BookForm(Form):
    title = StringField('Book Title', validators=[validators.InputRequired(), validators.Length(min=1, max = 20)])
    description = TextAreaField('Book Description')
    price_choices = [('10', 'Basic Price $10'), ('20', 'Premium Price $20')]
    price = SelectField('Book Price', choices=price_choices, default='10')
    rating_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = RadioField('Ratings', choices=rating_choices, default='1')
