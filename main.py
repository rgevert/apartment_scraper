from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.portalinmobiliario.com/"

def build_url(core_params: {}, filter_params: {}):
    core_params_list = list(map(lambda x: str(x), core_params.values()))
    return URL + "/".join(core_params_list)


core_params = {
  "contract_type": "arriendo",
  "building_type": "departamentos",
  "location": "las-condes-metropolitana"
}

filter_params = {
}

page = urlopen(build_url(core_params = core_params, filter_params = filter_params))
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, features="html.parser")
print(soup.prettify())


# arriendo/departamento/3-dormitorios/las-condes-metropolitana#applied_filter_id%3DBEDROOMS%26applied_filter_name%3DDormitorios%26applied_filter_order%3D9%26applied_value_id%3D%5B3-3%5D%26applied_value_name%3D3+dormitorios%26applied_value_order%3D4%26applied_value_results%3D740%26is_custom%3Dfalse'
