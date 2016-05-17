import numpy as np
from sklearn import svm, preprocessing
import pandas as pd

FEATURES =  ['(+ve word count) ',
             '(-ve word count)' ,
             '(overall polarity)' ,
             '(times change in pol)' ,
             '(largest + cont)' ,
             '(largest - cont)' ,
             '(capital letters)' ,
             '(punctuation)',
             'emoji_count',
             'laughter_exp_count']

def Build_Data_Set():
    data_df = pd.DataFrame.from_csv("data10.csv",encoding="utf-8-sig")
    #print(data_df.columns)
    #data_df = data_df[:100]

    X = np.array(data_df[FEATURES].values)#.tolist())

    y = (data_df["label"]
         .values.tolist())

    X = preprocessing.scale(X)

    return X,y

def Analysis():

    test_size = 1061
    X, y = Build_Data_Set()
    print(len(X))


    clf = svm.SVC(kernel="rbf", C= 0.75)
    clf.fit(X[:-test_size],y[:-test_size])

    correct_count = 0
    tp,fp,fn=0,0,0
    for x in range(1, test_size+1):
        pred=clf.predict(X[-x])[0]
        if pred == y[-x]:
            correct_count += 1
        if pred==1 and y[-x]==1:
            tp+=1
        if pred==1 and y[-x]==0:
            fp+=1
        if pred==0 and y[-x]==1:
            fn+=1

    precision=(tp/(tp+fp))
    recall=(tp/(tp+fn))
    print("Accuracy:", (correct_count/test_size) * 100.00)

    print("Precision:", precision * 100.00)

    print("Recall:",  recall * 100.00)

    print("F-score:", (2*precision*recall)/(precision+recall) * 100.00)

Analysis()