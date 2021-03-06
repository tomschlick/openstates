import datetime

metadata = dict(
    name='Indiana',
    abbreviation='in',
    legislature_name='Indiana General Assembly',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Representatives',
    upper_chamber_title='Senator',
    lower_chamber_title='Representative',
    upper_chamber_term=4,
    lower_chamber_term=2,
    terms=[
        {'name': '2011-2012', 'start_year': 2011,
         'end_year': 2012, 'sessions': ['2011']},
        ],
    session_details={
        '2011': {'start_date': datetime.date(2011, 1, 5),
                 'display_name': '2011 Regular Session',
                },
        },
    feature_flags=['subjects'],
)

def session_list():
    from billy.scrape.utils import url_xpath
    # cool URL bro
    return url_xpath('http://www.in.gov/legislative/2414.htm', '//h3/text()')
