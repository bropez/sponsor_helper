
def get_set():
    the_set = set()
    with open('advert_list_cleaned.txt', 'r', encoding='utf-8') as f:
        for line in f:
            the_set.add(line)

    return the_set

if __name__ == '__main__':
    thingy = get_set()
    for line in thingy:
        print(line)