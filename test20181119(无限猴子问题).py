import random
import time

string = '''hahahah You don't understand! I coulda had class. I coulda been a contender.
I could've been somebody,instead of a bum, which is what I am.
And God blessed them, and God said unto them, Be fruitful, and multiply, 
and replenish the earth, and subdue it: and have dominion over the fish of the sea, 
and over the fowl of the air,and over every living thing that moveth upon the earth.
'''

def guess():
    # 主函数
    # print(string[0])
    wordstring = 'abcdefghijklmnopqrstuvwxyz'+' '+'abcdefghijklmnopqrstuvwxyz'.upper()+'.'+'\''+','
    # print(len(wordstring))
    newlist = []
    # print(random.sample(wordstring,1))

    for x in range(0,len(string)):#重复匹配操作到所有字符串都匹配完毕

        for i in range(0,1000):#随机抽取字符集里面的一个字母去匹配源字符串的第X位字母
            word = ''.join(random.sample(wordstring,1))
            
            if word == string[x]:
            
                newlist.append(word)#匹配成功后加入新列表，退出循环
                break
            i+=1
        x+=1
    print(''.join(newlist))

if __name__ == '__main__':
    guess()