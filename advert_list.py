import html.parser as htmlparser


with open('advert_list.txt', 'r', encoding='utf-8') as f:

    with open('advert_list_cleaned.txt', 'a+', encoding='utf-8') as f2:

        for line in f:
            # line = parser.unescape(line)
            splitter = htmlparser.unescape(line).split('option value="')[1]
            splitter_again = splitter.split('">')[0]

            f2.write(splitter_again + '\n')
            print(splitter_again)
