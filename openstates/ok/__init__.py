metadata = dict(
    name='Oklahoma',
    abbreviation='ok',
    legislature_name='Oklahoma Legislature',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Representatives',
    upper_chamber_title='Senator',
    lower_chamber_title='Representative',
    upper_chamber_term=4,
    lower_chamber_term=2,
    terms=[
        {'name': '2011-2012',
         'start_year': 2011,
         'end_year': 2012,
         'sessions': ['2011']}
        ],
    session_details={
        '2011': {'display_name': '2011 Regular Session'},
    },
    feature_flags=['subjects'],
)

def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://webserver1.lsb.state.ok.us/WebApplication2/WebForm1.aspx',
        "//select[@name='cbxSession']/option/text()")
