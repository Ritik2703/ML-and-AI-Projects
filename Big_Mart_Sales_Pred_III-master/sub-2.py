#Predicting Outlest sales based on 
# - Item_Visibility
# - Item_MRP
# - Outlet_Establishment Year
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
train = pd.read_csv("train_modified.csv")
test = pd.read_csv("test_modified.csv")

#Define target and ID columns:
target = 'Item_Outlet_Sales'
IDcol = ['Item_Identifier','Outlet_Identifier']
Unusedcol = ['Outlet_Type','Outlet_Location_Type','Outlet_Size','Item_Fat_Content'
        ,'Item_Type','Item_Weight','Outlet_Size']
from sklearn import cross_validation, metrics
def modelfit(alg, dtrain, dtest, predictors, target, IDcol, filename):
    #Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain[target])
    #Predict training set:
    dtrain_predictions = alg.predict(dtrain[predictors])
    #Perform cross-validation:
    cv_score = cross_validation.cross_val_score(alg, dtrain[predictors], dtrain[target], cv=20, scoring='neg_mean_squared_error')
    cv_score = np.sqrt(np.abs(cv_score))
    
    #Print model report:
    print("\nModel Report")
    print("RMSE : %.4g" % np.sqrt(metrics.mean_squared_error(dtrain[target].values, dtrain_predictions)))
    print("CV Score : Mean - %.4g | Std - %.4g | Min - %.4g | Max - %.4g" % (np.mean(cv_score),np.std(cv_score),np.min(cv_score),np.max(cv_score)))
    
    #Predict on testing data:
    dtest[target] = alg.predict(dtest[predictors])
    
    #Export submission file:
    IDcol.append(target)
    submission = pd.DataFrame({ x: dtest[x] for x in IDcol})
    submission.to_csv(filename, index=False)

from sklearn.linear_model import LinearRegression, Ridge, Lasso
predictors = [x for x in train.columns if x not in [target]+IDcol]
# print predictors
# alg1 = LinearRegression(normalize=True)
# modelfit(alg1, train, test, predictors, target, IDcol, 'sub-3.csv')
# coef1 = pd.Series(alg1.coef_, predictors).sort_values()
# coef1.plot(kind='bar', title='Model Coefficients')
# Ridge Regression
alg2 = Ridge(alpha=0.05,normalize=True)
modelfit(alg2, train, test, predictors, target, IDcol, 'alg2.csv')
coef2 = pd.Series(alg2.coef_, predictors).sort_values()
coef2.plot(kind='bar', title='Model Coefficients')
#plot.show()