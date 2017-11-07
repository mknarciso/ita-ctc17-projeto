from lxml import html
import requests
import codecs
import sys

page = requests.get("https://www.letras.mus.br/mais-acessadas/funk/")
tree = html.fromstring(page.content)
top = tree.xpath('//ol[@class="top-list_mus cnt-list--col1-3"]/li/a/@href')
main = "https://www.letras.mus.br"
artists = tree.xpath('//ol[@class="top-list_art"]/li/a/@href')
lyrics_add = []
art = 0
for a in artists:
    print a
    print float(art) / len(artists)
    p = requests.get("https://www.letras.mus.br"+a)
    t = html.fromstring(p.content)
    exp = t.xpath('//ol[@class="cnt-list cnt-list--num cnt-list--col2"]/li/a/@href')
    top = top + exp
    art +=1
for t in top:
    lyrics_add.append(main+t)
lyrics_add = list(set(lyrics_add))
print lyrics_add
print len(lyrics_add)
ans = []
lyrics_add.remove("https://www.letras.mus.br/mc-duduzinho/1943838/")
lyrics_add.remove("https://www.letras.mus.br/mc-pedrinho/hit-do-verao/")
lyrics_add.remove("https://www.letras.mus.br/mc-duduzinho/1902856/")
lyrics_add.remove("https://www.letras.mus.br/mc-g7/que-delicia--essa/")
lyrics_add.remove("https://www.letras.mus.br/mc-kauan/1837095/")
lyrics_add.remove("https://www.letras.mus.br/mc-duduzinho/1957243/")
total = len(lyrics_add)
count = 0
print total
max_size = 0
min_size = 999999999
for add in reversed(lyrics_add):
    try:
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
        size = len(lyric)
        if size < min_size:
            min_size = size
            print "Min size: " + str(min_size) 
        if size > max_size:
            max_size = size
            print "Max size: " + str(max_size)
        print float(count)/total
    except:
        sys.exc_clear()

thefile = codecs.open('funk_all.txt', 'w', "utf-8")
for item in ans:
  thefile.write("%s\n" % item)

print "Min size: " + str(min_size) 
print "Max size: " + str(max_size) 