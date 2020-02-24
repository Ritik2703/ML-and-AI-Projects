import pandas as pd
import numpy as np
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Building a baseline model. Predicting Sales as overall average sales
# Determine mean of the output column:
mean_sales = train['Item_Outlet_Sales'].mean()
#Initialize submission dataframe with ID varaibles
base1 = test[['Item_Identifier','Outlet_Identifier']]
#Assign outcome variable to mean value:
base1['Item_Outlet_Sales'] = mean_sales
#Export submission:
base1.to_csv("submission_baseline1.csv",index=False)

# Predicted value minus actual value
mse = np.mean((base1['Item_Outlet_Sales'] - train['Item_Outlet_Sales'])**2)
rmse=np.sqrt(mse)
print('Score: {}'.format(rmse))