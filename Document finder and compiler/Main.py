import file_search
import GUI
import os 
import logging as lg
def main():
    g=GUI.Gui()
    s=file_search.search_engine()
    
    lg.basicConfig(filename='prod.log',level=lg.DEBUG,filemode='a',format='%(name)s - %(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    while True:
        event, values = g.window.read()
        try:  
            if event is None:
                try:
                    os.remove('search_results.txt')
                    break
                except:
                    break
            if event=='_INDEX_':
                s.create_new_index(values)
            if event=='_SEARCH_':
                if not 'file_index.pkl' in os.listdir():
                    GUI.sg.popup('Please select the correct root path and then re-index again!',title='Message')
                else:
                    s.search(values)
                    for result in s.results:
                        print(result)
                        print('There were {:,d} matches out of {:,d} records searched.'.format(s.matches,s.records))
        except Exception as e:
            mainl=lg.getLogger("main")
            mainl.info(e)

main()