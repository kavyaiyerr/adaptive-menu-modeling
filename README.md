# adaptive-menu-modeling
Created a cognitive model in ACT-R to model the impact of adaptive menus (similar to classic 2000-era Windows) on user performance/behavior. Designed an experiment using Python to run the model on.

Model Description (final-model.lisp):
The model I implemented involves learning the position of the menu items using declarative chunks and associating them to its visual location. For each trial of the experiment, the model is given an item to find and attempts to retrieve the location from memory. If the retrieval fails, it then begins to search each menu item individually, beginning with the top-most one, until it finds the desired item. It then clicks on the appropriate button, and stores that item as well as its visual location in memory. If the retrieval was successful, the model goes to the visual-location stored in memory and checks if the item in that position matches the item associated with that location in memory, which is the target. If they do not match, the model begins searching each menu item individually the same way it would in the case of a retrieval failure. If they do match, the model clicks the appropriate button and that chunk in memory is reinforced.

Experiment Design (finalproject.py):
The independent variable being manipulated is the menu condition that the model is being presented with. There are three different conditions: control, fixed, and adaptive. Each condition is made up of 3 blocks of 40 trials. In the control condition, each of the four characters appears as the target in equal proportion (each character is the target for 10 trials), and the order of the menu items in the menu itself does not change over the course of the 40 trials. In the fixed condition, each of the four characters are randomly assigned to different proportions in terms of the frequency at which they appear as the target, but the order of the menu items in the menu still does not change over the course of each set of 40 trials. For the fixed and adaptive conditions, the different proportions for the target frequency are as follows (50% of the trials, 25% of the trials, 15% of the trials, 10% of the trials). In all the conditions, the order of appearance of the items in the menu is random. 
Since the letters' frequencies are randomized in the fixed and adaptive conditions, this results in the final reaction times effectively ignoring the frequency of the items when averaged over multiple runs (since a given letter will be averaged over its presentations with different frequencies). To analyze the potential effect that frequency of a menu item may have, I also created fixed and adaptive conditions of the experiment where each letter appears as the target at the same frequency across all the trials ( ‘a’ = 50%, ‘b’ = 25%, ‘c’ = 15%, ‘d’ = 10%), but the menus are still shuffled at the start so that they aren't always located in the same start positions.
The dependent variable is the model’s reaction time to find the target in each trial of each condition. 

