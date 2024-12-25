from bs4 import BeautifulSoup
import requests
import smtplib
import datetime as dt

URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B075CYMYK6/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.6750a477-b756-4495-9032-f19cde6d7085&dib=eyJ2IjoiMSJ9.qSgqFVsUTOow5wAvcdE1QIB56vmxIdNM0-Ex7KheOFCwlyyivE_FuPeZfLZ11W_pFotFMNi960pcug-A0xrCpsydIoOzqUTgCXRvl4gsbIK4vUAGajS5AIKeWGVHo46cG6MCn-S42Uo1rgtmMa3o5coy9qYPLJHlq-ClF30OpKxQh9zzzTlN--0Juubu1WF6SzrEL8xlve5sg5pM-0N7FOD1ueoDGj5jKkb2WvinoOs.K-Ivc5lHkoiBLBg9UVgdmRElRhcVm-oe3XE0XMVJ1N8&dib_tag=se&keywords=cooker&pd_rd_r=0aed5344-bf6f-407a-8cc3-a64981704873&pd_rd_w=4T0cE&pd_rd_wg=Wi2Vg&pf_rd_p=6750a477-b756-4495-9032-f19cde6d7085&pf_rd_r=3CW6BAYNYCZAP1RMWE9B&qid=1735123635&sr=8-3&th=1"

bütçem = 99.99

my_email = "selemeceneme216@gmail.com"
password = "wjot efsr wflf drfy"
now = dt.datetime.now()


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
fiyat_etiketi = soup.select("span #size_name_0_price")[0]
fiyat = fiyat_etiketi.getText().split("$")[1]

if float(fiyat)<bütçem:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mucahitakca2703@gmail.com",
                            msg=f"Beklediğin ürün {fiyat}fiyatına düştü!!!!")

