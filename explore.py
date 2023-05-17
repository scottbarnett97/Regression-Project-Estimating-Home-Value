# imports 
import warnings
warnings.filterwarnings("ignore")
# Tabular data friends:
import pandas as pd
import numpy as np
import math
# Data viz:
import matplotlib.pyplot as plt
import seaborn as sns


# Data acquisition
from pydataset import data
import scipy.stats as stats
import seaborn as sns
import numpy as np
import env
import os

# Sklearn stuff:
import sklearn

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

from sklearn.metrics import mutual_info_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score


from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix

# Project related
import acquire
import prepare
############################### exploration data visuals ##############################

def plot_regression(train):
    '''
    this feature brings in the lmplot for the counties to tax value
    '''
    sns.color_palette("magma")
    sns.lmplot(x="area", y="taxvalue", hue='county', data=train, scatter=True,scatter_kws={'alpha': 0.2}, line_kws={'linewidth': 3})
    plt.xlabel("Area in Sq.ft")
    plt.ylabel("Tax Value in USD millions")
    plt.title("Regression Plot: Area vs. Tax Value")
    plt.show()

def bed_chart(data):
    '''
    creates a scatter plot for bedrooms vs tax value
    '''
    # Specify the x and y variables
    x = data['bedrooms']
    y = data['taxvalue']
    # Create the scatter plot
    plt.scatter(x, y, alpha=0.5)
    # Set the labels and title
    plt.xlabel("Number of Bedrooms")
    plt.ylabel("Tax Value in millions USD")
    plt.title("Number of Bedrooms vs. Tax Value")
    # Display the chart
    plt.show()
    
def bath_chart(data):
    '''
    creates a scatter plot for bathrooms vs tax value
    '''
    # Specify the x and y variables
    x = data['bathrooms']
    y = data['taxvalue']
    # Create the scatter plot
    plt.scatter(x, y, alpha=0.5)
    # Set the labels and title
    plt.xlabel("Number of Bathrooms")
    plt.ylabel("Tax Value in millions USD")
    plt.title("Number of Bathrooms vs. Tax Value")
    # Display the chart
    plt.show()
    
def lot_chart(data):
    '''
    creates a scatter plot for lot vs tax value
    '''
    # Specify the x and y variables
    x = data['lot']
    y = data['taxvalue']
    # Create the scatter plot
    plt.scatter(x, y, alpha=0.5)
    # Calculate the best-fit line
    slope, intercept = np.polyfit(x, y, 1)
    best_fit_line = slope * x + intercept
    # Plot the best-fit line
    plt.plot(x, best_fit_line, color='red')
    # Set the labels and title
    plt.xlabel("Lot in Sqft")
    plt.ylabel("Tax Value in millions USD")
    plt.title("Lot vs. Tax Value with Best-Fit Line")
    # Display the chart
    plt.show()

###############################  satatistical tests ######################

def run_lattest(data):
    '''
    runs a Ttest for LA county vs tax value
    '''
    x = data['county_LA']
    y = data['taxvalue']
    # Perform t-test
    t_statistic, p_value = stats.ttest_ind(x, y)
    # Decide whether to reject the null hypothesis
    alpha = 0.05
    if p_value == alpha:
        decision = "Fail to Reject Null Hypothesis"
    else:
        decision = "Reject Null Hypothesis"
# Create a DataFrame to store the results
    results = pd.DataFrame({
        'T-Statistic': [t_statistic],
        'P-Value': [p_value],
        'Decision': [decision]})
    return results

def run_orangettest(data):
    '''
    runs a Ttest for orange county vs tax value
    '''
    x = data['county_Orange']
    y = data['taxvalue']
    # Perform t-test
    t_statistic, p_value = stats.ttest_ind(x, y)
    # Decide whether to reject the null hypothesis
    alpha = 0.05
    if p_value == alpha:
        decision = "Fail to Reject Null Hypothesis"
    else:
        decision = "Reject Null Hypothesis"       
# Create a DataFrame to store the results
    results = pd.DataFrame({
        'T-Statistic': [t_statistic],
        'P-Value': [p_value],
        'Decision': [decision]})
    return results    
    
def run_ventttest(data):
    '''
    runs a Ttest for Ventura county vs tax value
    '''
    x = data['county_Ventura']
    y = data['taxvalue']
    # Perform t-test
    t_statistic, p_value = stats.ttest_ind(x, y)
    # Decide whether to reject the null hypothesis
    alpha = 0.05
    if p_value == alpha:
        decision = "Fail to Reject Null Hypothesis"
    else:
        decision = "Reject Null Hypothesis"   
    # Create a DataFrame to store the results
    results = pd.DataFrame({
        'T-Statistic': [t_statistic],
        'P-Value': [p_value],
        'Decision': [decision]})
    return results    
    
def run_all_ttests(data):
    '''
    this feature runs all county T-tests and consolidates findings
    '''
    results = pd.DataFrame()  # Create an empty DataFrame to store the results
    # Run the T-tests for LA, Orange, and Ventura counties
    la_results = run_lattest(data)
    la_results['County'] = 'LA County'  # Add county name column
    orange_results = run_orangettest(data)
    orange_results['County'] = 'Orange County'  # Add county name column
    ventura_results = run_ventttest(data)
    ventura_results['County'] = 'Ventura County'  # Add county name column
    # Concatenate the results into a single DataFrame
    results = pd.concat([results, la_results, orange_results, ventura_results], ignore_index=True)
    return results

def get_areastats(data):
    '''
    This function reurns ther results from a pearsons r correlation test on area and tax value
    '''
    x_var='area'
    y_var='taxvalue'
    alpha=0.05
    # Perform Pearson correlation test
    r, p_value = stats.pearsonr(data[x_var], data[y_var])
    # Round p-value to 4 decimal places
    rounded_p_value = round(p_value, 4)

    # Evaluate p-value compared to alpha
    if rounded_p_value < alpha:
        evaluation = "Reject Null"
    else:
        evaluation = "Fail to Reject"
    results = {'x_variable': x_var, 'r': r, 'p_value': rounded_p_value, 'evaluation': evaluation}
    results_df = pd.DataFrame(results, index=[0])
    return results_df
  
def get_bedstats(data):
    '''
    this function runs a ttest on bedrooms to taxvalue
    '''
    x_var = 'bedrooms'
    y_var = 'taxvalue'
    alpha=0.05
    # Perform Pearson correlation test
    r, p_value = stats.pearsonr(data[x_var], data[y_var])
    # Round p-value to 4 decimal places
    rounded_p_value = round(p_value, 6)
    # Evaluate p-value compared to alpha
    if rounded_p_value < alpha:
        evaluation = "Reject Null"
    else:
        evaluation = "Fail to Reject"
    results = {'x_variable': x_var, 'r': r, 'p_value': rounded_p_value, 'evaluation': evaluation}
    results_df = pd.DataFrame(results, index=[0])
    return results_df   
  
def get_bathstats(data):
    '''
    this function runs a ttest on bathrooms to taxvalue
    '''
    x_var = 'bathrooms'
    y_var = 'taxvalue'
    alpha=0.05
    # Perform Pearson correlation test
    r, p_value = stats.pearsonr(data[x_var], data[y_var])
    # Round p-value to 4 decimal places
    rounded_p_value = round(p_value, 6)
    # Evaluate p-value compared to alpha
    if rounded_p_value < alpha:
        evaluation = "Reject Null"
    else:
        evaluation = "Fail to Reject"
    results = {'x_variable': x_var, 'r': r, 'p_value': rounded_p_value, 'evaluation': evaluation}
    results_df = pd.DataFrame(results, index=[0])
    return results_df    
    
def get_lotstats(data):
    '''
    This function reurns ther results from a pearsons r correlation test on lot and tax value
    '''
    x_var='lot'
    y_var='taxvalue'
    alpha=0.05
    # Perform Pearson correlation test
    r, p_value = stats.pearsonr(data[x_var], data[y_var])
    # Round p-value to 4 decimal places
    rounded_p_value = round(p_value, 4)

    # Evaluate p-value compared to alpha
    if rounded_p_value < alpha:
        evaluation = "Reject Null"
    else:
        evaluation = "Fail to Reject"
    results = {'x_variable': x_var, 'r': r, 'p_value': rounded_p_value, 'evaluation': evaluation}
    results_df = pd.DataFrame(results, index=[0])
    return results_df

        ################################ Modeling ####################################



def scale_data(train, validate, test, columns):
    """
    Scale the selected columns in the train, validate, and test data.
    Args:
        train (pd.DataFrame): Training data.
        validate (pd.DataFrame): Validation data.
        test (pd.DataFrame): Test data.
        columns (list): List of column names to scale.
    Returns:
        tuple: Scaled data as (X_train_scaled, X_validate_scaled, X_test_scaled).
    """
    # create X & y version of train, where y is a series with just the target variable and X are all the features.
    X_train = train.drop(['county','taxvalue'], axis=1)
    y_train = train['taxvalue']
    X_validate = validate.drop(['county','taxvalue'], axis=1)
    y_validate = validate['taxvalue']
    X_test = test.drop(['county','taxvalue'], axis=1)
    y_test = test['taxvalue']
    # Create a scaler object
    scaler = MinMaxScaler()
    # Fit the scaler on the training data for the selected columns
    scaler.fit(X_train[columns])
    # Apply scaling to the selected columns in all data splits
    X_train_scaled = X_train.copy()
    X_train_scaled[columns] = scaler.transform(X_train[columns])

    X_validate_scaled = X_validate.copy()
    X_validate_scaled[columns] = scaler.transform(X_validate[columns])

    X_test_scaled = X_test.copy()
    X_test_scaled[columns] = scaler.transform(X_test[columns])
    return X_train_scaled, y_train, X_validate_scaled, y_validate, X_test_scaled, y_test

def metrics_reg(y_true, y_pred):
    """
    Calculate RMSE and R2 scores.

    Args:
        y_true (array-like): True target values.
        y_pred (array-like): Predicted target values.

    Returns:
        tuple: Tuple containing RMSE and R2 scores.
    """
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    return rmse, r2


def get_baseline(y_true):
    """
    Calculate RMSE and R2 scores for the baseline model.

    Args:
        y_true (array-like): True target values.

    Returns:
        pd.DataFrame: DataFrame with baseline model metrics.
    """
    baseline = y_true.mean()
    baseline_array = np.repeat(baseline, len(y_true))
    rmse, r2 = metrics_reg(y_true, baseline_array)

    metrics_df = pd.DataFrame(data=[{
        'model': 'baseline',
        'rmse': rmse,
        'r2': r2
    }])

    return metrics_df


def get_blinemetrics(y_true):
    baseline_metrics = get_baseline(y_true)
    return baseline_metrics


 
  