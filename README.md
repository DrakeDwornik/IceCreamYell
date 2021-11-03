# IceCreamYell
a mystery dataset. what does it tell you?

The point of this lab is to examine a dataset (ice_cream.csv) and figure out what you can discover about it. 
You may have to research what terms are used in its description. (what's a dependent variable? predictor?)

Read the files presented here in the repo, esp the Ice_cream_data_description.rtf
What can you learn about the terms in the RTF. What do they mean.

Examine this data set. Load it into a python script and try to run some stat measures against it.

What interesting things can you discover about this data?

Things to Consider before starting
- How would you read it into memory using python?
- What data structure would you use to handle the data?
- What statistical measures might be helpful in understanding what the data is?
- Can you see any relationships between the various columns?
- Do test scores and gender indicate anything about what kind of ice cream a person favors?

*Finally*: What can you do to present / communicate what you discovered about this dataset?

You might wish to use some functions from https://docs.python.org/3/library/statistics.html

# File Notes
This page shows an example of a multinomial logistic regression analysis with footnotes explaining the output. The data were collected on 200 high school students and are scores on various tests, including a video game and a puzzle. The outcome measure in this analysis is the student’s favorite flavor of ice cream – vanilla, chocolate or strawberry- from which we are going to see what relationships exists with video game scores (**video**), puzzle scores (**puzzle**) and gender (**female**). 

|**Variable Name**|**Variable**|**Data type|
|---|---|---|
|**Id**|Identity of the student|Nominal|
|**female**|Fender (0: Male, 1: Female)|Binary|
|**ice_cream**|Favorite Flavor (1: Vanilla, 2: Chocolate, 3: Strawberry)| Nominal|
|**video**|Score on the video game|Scale/Continuous|
|**puzzle**|Score on the puzzle|Scale/Continuous|

**ice_cream** is the **dependent** variable (the **predicted** variable).
**female**, **video** and **puzzle** are the independent variables (the **predictors**).