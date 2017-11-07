from lxml import html
import requests
import codecs

page = requests.get("https://www.letras.mus.br/mais-acessadas/funk/")
tree = html.fromstring(page.content)
top = tree.xpath('//ol[@class="top-list_mus cnt-list--col1-3"]/li/a/@href')
main = "https://www.letras.mus.br"
lyrics_add = []
for t in top:
    lyrics_add.append(main+t)
ans = []
lyrics_add.remove("https://www.letras.mus.br/mc-duduzinho/1943838/")
lyrics_add.remove("https://www.letras.mus.br/mc-pedrinho/hit-do-verao/")
total = len(lyrics_add)
count = 0
for add in reversed(lyrics_add):
    print add
    p = requests.get(add)
    t = html.fromstring(p.content)
    lyric_array = t.xpath('//article/p/text()')
    lyric = ""
    print lyric_array[0].encode('iso-8859-1').decode('utf-8')
    for s in lyric_array:
        lyric = lyric + s.encode('iso-8859-1').decode('utf-8') + "\n"
    ans.append(lyric)
    count += 1
    print float(count)/total

thefile = codecs.open('funk1000.txt', 'w', "utf-8")

for item in ans:
  thefile.write("%s\n" % item)