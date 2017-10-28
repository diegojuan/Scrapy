start_urls = ['http://www.dislicoresstore.com/vinos.html']

for i in range(1,6):
    url = start_urls[0] + "?p=" + str(i)
    print url
