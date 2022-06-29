import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

def evaulation_model(X_tr,X_te,y_tr,y_te,log=False):
    '''
    Write a good doc string.
    
    '''
    #Create and fit model
    model = sm.OLS(y_tr,sm.add_constant(X_tr)).fit()
    
    #print summary if ols
    print(model.summary())
    
    # grab predictions
    tr_preds = model.predict(sm.add_constant(X_tr))
    te_preds = model.predict(sm.add_constant(X_te))
    
    
    # exaluate on train and test
    print("*"*20)
    print(f"Train R2 Score: {r2_score(y_tr, train_preds):.4f}")
    if log == True:
        y_tr_unlog = np.expm1(y_tr)
        y_te_unlog = np.expm1(y_te)
        tr_preds_unlog = np.expm1(tr_preds)
        te_preds_unlog = np.expm1(te_preds)
        print(f"Train MAE Score: ${mean_absolute_error(y_tr_unlog, tr_preds_unlog):.4f}")
        print(f"Train RMSE Score: ${mean_squared_error(y_tr_unlog, tr_preds_unlog, squared=False):.4f}")
    else:
        print(f"Train MAE Score: ${mean_absolute_error(y_tr, train_preds):.4f}")
        print(f"Train RMSE Score: ${mean_squared_error(y_tr, train_preds, squared=False):.4f}")
    print("*"*20)
    print(f"Test R2 Score: {r2_score(y_te, test_preds):.4f}")
    if log == True:
        y_te_unlog = np.expm1(y_te)
        te_preds_unlog = np.expm1(te_preds)
        print(f"Test MAE Score: ${mean_absolute_error(y_te_unlog, te_preds_unlog):.4f}")
        print(f"Test RMSE Score: ${mean_squared_error(y_te_unlog, te_preds_unlog, squared=False):.4f}")
    else:
        print(f"Test MAE Score: ${mean_absolute_error(y_te, test_preds):.4f}")
        print(f"Test RMSE Score: ${mean_squared_error(y_te, test_preds, squared=False):.4f}")
        print("*"*20)  
    # visulize residuals
    plt.scatter(train_preds, y_tr-train_preds, label='Train')
    plt.scatter(test_preds, y_te-test_preds, label='Test')

    plt.axhline(y=0, color = 'red', label = '0')
    plt.xlabel('predictions')
    plt.ylabel('residuals')
    plt.legend()
    plt.show()
    
    return tr_preds, te_preds