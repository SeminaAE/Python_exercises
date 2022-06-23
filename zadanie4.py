class Words():

    def __init__(self,S1,S2):
        self.S1=S1
        self.S2=S2        
        
    def compare(self):
        ngrams = [
        self.S1 [i:1+3] for i in range (len(self.S1))
        ]
        count=0
        for ngram in ngrams:
            count += self.S2.count(ngram)
        r=count/max(len(self.S1), len (self.S2))
        print ('Результат', r )
     
if __name__=='__main__':
       
    spisok=[('Абажур','Абитуриент'),('Аббревиатура','Абзац'),('Авария','Ашот')]
    for w1,w2 in spisok: 
        w=Words(w1,w2)
        w.compare()
   

    
    