from selenium.webdriver import Firefox
from get_advert_list import get_set


adverts_list = get_set()


def get_links(text):
    link_list = []
    words = text.split()
    for word in words:
        if '.com' in word or 'https' in word:
            link_list.append(word)

    return link_list


def check_adverts(text):
    # TODO: see if any of the sponsors are in the 'advert_list_cleaned.txt'


browser = Firefox()
# address = 'C:\Users\Matthew\Desktop\files\pythonPrograms\mturk\peter_birsinger_advert\test.html'
# browser.get(address)
file_path = 'C://Users//Matthew//Desktop//files//pythonPrograms//mturk//peter_birsinger_advert//test.html'
browser.get('file:///' + file_path)

browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))

# getting the text from xpath
tag_thing = browser.find_element_by_xpath('/html/body/crowd-form/form/div/p[5]')
# tag_thing = browser.find_element_by_tag_name('strong')

# getting the datalist of advertisers
ad_list = []
known_good_advert = browser.find_element_by_id('known-advertisers')
print(known_good_advert)
options = known_good_advert.find_elements_by_tag_name('option')
for option in options:
    print(option.text)
    ad_list.append(option)
# options = [x for x in known_good_advert.find_element_by_tag_name('option')]

# thingy = get_links(tag_thing.text)
# for link in thingy:
#     print(link)

