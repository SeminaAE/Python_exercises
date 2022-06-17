#Написать модуль, который реализует сравнение строк
#одним из рассмотренных в лекции методом.

def compare (S1, S2):
    ngrams = [
    S1 [i:1+3] for i in range (len(S1))
    ]
    count=0
    for ngram in ngrams:
        count += S2.count(ngram)
    r=count/max(len(S1), len (S2))
    
#Написать в модуле if name == 'main' 
#в котором провести проверку работы модуля,
#напрмер как в лекции - парами строк.

if _name_ == '_main_':
    print ('Результат', r )

#Написать программу, которая перебирает
#все элементы списка (задан в программе)
#с некоторой строковой константой (также задана).

spisok = ['Абажур', 'Аббревиатура', 'Абзац', 'Абитуриент']
constanta = 'ур'

for element in spisok:
    if (element.find(constanta)):
        print (element)