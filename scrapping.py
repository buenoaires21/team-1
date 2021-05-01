from bs4 import BeautifulSoup, Tag
import requests
import json

def scrappingUdemy():
    url = 'https://www.udemy.com/featured-topics/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Sections
    for script in (soup.find_all('script')):
        s:Tag = script
        if s.string is not None and "navigation_categories" in s.string:
            firstmatch = s.string.find("navigation_categories")
            content_categories = (s.string[s.string.find("navigation_categories") + 23:s.string.find("popular_subcategory_topics")])

            content_categories = (content_categories.strip()[:-1])

            categories_json = json.loads(content_categories)

            content_subcat = (s.string[s.string.find("popular_subcategory_topics")+28:])

            content_subcat = (content_subcat[:content_subcat.find("}]}")+3])

            subcat_json = json.loads(content_subcat)

            diccionarioSubcategorias = {}
            subdiccionarios = []
            diccionarioCategorias = {}

            for n in subcat_json:
                for contador in subcat_json[n]:
                     subdiccionarios.append(contador['title'])
                diccionarioSubcategorias[n] = subdiccionarios
                subdiccionarios = []

            for i in categories_json:
                for j in i['children']:
                    diccionarioCategorias[j['id']]= j['title']

            diccionarioFinal = {}
            for clave in diccionarioCategorias:
                for claveDos in diccionarioSubcategorias:
                    if clave == int(claveDos):
                        diccionarioFinal[diccionarioCategorias[clave]] = diccionarioSubcategorias[claveDos]
    return (transformarDiccionarioEnTupla(diccionarioFinal))

def transformarDiccionarioEnTupla(dic):
    listaux = []
    for i in dic:
        for j in dic[i]:
            tupla = (j, i, "Jóvenes y Adolescentes")
            listaux.append(tupla)
    tuplaFinal = tuple(listaux)
    return tuplaFinal





