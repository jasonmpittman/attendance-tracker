from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    class_date = Col('Class Date')
    student = Col('Student')
    keyword = Col('Keyword')
