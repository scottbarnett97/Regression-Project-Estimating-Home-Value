# Zillow-Regression-Project

## Project description with goals
### Description
* We want to be able to predict the property tax assessed values ('taxvaluedollarcnt') of Single Family Properties that had a transaction during 2017

### Goals¶
* Construct an ML Regression model that predicts propery tax assessed values ('taxvaluedollarcnt') of Single Family Properties using attributes of the properties.

* Find the key drivers of property value for single family properties.
* Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.
* Make recommendations on what works or doesn't work in predicting these homes' values.

## Initial hypotheses and/or questions you have of the data, ideas
There should be some combination of features that can be used to build a predictive model for property values
* 1. Do any of 
* 2. Do 
* 3. Do 
* 4. Do 
*****************************************
** Project Plan 
*** Acquire data from Codeup DB Server
*** Prepare data
    **** Create Engineered columns from existing data
        ***** contract_types
        ***** customer_churn
        ***** customer_contracts
        ***** customer_details
        ***** customer_payments
        ***** customers
        ***** customer_signups
        ***** customer_subscriptions
        ***** internet_service_types
        ***** payment_types
*** Explore data in search of drivers of churn
    **** Answer the folowwing initial questions
        ***** 1. Do any of the demographic features provide relevant preditive value for churn?
        ***** 2. Do catagorical customer account features provide relevant predictive value for churn?
        ***** 3. Do numerical customer account features provide relevant predictive value for churn?
        ***** 4. Do any of the service features provide relevant predictive value for churn? 
*** Develop a model to predict if a customer will churn
*** Draw conclusions

## Data Dictionary

|Target|Datatype|Key|Definition
|:-------|:-------|:-------|:----------|
|churn|  int64| 1 = Yes <br /> 0 = No| has customer churned|

|Feature|Datatype|Key|Definition|
|:------- |:-------|:-------|:----------|
|customer_id                        | object | Unique   | identifier for each individual customer's account|
|senior_citizen                     | int64  | 1 = Yes  <br />0 = No    | is senior citizen|
|tenure                             | int64  | Months   | how long a customer has been utilizing telco services|
|monthly_charges                    | float64|  in USD  | how much a customer pays per month|
|total_charges                      | float64|  in USD  | how much a customer has paid since account opening|
|gender_Male                        | int64  | 1 = Male <br />0 = Female| gender|
|partner_Yes                        | int64  | 1 = Yes  <br />0 = No| has a significant other|
|has_dependents                     | int64  | 1 = Yes  <br />0 = No| has children|
|has_phone_service                  | int64  | 1 = Yes  <br />0 = No| has phone service with telco|
|multiple_lines_Yes                 | uint8  | 1 = Yes  <br />0 = No| has multiple phone lines|
|online_security_Yes                | uint8  | 1 = Yes  <br />0 = No| utilizes online security services|
|online_backup_Yes                  | uint8  | 1 = Yes  <br />0 = No| has online backup services via telco|
|device_protection_Yes              | uint8  | 1 = Yes  <br />0 = No| has device protection via telco|
|tech_support_Yes                   | uint8  | 1 = Yes  <br />0 = No| has technical support services with telco|
|streaming_tv_Yes                   | uint8  | 1 = Yes  <br />0 = No| has tv streaming capabilities with their account|
|streaming_movies_Yes               | uint8  | 1 = Yes  <br />0 = No| has movie streaming capabilities with their account|
|contract_type_One year             | uint8  | 1 = Yes  <br />0 = No| must renew their contract every year|
|contract_type_Two year             | uint8  | 1 = Yes  <br />0 = No| must renew their contract every two years|
|internet_service_type_Fiber optic  | uint8  | 1 = Yes  <br />0 = No| has fiber optic internet, 0: doesn't have fiber optic internet|
|internet_service_type_None         | uint8  | 1 = Yes  <br />0 = No| doesn't have internet service via telco|
|payment_type_Credit car (automatic)| uint8  | 1 = Yes  <br />0 = No| makes payments via automatic credit card transfer|
|payment_type_Electronic check      | uint8  | 1 = Yes  <br />0 = No| makes payments via electronic checks|
|payment_type_Mailed check          | uint8  | 1 = Yes  <br />0 = No| makes payments via mailed in checks|

##Steps to Reproduce
* 1.Clone this repo.
* 2.Acquire the data from Codeup DB Server
* 3.Put the data in the file containing the cloned repo.
* 4.Run notebook.

## Takeaways and Conclusions
* Of the features examined these provided statiscally relevant predictive value for predicting customer churn
** Account features
*** tenure
*** monthly_charges
** Demographic features
*** partner_Yes
*** dependents_Yes
** Other features
*** tech_support_Yes
*** internet_service_type_fiber_optic
*** payment_type_electronic_check
*Three major drivers
** Customers with Fiber Optic Internet Service churn faster than others
** Customers without Tech support turn at a higher rate than those with it
** Legacy customers are less likly to churn than newer customers

# Recomendations
* Implement the model provided and work with the marketing to form retention programs to reduce the churn rate for the company.
* These programs can be offered to seperate test markets derived from this model and later be evaluated to determine which retention program works best
* Investigate reason for fiber optic customers without tech support churning faster than others