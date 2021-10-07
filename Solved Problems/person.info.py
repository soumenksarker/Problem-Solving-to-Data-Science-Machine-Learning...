class person_info:
     ''' Represent a people with a name,address and contact info'''
     def __init__(self, name,address,contact):
        """initializes the data"""
        self.name = name
        self.address = address
        self.contact = contact
        print ('(initializing the human : {})'.format(self.name))
     def tell(self):
        """ Hey guys my information is below"""
        print ('name : "{}" address : "{}"  contact : "{}"'.format(self.name, self.address, self.contact))
#import pickle
#peoplefile = 'people.data'
#people = {
           #'Masud' : 'khulna',
           #'toriqul':'Bogra',
           #'me' : 'Bogra',
           #'gourob' : 'Rajbari'
         #}

#f = open(peoplefile, 'wb')
#pickle.dump(people, f)
#f.close()

#del people
#f = open(peoplefile, 'rb')
#stored_people = pickle.load(f)
#for name, address in people.items():
    #print(stored_people)
p = person_info('Supto', 'Bogra',"01795776460")

p.tell()
