import pickle as c
from collections import Counter
import os
tags=dict()
count=0
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y%H%M%S")

# creating dictionary of most commanly used words overall in data
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now","How","I","Why"]
def load(clf_file):
    with open(clf_file,"rb") as fp:
        clf = c.load(fp)
    return clf
words=[]
f=open("all.txt","r")
for i in f:
    i=i.rstrip()
    i=i.split(" ")
    for x in i:
        if x in stop_words:
            continue
        else:
            words.append(x)
for i in range(len(words)):
    if not words[i].isalpha():
        words[i]=""
dictionary=Counter(words)
del dictionary[""]
ans=[]
d = os.getcwd()
directory=["logistic_train","svm_train","multinomial_train"]
dictionary=dictionary.most_common(4000)     #taking most common 4000 words

# predict for a question retived from user
inp= input("enter question to predict tags>")
for i in directory:
    path=d+"\\"+i
    #itereated the tags obtained from crawler
    list1=['javascript', 'java', 'c#', 'php', 'python', 'sql_server', 'jquery', 'html', 'c++', 'ios', 'css', 'mysql', 'sql', 'asp.net', 'ruby-on-rails', 'c', 'arrays', 'r', 'objective-c', 'node.js', '.net', 'json', 'android', 'angularjs', 'swift', 'iphone', 'regex', 'ruby', 'django', 'ajax', 'excel', 'xml', 'asp.net-mvc', 'linux', 'angular', 'python-3.x','database', 'spring', 'wordpress', 'reactjs', 'wpf', 'vba', 'string', 'xcode', 'windows', 'vb.net', 'laravel', 'html5', 'eclipse', 'multithreading', 'mongodb', 'bash', 'pandas', 'git', 'oracle', 'postgresql', 'forms', 'twitter-bootstrap', 'image', 'macos', 'algorithm', 'python-2.7', 'scala', 'list', 'visual-studio', 'typescript', 'winforms', 'apache', 'matlab', 'performance', 'facebook', 'excel-vba','entity-framework', 'css3', 'hibernate', 'amazon-web-services', 'sqlite', 'function', 'linq', 'firebase', 'azure', 'swing', 'rest', 'shell', 'qt', 'powershell', 'api', 'maven', '.htaccess', 'file', 'unit-testing', 'selenium', 'loops', 'codeigniter', 'spring-boot', 'csv', 'perl', 'numpy', 'symfony', 'google-maps', 'docker', 'class', 'uitableview', 'web-services', 'cordova', 'google-chrome', 'tsql', 'sorting']

    for i in list1:
        clf=load(path+"\\"+i+".mdl")
        features=[]
        for entry in dictionary:
            features.append(inp.count(entry[0]))
        res=clf.predict([features])
        if res[0]==1:
            ans.append(i)
    a = dict(Counter(ans))
# generating the tags in .txt file in result folder
for tag,count in a.items():
    if count>2:
        print(tag)
        result=open(d+"\\"+"result\\"+dt_string+".txt","a")
        result.write(tag+",")
