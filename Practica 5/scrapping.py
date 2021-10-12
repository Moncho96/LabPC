#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def wiki():
    soup = get_soup("https://en.wikipedia.org/wiki/List_of_states_of_Mexico")
    rows = soup.find_all("table")[0].find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        t = [ele.text.strip() for ele in columns]
        print(f"{t}")


def google_images():
    soup = get_soup(
        "https://www.google.com/search?q=perros&sxsrf=ALeKk02jGsCChitxcd1n9i8fZNIA8H2y0A:1602915634703&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiwoIuI_rrsAhUKCKwKHYTdBI4Q_AUoAXoECAQQAw&biw=1280&bih=662"
    )
    images = soup.find_all("img")
    t = [{"src": image.get("src"), "alt": image.get("alt")} for image in images]
    print(f"{t}")


def transparencia_uanl():
    soup = get_soup(
        "http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php?pag_act=1&id_area_form=2305&mya_det=082020"
    )
    tr = soup.find_all("table")[2].find_all("tr")
    for row in tr:
        cols = row.find_all("td")
        t = [ele.text.strip() for ele in cols]
        print(f"{t}")


def fernanda():
    codigo = (
        "mx"  # str(input("introduzca el codigo del pais que desea conocer la Hora: "))
    )
    base = "https://cambiohorario.com/zonas/"
    response = requests.get(base + codigo)
    soup = BeautifulSoup(response.content, "html.parser")
    tr = soup.find_all("table")[2].find_all("tr")
    timezone = tr[0]
    for row in tr[1:]:
        cols = row.find_all("td")
        t = [ele.text.strip() for ele in cols]
        print(f"{t}")
    print(tr)


if __name__ == "__main__":
    fernanda()
