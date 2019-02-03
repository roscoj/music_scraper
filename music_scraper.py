import requests
from bs4 import BeautifulSoup
import csv

DOMAIN = 'https://www.musicteachers.co.uk'

### SETUP ###
def raw_download(url):
    return requests.get(url)

def make_soup(html_doc, parser='html.parser'):
    return BeautifulSoup(html_doc.text, parser)



### HELPERS ###
def list_filter(list_of_objs, filter_str):
    return [item for item in list_of_objs if filter_str in item]

def prefix_list_item(list_of_objs, prefix_str):
    return [prefix_str + item for item in list_of_objs]

def teacher_has_phone_type(url, search_str):
    if soup(url).find('th', string=search_str): return True
    else: return False

def add_suffix(string, suffix):
    return string + str(suffix)



### MAIN FUNCTIONALITY ###
def all_anchors(some_soup):
    return [anchor.get('href') for anchor in some_soup.find_all('a') if anchor.get('href') is not None]


def teacher_title(url):
    return soup(url).find(class_='teacher-profile-name').string.split(' ')[0]

def first_name(url):
    return soup(url).find(class_='teacher-profile-name').string.split(' ')[1]

def last_name(url):
    return soup(url).find(class_='teacher-profile-name').string.split(' ')[2]

def phone(url):
    if teacher_has_phone_type(url, 'Phone:') == True:
        return soup(url).find('th', string='Phone:').next_element.next_element.next_element.string.strip()
    else: return '-'

def mobile(url):
    if teacher_has_phone_type(url, 'Mobile:') == True:
        return soup(url).find('th', string='Mobile:').next_element.next_element.next_element.string.strip()
    else:
        return '-'



### RETURN VALUES ###
def soup(url):
    return make_soup(raw_download(url))

def teacher_anchors(url):
    return prefix_list_item(list_filter(all_anchors(soup(url)), '/teacher/'), DOMAIN)

def rows(anchor_list):
    return [{'title': teacher_title(item), 'first_name': first_name(item), 'last_name': last_name(item), 'phone': phone(item), 'mobile': mobile(item), 'anchor': item} for item in anchor_list]



### CSV ###
def create_new_csv(file_name, list_of_rows):
    csv_file = open(file_name, 'w')
    with csv_file:
        headers = ['title', 'first_name', 'last_name', 'phone', 'mobile', 'anchor']
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        writer.writeheader()

        for row in list_of_rows:
            writer.writerow(row)


### MAIN LOOP ###

def run(url, page_num = 1, all_rows = []):
    if teacher_anchors(add_suffix(url, page_num)) != []:
        all_rows += rows(teacher_anchors(add_suffix(url, page_num)))
        run(url, page_num + 1, all_rows)
    else:
        create_new_csv('d.csv', all_rows)
        print('your csv file is ready...')


