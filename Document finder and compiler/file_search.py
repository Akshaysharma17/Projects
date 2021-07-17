import os
import pickle
import logging as lg
import GUI as g
class search_engine:
    lg.basicConfig(filename='prod.log',level=lg.DEBUG,filemode='a',format='%(name)s - %(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    
    def __init__(self):
        self.file_index = []
        self.results = []
        self.matches = 0
        self.records = 0
    
    def create_new_index(self, values):
        
        try:
            root_path=values['PATH']
            self.file_index=[(roots,files) for roots,dirs,files in os.walk(root_path) if files]
            if not self.file_index:
                print("Please fill correct Root path field first")
            else:
                with open('file_index.pkl','wb') as f:
                    pickle.dump(self.file_index,f)
                g.sg.popup("Index has been created!")
        except Exception as e:
            index=lg.getLogger('create_new_index')
            index.debug(e)

    def load_existing_index(self):
        try:
            with open('file_index.pkl','rb') as f:
                self.file_index=pickle.load(f)
        
        except Exception as e:
            load_existing=lg.getLogger('Load_existing')
            self.file_index=[]
            load_existing.info(e)


    def search(self , values):                   
        self.results.clear()
        self.matches=0
        self.records=0
        term=values['TERM']
        self.load_existing_index()    
        for path,files in self.file_index:
            if (values['CONTAINS'] or
                values['STARTSWITH'] or 
                values['ENDSWITH']) is True:
                    for file in files:
                        self.records +=1
                        if (values['CONTAINS'] and term.lower() in file.lower() or
                            values['STARTSWITH'] and file.lower().startswith(term.lower()) or
                            values['ENDSWITH'] and file.lower().endswith(term.lower())):
                            result = path.replace('\\','/')+'/'+file
                            self.results.append(result)
                            self.matches+=1
                        else:
                            continue
            else:
                g.sg.popup("Please choose any option among Contains, Starts with, Ends with to proceed!",title='Message')
                break

        if not self.results:
            print('There were {:,d} matches out of {:,d} records searched.'.format(self.matches,self.records))
        else:
            with open ('search_results.txt','w') as f:
                for row in self.results:
                    f.write(row+'\n')
            
    



