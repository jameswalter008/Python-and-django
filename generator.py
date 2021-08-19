words=['apple','orange','lemon','lime','banana']

from random import randint;
def randomSentenceGenerator(word):
    randomindex=randint(0,len(words)-1)
    return f'{words[randomindex]} {word}'

with open('./write.txt')as file:
    paragraph=file.read();
    wordlist=paragraph.split()#['asdf','jkl;']
    sentencelist=list(map(randomSentenceGenerator,wordlist))

    paracount= int(input('paragraph count : '))

    for count in range(paracount):
        with open('./generator.txt','a') as write_file:
            write_file.write(paragraph+ ''.join(sentencelist)+'\n\n')