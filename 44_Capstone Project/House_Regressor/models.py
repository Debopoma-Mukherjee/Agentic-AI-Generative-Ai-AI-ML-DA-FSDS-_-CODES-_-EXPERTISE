import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (LinearRegression,Ridge,Lasso,ElasticNet,SGDRegressor,HuberRegressor )
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline 
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import pickle

data=pd.read_csv(r"C:\Users\91995\NIT\44_Capstone Project\USA_Housing.csv")
data

x=data.drop(['Price','Address'],axis=1)
y=data['Price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
models={
    "Linear Regression":LinearRegression(),
    "RobustRegression":HuberRegressor(),
    "Ridge Regression":Ridge(),
    "Lasso Regression":Lasso(),
    "ElasticNet":ElasticNet(),
    "Polynomial Regression":Pipeline([('poly', PolynomialFeatures(degree=4)),
                                     ('linear', LinearRegression())]),
    "SGDRegressor":SGDRegressor(),
    "ANN":MLPRegressor(hidden_layer_sizes=(100,),max_iter=1000),
    "Random Forest Regressor":RandomForestRegressor(),
    "SVM":SVR(),
    "LGBM":lgb.LGBMRegressor(),
    "XGBoost":xgb.XGBRegressor(),
    "KNN":KNeighborsRegressor(),   
}

results=[]

for name,model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)
    results.append({
        "Model":name,
        "MAE":mae,
        "MSE":mse,
        "R2_Score":r2
    })

    with open(f'{name}.pkl','wb') as f:
        pickle.dump(model,f)

results_df=pd.DataFrame(results)
results_df.to_csv('model_evaluation_results.csv',index=False)
print("Models have been trained and saved as pickle files.Evaluation results have been saved to model_evaluation_results.csv")