# Welcome

__This is my repository file retracing the work done on my counterfeit banknote detection project for the ONCFM (National Office for the Fight against Counterfeit Currency in english)__

The subject was to manage to detect counterfeit banknotes in python, with a percentage of probability for each banknote.

There was only a data set of 1500 rows available with the following variables:

- diagonal : the diagonal of the banknote

- height_left : the left height of the banknote

- height_right : the right height of the banknote

- margin_low : the bottom margin of the banknote

- margin_up : the high margin of the banknote

- is_genuine : True or False to tell us if the banknotes are true or false.

__________________________________________________________________________________________________________

From this dataset, we have to build an adequate machine learning model in order to detect the veracity of a given banknote out of this initial dataset.

So I developed a script in python which has several outputs: 
- a logistic regression model to predict the value of the banknote (True or False) according to the different variables available.
- a csv file with the predictions
- a final dataset used depending on whether or not linear regression was applied to fill in empty cells that might be within the margin_low variable

I also developed following this script a web app thanks to streamlit, via jupyter notebook.

__________________________________________________________________________________________________________

The different data sources produced during this project are present under 'Source' in this repository.

The different parts of code produced during this project are present under 'Code' in this repository.

In order to allow you to test the web app yourself, you can access it at any time via this link:

##########################################################################

 https://kevinb-data-detection-billets-web-app-v2-c3vj01.streamlit.app/
 
##########################################################################

__________________________________________________________________________________________________________

You will need to download two files and drop them on the web app:

- 'dataframe_final_20220530.csv' (under the 'Sources' folder of this repository)
- 'modele_regression.joblib' (under the 'Code' folder of this repository)

Thanks to the prediction model and the web application, you can then use the buttons available to be able to find out if your banknote, according to the input values ​​you have assigned to it, is true or false.
