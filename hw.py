import re
def cal_age20(ag):
    age20 = ag + 20
    return age20

def show(st,ag):
    print('the name is {} and age is {}'.format(st,str(ag)))
    print('the age after 20yrs will be {}'.format(str(cal_age20(ag))))

print('hello all people')
stt = input("enter your name: ")
agg = int(input("enter your age: "))
strt = "my name is Ram and my brother's name is Lakshman"
pat = list(re.findall('name',strt))
print("the no.of times a string having 'name' word: ", len(pat))

show(stt,agg)