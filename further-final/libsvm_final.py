from svmutil import *
from libsvm import *
y, x = svm_read_problem('D:\exp-proj\twitter2\further-final\libsvm_data')
m = svm_train(y[:4000], x[:4000], '-c 4')
p_label, p_acc, p_val = svm_predict(y[4000:], x[4000:], m)
print(p_label)
print(p_acc)