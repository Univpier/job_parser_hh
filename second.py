import json
from pprint import pprint
import re
from collections import Counter 
with open('data2.json', 'r', encoding ='utf8') as f:
    text = json.load(f)
    txt = ""
    pprint(text)
    for group in text:
        id_group = group['count']
        for objects in group['tags']:
         print(objects)
with open('data2.json', 'r', encoding ='utf8') as f:
    text = json.load(f)
    txt = ""
    tokens = []
    print(text)
    for group in text:
        id_group = group['count']
        for objects in group['tags']:
            txt = txt + '\n' + objects
            tokens.append(objects)         
text = re.sub('["|(|)|«|»|,]', '' , txt)
file_txt = open("text6.txt", "w", encoding="utf-8")
file_txt.write(txt)
file_txt.close()
file_txt = open("tokens6.txt", "w", encoding="utf-8")
for item in tokens:
    file_txt.write("%s\n" % item)
file_txt.close()
print(tokens)
print(text)   
array_d = {}.fromkeys(tokens, 0)
for a in tokens:
    array_d[a] += 1
if __name__ == '__main__':
    c = Counter(array_d)
    most = c.most_common()
file_txt = open("popular6.txt", "w", encoding="utf-8")
for item in most:
    file_txt.write(f"{item}\n")
file_txt.close()
def pop_tokens(path):
    with open(path, encoding="utf-8") as r:
        all_words = re.findall(r"[0-9a-zA-Zа-яА-Я)]+", r.read())
        txt = ""
        for word in all_words:
            clean2 = re.sub(r"[)]", ',' , word)
            txt = clean2.split()
            file_txt = open("text_tokens(Специалист по безопасности объектов критической инфраструктуры нефтегазового комплекса)6.txt", "a", encoding="utf-8")
            for item in txt:
                file_txt.write("%s " % item)
            file_txt.close()        
pop_tokens('popular6.txt')
def count_words(path):
    with open(path, encoding="utf-8") as file:
        all_words = re.findall(r"[0-9a-zA-Zа-яА-Я]{3,}", file.read())
        all_words = [word.upper() for word in all_words]
        print('\nTotalWords:', len(all_words))
        word_counts = Counter()
        for word in all_words:
            word_counts[word] +=1
        print('\nTop Words:')
        print(word_counts)
        for word in word_counts.most_common(1000):
            file_txt = open("text_popular.txt", "a", encoding="utf-8")
            file_txt.write(word[0]+'\n')
            file_txt.close()  
def pop_words(path):
    with open(path, encoding="utf-8") as r:
        all_words = re.findall(r"[0-9a-zA-Zа-яА-Я]+", r.read())
        for word in all_words:
            with open('data2.json', 'r', encoding ='utf8') as r:
                text = json.load(r)
                txt = ""
                for group in text:
                    for objects in group['tags']:
                        clean = re.sub('["|(|)|«|»|,]', '' , objects)
                        txt = clean.split()
                        for obj in txt:
                            if word == obj:
                                print(objects)
pop_words('text_popular.txt')
