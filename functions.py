def plotRocCurves(gs, X_test, y_test, auc, roc_curve, plt):
    y_pred = gs.predict(X_test) 
    
    y_pred_low = [0 if x in [2, 3] else 1 for x in y_pred]
    y_test_low = [0 if x in [2, 3] else 1 for x in y_test]    
    
    y_pred_medium = [0 if x in [1, 3] else 1 for x in y_pred]
    y_test_medium = [0 if x in [1, 3] else 1 for x in y_test]
    
    y_pred_high = [0 if x in [1, 2] else 1 for x in y_pred]
    y_test_high = [0 if x in [1, 2] else 1 for x in y_test]
    
    plotRocCurve(y_test_low, y_pred_low, "low quality", auc, roc_curve, plt)
    plotRocCurve(y_test_medium, y_pred_medium, "medium quality", auc, roc_curve, plt)
    plotRocCurve(y_test_high, y_pred_high, "high quality", auc, roc_curve, plt)
    
def plotRocCurve(y_test, y_pred, quality_type, auc, roc_curve, plt):    
    
    fpr, tpr, threshold = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)

    plt.title('ROC - ' + quality_type)
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('true positive rate')
    plt.xlabel('false positive rate')
    plt.show()

def printStatistics(gs, X_test, y_test, precision_score, recall_score, f1_score, confusion_matrix):
    prediction = gs.predict(X_test)

    print('Accuracy  : {:.5f}'.format(gs.score(X_test, y_test)), sep = '\n')

    ##tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. 
    ##The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.
    print('Precision  : {:.5f}'.format(precision_score(y_test, prediction, average='micro')))
              
    ##tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. 
    ##The recall is intuitively the ability of the classifier to find all the positive samples.                     
    print('Recall  : {:.5f}'.format(recall_score(y_test, prediction, average='micro')))
                                
    ##F1 = 2 * (precision * recall) / (precision + recall)
    print('f1_score  : {:.5f}'.format(f1_score(y_test, prediction, average='micro')))
      
    print('Confusion matrix', confusion_matrix(y_test, prediction), sep = '\n')

    print('Best model parameters', gs.best_params_, sep = '\n')
