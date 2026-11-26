from sklearn.metrics import confusion_matrix

truth = [1, 0, 1, 0, 1, 0, 1, 1]
pred = [1, 0, 0, 0, 1, 1, 1, 0]

tp = 0
fp = 0
fn = 0
tn = 0

for actual, predicted in zip(truth, pred):
    if actual == 1 and predicted == 1:
        tp = tp + 1
    elif actual == 0 and predicted == 1:
        fp = fp + 1
    elif actual == 1 and predicted == 0:
        fn = fn + 1
    else:
        tn = tn + 1
assert (tp, fp, fn, tn) == (3, 1, 2, 2)

accuracy = (tp + tn) / len(truth)
precision = tp / (tp + fp)
recall = tp /(tp + fn)
print("accuracy:", accuracy)
print("precision:", precision)
print("recall:", recall)
print(confusion_matrix(truth, pred))
