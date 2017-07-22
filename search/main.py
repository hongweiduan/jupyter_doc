import csv 
import pickle
def got_data():
    tab =[]
    with open('data.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
        	for j in row[0].split(","):
    			tab.insert(-1,j)
                yield j        
    # print (len(tab))
    # return len(tab)
a = got_data()

def basis_of_search(row_data,y):
    if row_data == y:
        return 1
    else:
        return 0
print basis_of_search(next(a),3)


# pickle_file=open('csv_pkl','wb')  
# pickle.dump(tab,pickle_file) 
# pickle_file.close()

# f=open('csv_pkl','rb') 
# data=pickle.load(f) 
# print(len(data)) 