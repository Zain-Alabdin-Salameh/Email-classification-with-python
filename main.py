from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import svm
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import Qt
from AlphaDarkTable import Ui_MainWindow
import sys
import csv

#____________________________________________________Start making table model to put data on it_______________________________________________________________
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()
#____________________________________________________end table model_______________________________________________________________
        





#____________________________________________________Start preparing data_______________________________________________________________
df = pd.read_csv("spamham1.csv", encoding="ISO-8859-1") # importing csv file as a pandas data frame 
data_set= df.where((pd.notnull(df)), '')# putting empty string instead of null value in the data frame ........cleaning data


data_set.loc[data_set["Category"] == 'ham', "Category",] = 1 # put 1 instead of ham in the data frame and 0 instead of spam
data_set.loc[data_set["Category"] == 'spam', "Category",] = 0


email = data_set['Message']
classs= data_set['Category']

train_email,test_email,train_classs, test_classs = train_test_split(email ,classs ,train_size=0.8, test_size=0.2 , random_state=4) # splitting data into training data and testing data

vectorizer=TfidfVectorizer(min_df=1,stop_words='english',lowercase=True) # vectorizer
classing=svm.LinearSVC()

train_email_vect = vectorizer.fit_transform(train_email) # putting training data into the vectorizer before use the svm classefire
test_email_vect=vectorizer.transform(test_email) # putting testing data into the vectorizer before use the svm classefire
y_trainSvm = train_classs.astype('int')
y_testSvm = test_classs.astype('int')

classing.fit(train_email_vect , y_trainSvm) # using svm classefire on training data to train the neural network

#___________________________________________________________preparing testing data to test the algorithm on it and putt it in the table to display_____________________________
test_result=[classing.predict(i) for i in test_email_vect]
testing_data={"message":test_email,"category":test_result}
testingTable=pd.DataFrame.from_dict(testing_data)
testingTable.loc[testingTable["category"] == 1, "category",] = "ham"
testingTable.loc[testingTable["category"] == 0, "category",] = "spam"
print(testingTable)


Accuracy=classing.score(test_email_vect,y_testSvm) # calculating the accuracy of the classefire

print(Accuracy)

# running qt widget inside the app
app = QtWidgets.QApplication(sys.argv) 
model=TableModel(testingTable)
window=QtWidgets.QMainWindow()
ui=Ui_MainWindow(window,model,Accuracy)
window.show()
app.exec_()