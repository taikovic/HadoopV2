from mrjob.job import MRJob

class QuantiteVendue(MRJob):
    def mapper(self,_,line):
        #split line
        idProduit, quantiteVendue, date, prixUnit=line.split(',')
        yield int(idProduit), int(quantiteVendue)
        
    def reducer(self, produit,quantityValues):
        yield '%05d'%int(produit), sum(quantityValues)

class PrixTotalProduit(MRJob):
    def mapper(self,_,line):
        idProduit, quantiteVendue, date, prixUnit=line.split(',')
        yield int(idProduit), int(quantiteVendue) * int(prixUnit)
    def reducer(self,produit,prixTotal):
        yield '%05d'%int(produit),sum(prixTotal)        
                        
class produitParMois(MRJob):
    def mapper(self, _, line):
       idProduit, quantiteVendue, date, prixUnit=line.split(',')
       #date1=date.split('/') 
       #month=date1[1]
       month=date.split('/')[1]
       yield (idProduit,int(month)), int(prixUnit) 
    def reducer(self,key,price):
        yield key,sum(price)
        
class QuantityMax(MRJob):
    def mapper(self):
        QuantiteVendue.mapper(self)
    def reduce(self,key,values):
        k=list(key)
        v=list(values)
        return k[v.index(max(values))]

if __name__ == '__main__':
    QuantiteVendue.run()
    #PrixTotalProduit.run()
    #produitParMois.run()
    #QuantityMax.run()