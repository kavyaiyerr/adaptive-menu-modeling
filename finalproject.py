# ACT-R final project.
# This experiment presents a model with a list of menu items
# and the model must find the correct menu item.
# There are three conditions for the menus: control, fixed position and adaptive
# The time the model took to find the items for each condition will be
# recorded and compared.

# Import the actr module for tutorial tasks

import actr

# Import the random module for tutorial tasks
import random

# Load the corresponding model for the task.

actr.load_act_r_model("ACT-R:tutorial;finalproject;final-model.lisp")

# Global variables to hold the information about the
# current trial information.
window = None
visible = False
response = None
#an array where the each index stores the menu item and the count of how many times that menu item appeared
menu_items = [['a', 0], ['b', 0], ['c', 0], ['d', 0]]

def move_model_cursor(x,y):
    actr.call_command("change-cursor-position",x,y)

def button_clicked():
    global response
    response = actr.get_time(True) 
        
actr.add_command('button_clicked',button_clicked)

# build_display is for the control and fixed conditions
def build_display():
    global window
    #put the menu items in a random order
    random_order = random.sample(menu_items, len(menu_items))

    #add the menu items for the participants to press in the window in that random order
  
    actr.add_button_to_exp_window(window, text=random_order[0][0], x=50, y=23, height=24, width=40, action="button_clicked")
    actr.add_button_to_exp_window(window, text=random_order[1][0], x=50, y=48, height=24, width=40, action="button_clicked")
    actr.add_button_to_exp_window(window, text=random_order[2][0], x=50, y=73, height=24, width=40, action="button_clicked")
    actr.add_button_to_exp_window(window, text=random_order[3][0], x=50, y=98, height=24, width=40, action="button_clicked")

# build_display_adaptive is for the adaptive conditions, where the order of the display depends on the count of the menu items
def build_display_adaptive():
        global window
        #reorder the menu item list depending on their count (highest to lowest)
        count_order = menu_items.copy()
        count_order.sort(key = lambda x: x[1]) #sort the list based on the second element of each sublist

        #add the menu items for the participants to press in the window in that order based on the count
        actr.add_button_to_exp_window(window, text=count_order[0][0], x=50, y=23, height=24, width=40, action="button_clicked")
        actr.add_button_to_exp_window(window, text=count_order[1][0], x=50, y=48, height=24, width=40, action="button_clicked")
        actr.add_button_to_exp_window(window, text=count_order[2][0], x=50, y=73, height=24, width=40, action="button_clicked")
        actr.add_button_to_exp_window(window, text=count_order[3][0], x=50, y=98, height=24, width=40, action="button_clicked")

# runs the control version of the experiment
def control():
    global response
    #randomly distribute the order of each of the target items (each item appears 10 times)
    trial_list = []

    #dict to store reaction time for each trial
    time_dict = {}

    #list of tuples to store the target and its average reaction time across the trials
    avg_time_dict = {}

    for i in range (10):
         for x in ['a', 'b', 'c', 'd']:
              trial_list.append(x)
    random.shuffle(trial_list)
    
    #open window
    window = actr.open_exp_window("Adaptive Menu Task",visible=visible,width=600,height=400)
    actr.install_device(window)
    
    #generate menu
    build_display()

    for j in range (len(trial_list)):
        target = trial_list[j]

        #display target info
        text = actr.add_text_to_exp_window (window, target, x=10, y=10)

        move_model_cursor(300,300)
        start = actr.get_time(True) # True is model time and you'd use False if getting human time
        response = False
        actr.run(120,visible) # some time long enough to always complete the task
        
        #keep track of response times
        if response:  #safety check
            trial_time = response - start
            if target in time_dict:
                time_dict[target].append(trial_time)
            else:
                time_dict[target] = [trial_time]
        
        actr.remove_items_from_exp_window(window, text)

    #find the average reaction time for each target across the trials
    avg_time_dict['a'] = sum(time_dict['a'])/10
    avg_time_dict['b'] = sum(time_dict['b'])/10
    avg_time_dict['c'] = sum(time_dict['c'])/10
    avg_time_dict['d'] = sum(time_dict['d'])/10

    
    return avg_time_dict


# runs the fixed version of the experiment
def fixed():
    global response

    trial_list = []

    #dict to store reaction time for each trial
    time_dict = {}

    #list of tuples to store the target and its average reaction time across the trials
    avg_time_dict = {}

    menu_options = ['a', 'b', 'c', 'd']

    #randomly choose which menu item appears at each frequency
    random.shuffle(menu_options)
    for a in range (20):
        trial_list.append(menu_options[0])
    for b in range (10):
        trial_list.append(menu_options[1])
    for c in range (6):
        trial_list.append(menu_options[2])
    for d in range (4):
        trial_list.append(menu_options[3])

    #randomly distribute the items across the trials
    random.shuffle(trial_list)
    
    #open window 
    window = actr.open_exp_window("Adaptive Menu Task",visible=visible,width=600,height=400)
    actr.install_device(window)
    #generate menu
    build_display()

    for j in range (len(trial_list)):
        target = trial_list[j]

        #display target info
        text = actr.add_text_to_exp_window (window, target, x=10, y=10)

        move_model_cursor(300,300)
        start = actr.get_time(True) # True is model time and you'd use False if getting human time
        response = False
        actr.run(120,visible) # some time long enough to always complete the task
        
        #keep track of response times
        if response:  #safety check
            trial_time = response - start
            if target in time_dict:
                time_dict[target].append(trial_time)
            else:
                time_dict[target] = [trial_time]

        actr.remove_items_from_exp_window(window, text)
    
    #find the average reaction time for each target across the trials
    avg_time_dict[menu_options[0]] = sum(time_dict[menu_options[0]])/20
    avg_time_dict[menu_options[1]] = sum(time_dict[menu_options[1]])/10
    avg_time_dict[menu_options[2]] = sum(time_dict[menu_options[2]])/6
    avg_time_dict[menu_options[3]] = sum(time_dict[menu_options[3]])/4


    return avg_time_dict

# runs the adaptive version of the experiment
def adaptive():
    global response

    trial_list = []

    #dict to store reaction time for each trial
    time_dict = {}

    #dict to store the target and its average reaction time across the trials
    avg_time_dict = {}

    menu_options = ['a', 'b', 'c', 'd']

    #randomly choose which menu item appears at each frequency
    random.shuffle(menu_options)
    for a in range (20):
        trial_list.append(menu_options[0])
    for b in range (10):
        trial_list.append(menu_options[1])
    for c in range (6):
        trial_list.append(menu_options[2])
    for d in range (4):
        trial_list.append(menu_options[3])

    #randomly distribute the items across the trials
    random.shuffle(trial_list)

    for j in range (len(trial_list)):
        target = trial_list[j]

        #open window 
        window = actr.open_exp_window("Adaptive Menu Task",visible=visible,width=600,height=400)
        actr.install_device(window)
        
        #generate menu
        build_display_adaptive()

        #display target info
        actr.add_text_to_exp_window (window, target, x=10, y=10)

        move_model_cursor(300,300)
        start = actr.get_time(True) # True is model time and you'd use False if getting human time
        response = False
        actr.run(120,visible) # some time long enough to always complete the task
        
        #keep track of response times
        if response:  #safety check
            trial_time = response - start
            if target in time_dict:
                time_dict[target].append(trial_time)
            else:
                time_dict[target] = [trial_time]
        
        #update count associated with the target for the specific trial
        if target == 'a':
            menu_items[0][1] += 1
        if target == 'b':
            menu_items[1][1] += 1
        if target == 'c':
            menu_items[2][1] += 1
        if target == 'd':
            menu_items[3][1] += 1

    #find the average reaction time for each target across the trials
    avg_time_dict[menu_options[0]] = sum(time_dict[menu_options[0]])/20
    avg_time_dict[menu_options[1]] = sum(time_dict[menu_options[1]])/10
    avg_time_dict[menu_options[2]] = sum(time_dict[menu_options[2]])/6
    avg_time_dict[menu_options[3]] = sum(time_dict[menu_options[3]])/4

    return avg_time_dict

# runs the fixed version of the experiment where frequency of each target item is controlled
def fixed_frequency():
    global response

    trial_list = []

    #dict to store reaction time for each trial
    time_dict = {}

    #list of tuples to store the target and its average reaction time across the trials
    avg_time_dict = {}

    menu_options = ['a', 'b', 'c', 'd']

    #manually assign which menu item appears at each frequency
    for a in range (20):
        trial_list.append(menu_options[0])
    for b in range (10):
        trial_list.append(menu_options[1])
    for c in range (6):
        trial_list.append(menu_options[2])
    for d in range (4):
        trial_list.append(menu_options[3])

    #randomly distribute the items across the trials
    random.shuffle(trial_list)
    
    #open window 
    window = actr.open_exp_window("Adaptive Menu Task",visible=visible,width=600,height=400)
    actr.install_device(window)
    #generate menu
    build_display()

    for j in range (len(trial_list)):
        target = trial_list[j]

        #display target info
        text = actr.add_text_to_exp_window (window, target, x=10, y=10)

        move_model_cursor(300,300)
        start = actr.get_time(True) # True is model time and you'd use False if getting human time
        response = False
        actr.run(120,visible) # some time long enough to always complete the task
        
        #keep track of response times
        if response:  #safety check
            trial_time = response - start
            if target in time_dict:
                time_dict[target].append(trial_time)
            else:
                time_dict[target] = [trial_time]

        actr.remove_items_from_exp_window(window, text)
    
    #find the average reaction time for each target across the trials
    avg_time_dict[menu_options[0]] = sum(time_dict[menu_options[0]])/20
    avg_time_dict[menu_options[1]] = sum(time_dict[menu_options[1]])/10
    avg_time_dict[menu_options[2]] = sum(time_dict[menu_options[2]])/6
    avg_time_dict[menu_options[3]] = sum(time_dict[menu_options[3]])/4


    return avg_time_dict

# runs the adaptive version of the experiment where the frequency of each target item is controlled
def adaptive_frequency():
    global response

    trial_list = []

    #dict to store reaction time for each trial
    time_dict = {}

    #dict to store the target and its average reaction time across the trials
    avg_time_dict = {}

    menu_options = ['a', 'b', 'c', 'd']

    #randomly choose which menu item appears at each frequency
    for a in range (20):
        trial_list.append(menu_options[0])
    for b in range (10):
        trial_list.append(menu_options[1])
    for c in range (6):
        trial_list.append(menu_options[2])
    for d in range (4):
        trial_list.append(menu_options[3])

    #randomly distribute the items across the trials
    random.shuffle(trial_list)

    for j in range (len(trial_list)):
        target = trial_list[j]

        #open window 
        window = actr.open_exp_window("Adaptive Menu Task",visible=visible,width=600,height=400)
        actr.install_device(window)
        
        #generate menu
        build_display_adaptive()

        #display target info
        actr.add_text_to_exp_window (window, target, x=10, y=10)

        move_model_cursor(300,300)
        start = actr.get_time(True) # True is model time and you'd use False if getting human time
        response = False
        actr.run(120,visible) # some time long enough to always complete the task
        
        #keep track of response times
        if response:  #safety check
            trial_time = response - start
            if target in time_dict:
                time_dict[target].append(trial_time)
            else:
                time_dict[target] = [trial_time]
        
        #update count associated with the target for the specific trial
        if target == 'a':
            menu_items[0][1] += 1
        if target == 'b':
            menu_items[1][1] += 1
        if target == 'c':
            menu_items[2][1] += 1
        if target == 'd':
            menu_items[3][1] += 1

    #find the average reaction time for each target across the trials
    avg_time_dict[menu_options[0]] = sum(time_dict[menu_options[0]])/20
    avg_time_dict[menu_options[1]] = sum(time_dict[menu_options[1]])/10
    avg_time_dict[menu_options[2]] = sum(time_dict[menu_options[2]])/6
    avg_time_dict[menu_options[3]] = sum(time_dict[menu_options[3]])/4

    return avg_time_dict



#takes in the condition and runs the appropriate 40 trial experiment n times
def experiment(condition, n):
    actr.reset()
    #dictionary that holds the reaction times for each target in each block of 40 trials 
    reaction_times = {'a':[], 'b': [], 'c': [], 'd': []}
    #list of four tuples holding the overall average reaction times for each target
    overall_times = []
    if (condition == "control"):
        for i in range (n):
            avg_time_dict = control()
            #add each block reaction time to the dict
            reaction_times['a'].append(avg_time_dict['a'])
            reaction_times['b'].append(avg_time_dict['b'])
            reaction_times['c'].append(avg_time_dict['c'])
            reaction_times['d'].append(avg_time_dict['d'])
    if (condition == "fixed"):
        for i in range (n):
            avg_time_dict = fixed()
            #add each block reaction time to the dict
            reaction_times['a'].append(avg_time_dict['a'])
            reaction_times['b'].append(avg_time_dict['b'])
            reaction_times['c'].append(avg_time_dict['c'])
            reaction_times['d'].append(avg_time_dict['d'])
    if (condition == "adaptive"):
        for i in range (n):
            avg_time_dict = adaptive()
            #add each block reaction time to the dict
            reaction_times['a'].append(avg_time_dict['a'])
            reaction_times['b'].append(avg_time_dict['b'])
            reaction_times['c'].append(avg_time_dict['c'])
            reaction_times['d'].append(avg_time_dict['d'])

    #average the times across all the experiment blocks
    overall_times.append(('a', sum(reaction_times['a'])/n))
    overall_times.append(('b', sum(reaction_times['b'])/n))
    overall_times.append(('c', sum(reaction_times['c'])/n))
    overall_times.append(('d', sum(reaction_times['d'])/n))

    return overall_times
    
    
    





    


         
    
     
               
               
     

    