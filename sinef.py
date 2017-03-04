import requests
from lxml import html


sinef = requests.get('https://ww2.fumec.br/sinefmobile/')

page = html.fromstring(sinef.text)

page.forms[0].fields = dict(registro='1A225733701', senha='211992')

print(type(html.submit_form(page.forms[0])))
# result = html.submit_form(form)
# [a.attrib['href'] for a in result.xpath("//a[@target='_blank']")]
