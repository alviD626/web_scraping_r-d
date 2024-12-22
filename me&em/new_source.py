import requests
from bs4 import BeautifulSoup

url = "https://www.meandem.com/merino-stretch-rib-two-way-zip-jumper-cream"

def get_response(url):
    payload = {}
    headers = {
    'cookie': 'akacd_prod-akoova-vercel=3910600862~rv=79~id=920708aebc6912f920453cc9cc5e6ee2; GlobalE_Full_Redirect=false; GlobalE_Welcome_Data=%7B%22showWelcome%22%3Afalse%7D; GlobalE_SupportThirdPartCookies=true; OptanonAlertBoxClosed=2024-12-02T14:01:09.926Z; MEEM_GUEST_CART_uk=6NQk7UOpzoKajoRF04FWD4QIx3jbhdcA; MEEM_GUEST_TOKEN=; GlobalE_Data=%7B%22countryISO%22%3A%22GB%22%2C%22currencyCode%22%3A%22GBP%22%2C%22cultureCode%22%3A%22en-GB%22%7D; AKA_A2=A; GlobalE_CT_Data=%7B%22CUID%22%3A%7B%22id%22%3A%22181257069.489116053.755%22%2C%22expirationDate%22%3A%22Mon%2C%2002%20Dec%202024%2018%3A04%3A23%20GMT%22%7D%2C%22CHKCUID%22%3Anull%2C%22GA4SID%22%3A501970761%2C%22GA4TS%22%3A1733160863192%2C%22Domain%22%3A%22.meandem.com%22%7D; GlobalE_CT_Data=%7B%22CUID%22%3A%7B%22id%22%3A%22181257069.489116053.755%22%2C%22expirationDate%22%3A%22Mon%2C%2002%20Dec%202024%2018%3A04%3A23%20GMT%22%7D%2C%22CHKCUID%22%3Anull%2C%22GA4SID%22%3A501970761%2C%22GA4TS%22%3A1733160863590%2C%22Domain%22%3A%22.meandem.com%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Dec+02+2024+09%3A34%3A30+GMT-0800+(Pacific+Standard+Time)&version=202403.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f3cc2105-eb5d-4d15-9bec-0f7a465c9d7e&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=BD%3BC&AwaitingReconsent=false; akacd_prod-akoova-vercel=3910683442~rv=98~id=a25f2017af28bac297c5478257ad866b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def source(url):
    response = get_response(url)
    source = BeautifulSoup(response.text, "html.parser")
    return source

print(source(url))