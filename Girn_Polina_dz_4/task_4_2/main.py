import requests


resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(code):
    key = []
    val = []
    curse = {}
    content = resp.text
    for el in content.split('<CharCode>')[1:]:
        key.append(el.split('</CharCode>'[0])[0])
    for el in content.split('<Value>')[1:]:
        val.append(el.split('</Value>'[0])[0])

    print(len(key), key)
    print(len(val), val)

    for i in range(len(key)):
        curse[key[i]] = val[i]

    return float(curse[code].replace(',', '.'))

