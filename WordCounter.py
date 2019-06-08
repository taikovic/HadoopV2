from mrjob.job import MRJob

class WordCounter(MRJob):
    def mapper(self, _, line):
        words = line.split()
        for word in words:
            if len(word)>10:
                yield word.lower(),1
                
    def reducer(self,key,values):
        yield key, sum(values)
        
if __name__ == '__main__':
    WordCounter.run()