import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "URL" :"https://www.amazon.in/Dell-3493-i3-1005G1-Integrated-D560194WIN9SE/dp/B087V8KK6Z/ref=sr_1_4?dchild=1&fst=as%3Aoff&qid=1601019581&refinements=p_89%3ADell&rnid=3837712031&s=computers&sr=1-4",
        "name" :"Dell",
        "target_price": 35000
    },
    {
        "URL": "https://www.amazon.in/HP-eq0024au-15-6-inch-Windows-Graphics/dp/B084656F9P/ref=sr_1_2?dchild=1&fst=as%3Aoff&qid=1601020473&refinements=p_89%3AHP&rnid=976393031&s=computers&sr=1-2",
        "name": "HP",
        "target_price": 40000
    },
    {
        "URL": "https://www.amazon.in/Lenovo-Ideapad-Laptop-Windows-81W10057IN/dp/B087D3JHGB/ref=sr_1_3?dchild=1&fst=as%3Aoff&qid=1601020715&refinements=p_89%3ALenovo&rnid=3837712031&s=computers&sr=1-3",
        "name": "Lenovo",
        "target_price": 35000
    },
    {
        "URL": "https://www.amazon.in/Renewed-Notebook-i5-10210U-Graphics-XMA1901-DG/dp/B08BYR2S22/ref=sr_1_10?dchild=1&fst=as%3Aoff&qid=1601021014&refinements=p_89%3AMI&rnid=3837712031&s=computers&sr=1-10",
        "name": "MI",
        "target_price": 40000
    },
    {
        "URL": "https://www.amazon.in/ASUS-i3-1005G1-Integrated-Transparent-X409JA-EK372T/dp/B08CHZ8MPF/ref=sr_1_4?dchild=1&fst=as%3Aoff&qid=1601021181&refinements=p_89%3AASUS&rnid=3837712031&s=computers&sr=1-4",
        "name": "ASUS",
        "target_price": 40000
    }
]

# URL = "https://www.amazon.in/HP-eq0007au-15-6-inch-Windows-Graphics/dp/B08496K8JL/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&qid=1601016010&refinements=p_89%3AHP&rnid=3837712031&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLUDRCTUdCUTdXMlcmZW5jcnlwdGVkSWQ9QTAxMTIyMDVHTlNYRkdNT0MwVEQmZW5jcnlwdGVkQWRJZD1BMDIzNDU1NDFTRjNCMEFBMURIV0Ymd2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3NlJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

# URL = "https://www.amazon.in/Dell-3493-i3-1005G1-Integrated-D560194WIN9SE/dp/B087V8KK6Z/ref=sr_1_4?dchild=1&fst=as%3Aoff&qid=1601019581&refinements=p_89%3ADell&rnid=3837712031&s=computers&sr=1-4"

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()

result_file = open('my_result_file.txt', 'w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("URL"))
        print(product_price_returned + "-" + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + '- \t'+ 'Available at Target Price ' + '\n' + ' Current Price - ' +str(my_product_price) + '\n')

        else:
            print("Still at Current price")

finally:
    result_file.close()



