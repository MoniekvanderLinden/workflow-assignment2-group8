import json

f = open('../../gen/data-preparation/temp/whitehouse_briefing_27_04.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tfollowers_count\tlanguage\ttext\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))

    try:
        followers = obj.get('user').get('followers_count')
    except:
        followers = 'NA'

    try:
        language = obj.get('lang')
    except:
        language = 'NA'

    text = obj.get('text')
    text = text.replace('\t', ' ').replace('\n', '')

    outfile.write(obj.get('id_str')+'\t'+str(followers)+'\t'+str(language)+'\t'+text+'\n')
    #if (cnt>1000): break

print('done.')
