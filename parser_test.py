import parser

URL = 'https://www.6pm.com/null/.zso?s=percentOff/desc/'
replyes = parser.parse(parser.get_html(URL))

for replye in replyes:
    print(replye)
