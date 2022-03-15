import pandas as pd 
from IPython.display import YouTubeVideo

def cd_screener():
    """This is the function that starts the conduct disorder screening tool. 
    By typing anything as input, the user would be able to start the test. 
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    
    # prints out introduction and inputs anything to start the first question
    intro = input("""Hello! Thank you for taking the time to participate 
in this conduct discorder (CD) screening tool.
If you suspect that your child is struggling with conduct disorder, 
please answer these questions below by typing the number 1-5. 
\nPlease note that this screening tool is not meant to provide a diagnosis, 
but rather an assessment that could determine if your child might need 
to consult a health professional for further information or treatment.
\n\nType anything to continue\n""")
    
    # initializes score to 0
    score = {"score" : 0}
    
    # receives user's input (integer of 1-5) and adds them to the total score
    q1 = int(input("""\nDoes your child have protruding thoughts and urges to hurt other people or animals? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))

    def question1(q1):
        """Provides a question and asks for the user's input (integer) based on the multiple choice options.
        Then it transitions to the next question. The scores will add up based on the user's input. 
        
        Parameters
        ----------
        q1 : int or str
            Input of user's answer, integer of 1-5.
            
        Returns
        -------
        none
        """
        
        if q1 == 1:
            score["score"] += 1
        elif q1 == 2:
            score["score"] += 2
        elif q1 == 3:
            score["score"] += 3
        elif q1 == 4:
            score["score"] += 4
        elif q1 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""") 
    
    question1(q1)
            
    q2 = int(input("""\nHas your child engaged in behaviors of theft or vandalism? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))
    
    def question2(q2):
        if q2 == 1:
            score["score"] += 1
        elif q2 == 2:
            score["score"] += 2
        elif q2 == 3:
            score["score"] += 3
        elif q2 == 4:
            score["score"] += 4
        elif q2 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""")
    
    question2(q2)
          
    q3 = int(input("""\nDoes your child find themselves lying to or manipulating others a lot? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))
    
    def question3(q3):
        if q3 == 1:
            score["score"] += 1
        elif q3 == 2:
            score["score"] += 2
        elif q3 == 3:
            score["score"] += 3
        elif q3 == 4:
            score["score"] += 4
        elif q3 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""")
    
    question3(q3)

    q4 = int(input("""\nHas your child ever ran away from home or school? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))
    
    def question4(q4):
        if q4 == 1:
            score["score"] += 1
        elif q4 == 2:
            score["score"] += 2
        elif q4 == 3:
            score["score"] += 3
        elif q4 == 4:
            score["score"] += 4
        elif q4 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""")
    
    question4(q4)

    q5 = int(input("""\nDoes your child have trouble performing well in school and blame others for their poor performance? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))
    
    def question5(q5):
        if q5 == 1:
            score["score"] += 1
        elif q5 == 2:
            score["score"] += 2
        elif q5 == 3:
            score["score"] += 3
        elif q5 == 4:
            score["score"] += 4
        elif q5 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""")
    
    question5(q5)
        
    q6 = int(input("""\nDoes your child have trouble showing emotion towards others? 
    \n 1. Never \n 2. Rarely \n 3. Sometimes \n 4. Often \n 5. Very Often \n"""))
    
    def question6(q6):
        if q6 == 1:
            score["score"] += 1
        elif q6 == 2:
            score["score"] += 2
        elif q6 == 3:
            score["score"] += 3
        elif q6 == 4:
            score["score"] += 4
        elif q6 == 5:
            score["score"] += 5
        else:
            print("""\nYour total score would not be accurate as your input is not between the number 1-5.
            \nPlease restart the test.""")
    
    question6(q6)
    
    def result():
        """Prints out the result of the user's assessment of conduct disorder based 
        on the sum of their score, in the form of a string.
        
        Parameters
        ----------
        none
            
        Returns
        -------
        none
        """
        
        #calculates the total score and prints out the likelihood of conduct disorder
        if score["score"] >= 22 and score["score"] <= 30:
            print("\nIt was found that the total score of your screening test was " + str(score["score"]) + """ out of 30. 
            \nThis indicates that your child is\033[1m \033[91m VERY \033[0m likely to have conduct disorder.""")
        elif score["score"] >= 14 and score["score"] <= 21:
            print("\nIt was found that the total score of your screening test was " + str(score["score"]) + """ out of 30. 
            \nThis indicates that your child is\033[1m \033[91m CONSIDERABLY \033[0m likely to have conduct disorder.""")
        elif score["score"] >= 6 and score["score"] <= 13:
            print("\nIt was found that the total score of your screening test was " + str(score["score"]) + """ out of 30. 
            \nThis indicates that your child is\033[1m \033[91m NOT \033[0m likely to have conduct disorder.""")
        
    result()

def get_help():
    """The function provides a table of treatment options and a video if the user chooses yes.
    If the user chooses no it will print out an outro string.
    To align the dataframe text to the left, I got information from an external source:
    https://www.geeksforgeeks.org/align-columns-to-left-in-pandas-python/
    To add a youtube video, I followed a tutorial on youtube:
    https://www.youtube.com/watch?v=Gx1I_J_Y_Is&vl=en-US
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    
    # gives user option to receive more information or not
    # if yes, gives out more information in the form of a dataframe table and video
    # makes dataframe text aligned on the left
    #if no, prints out an outro message
    info = input("""\nGetting help is always possible. 
            \nTo find additional information and assistance for you or 
            \nyour child regarding conduct disorder, there are a number of resources available. 
            \nWould you like to look into this? Type yes or no.\n""")
    video = YouTubeVideo("EUCIKfNINYU")
    treatment_info = {"Treatment Options" : 
                    ["Cognitive behavioral therapy", "Family therapy", 
                    "Group therapy", "School support", "Medication"]}
    df = pd.DataFrame(treatment_info, index=['1','2','3','4','5'])
    left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
    left_aligned_df = left_aligned_df.set_table_styles(
    [dict(selector = 'th', props=[('text-align', 'left')])])
    
    if info.lower() == "yes":
        print("\nGreat! Here are some resources/treatments that you could consider:")
        display(left_aligned_df)
        print("\nHere is also a video that could provide more information about the disorder:")
        display(video)
        print("""\nIf you wish to receive a more detailed or specific information and diagnosis for your child, 
        \nplease consider contacting a mental health professional. Thank you!""")
    elif info.lower() == "no":
        print("\nAlright! Thank you for using our conduct disorder screening tool.")
        
cd_screener()       
get_help()