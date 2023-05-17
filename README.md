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
* 1. Dose the county of the poperty provide relevant predicting tax value?
* 2. Does the number of bedrooms provide predictive value for churn? 
* 3. Does the number of bathrooms provide relevant predictive value tax value?
* 4. Does the size of the lot provide predictive value for tax value? 
*****************************************
** Project Plan 
*** Acquire data from Codeup DB Server
*** Prepare data
    **** Create Engineered columns from existing data
        ***** county_LA
        ***** county_Orange
        ***** county_Ventura
        ***** evaluate database to tidy up 
        ***** address any outliers
*** Explore data in search of drivers of property tax value
    **** Answer the following initial questions
        ***** 1. Does the county of the poperty and area of the home provide relevant predicting tax value?
        ***** 2. Does the number of bedrooms provide predictive value for tax value?
        ***** 3. Does the number of bathrooms provide relevant predictive value tax value?
        ***** 4. Does the size of the lot provide predictive value for tax value? 
*** Develop a model to predict tax value of properties
*** Draw conclusions

## Data Dictionary
| Feature | Datatype | Key | Definition |
|---|---|---|---|
| county | object | Unique | labels each county from fips |
| taxvalue | int64 | in USD | tax assessed value of property |
| bedrooms | int64 | # rooms | number of bedrooms in property |
| bathrooms | int64 | # rooms | number of bathrooms |
| area | int64 | in Sqft | area of property structure |
| lot | int64 | in Sqft | area of property lot |
| county_LA | unit8 | 1 = Yes  <br>0 = No | is county LA |
| county_Orange | unit8 | 1 = Yes  <br>0 = No | is county Orange |
| county_Ventura | unit8 | 1 = Yes  <br>0 = No | is county Ventura |

## Steps to Reproduce
* 1. Clone this repo.
* 2. Acquire the data from Codeup DB Server
* 3. Put the data in the file containing the cloned repo.
* 4. Run notebook.

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