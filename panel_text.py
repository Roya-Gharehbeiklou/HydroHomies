from panel.pane import Markdown

### Home page

def home_info():
    text = '''
    #### Welcome to the Hydrohomies Dashboard
    On this webpage we want to share the results of our research into the relation between dehydration and cognitive funcitoning.  
    Below you find the abstract of our article. Via the buttons on the sidebar you can find more in-depth information about each cognitive test and our health parameters during testing.

    #### Abstract
    Water consumption is crucial for human life and survival. It is vital to have a balance between water loss and water consumption. If this balance is disturbed and a body loses more water than it consumes it is called dehydration (Greenleaf-1991, n.d.)]. Numerous experiments have researched the effects of dehydration on the cognitive abilities. However, most of these researches are focused on high-risk groups (Pross, 2017). Therefore, the aim of this study was to investigate the short-term effects of dehydration on different cognitive domains in adults. Dehydration was obtained by exercising in a sweatsuit, where the participants were not allowed to drink fluids. After dehydration was obtained, five cognitive domains were tested: learning and memory, language, perceptual-motor function, executive function, and complex attention. However, only a maximum of 1.2% dehydration (body-weight loss) was achieved using this method. Most of the time this mild dehydration did not seem to have a negative effect on the performance on the listed domains. However, various results were obtained per participant when looking at a specific domain.  In general, this work illustrates that achieving a dehydration level of at most 1.2% is not enough to significantly affect your mental abilities.
    '''
    return Markdown(text)
    
    
### FLANKER TEST
def flanker_info():
    text = '''
    In the flanker test the participant responds to a series of 50 stimuli by pressing ‘A’ on the keyboard, if the stimuli ‘X’ or ‘C’ are shown, or 'L’ if the stimuli ‘B’ and ‘V’ are shown.   
    Around this letter two flanking letters are shown on both sides, which might confuse the participant.  
    These flanking letters are X, C, B or V and thus sometimes match the stimuli and sometimes dont.  
    '''
    return text
    
def flanker_rt():
    text = '''
    In the flanker test it is expected that a participants reaction time increases when the participant is dehydrated.  
    As illustrated in the figur above, the orange and red participant show an increase in reaction time when dehydrated.  
    However, for the blue, green, and pink participant the hypothesis is not true.  
    '''
    return text
    
def flanker_corr():
    text = '''
    In the flanker test it is expected that a participant answer accarydecreases  when the participant is dehydrated, compared to the control.  
    For all the participants no significant change in the number of errors is detected, so the hypothesis is rejected, dehydration does not seem to affect the accuracy.  
    '''
    return text


## STROOP TEST
def stroop_info():
    text = '''
    In the stroop test there are  40 written colours of which the ink colour either matches the written word or does not.  
    The participant has to press a key on the keyboard according to the ink colour shown (red, green, yellow or blue).  
    '''
    return text

def stroop_rt():
    text = '''
    In the stroop test it was expected that the reaction time increases when a participant is dehydrated.  
    As shown in the barplot above, only the red participants' reaction time is significantly affected under the dehydration condition.  
    All the other participants did not seem to be affected by the dehydration.  
    '''
    return text

def stroop_corr():
    text = '''
    In the stroop test the accuracy (number of correct answers) is expected to decrease under the dehydration condition.  
    As can be seen in the barplot, the orange, pink and red participant show a slight decrease in number of correct answers.    
    Only the red  participant shows a statistically significant result, where it is negatively effected by the dehydration.  
    '''
    return text

## VERBAL FLUENCY 
def verbal_info():
    text = '''
    In the verbal fluency test the participant has 60 seconds to name as many English words starting with a letter, provided by the examiner.  
    This was done for a total of 3 times, where 2 letters are consonants and 1 letter is a vowel.  
    The amount of words is recorded 
    '''
    return text 

def verbal_corr():
    text = '''
    In the verbal fluency test we expected that the words a participant could say is negatively influenced by dehydration.  
    As expected, the number of words decreased in dehydration session for red and pink. This is illustrated in the figure above.  
    Orange and green participants' performance were only slightly negatively affected by losing water and there is a slight difference in their result.  
    The blue participant has the opposite performance, which is contradictory to the hypothesis.  
    '''
    return text

## DIGIT SPAN TEST
def digit_info():
    text = '''
    In the digit span test the participant must remember a sequence of digits.  
    First the sequence is shown, then the participant should repeat it by clicking the right numbers on the screen.  
    Initially, the sequence length is 2 and this increases when the participant remembered the sequence of that length correctly for 2 times in a row.  
    The test stops when the participant made a mistake in repeating the sequence 2 consecutive times.  
    '''
    return text

def digit_length():
    text = '''
    In the digit span test The memorized sequence length is expected to decrease if the participant is dehydrated.  
    As visualised in the barplot, all participants performed better or equal in the control sessions than in the dehydration sessions.  
    '''
    return text


## STOP SIGNAL TEST
def stop_info():
    text = '''
    In the stop signal test the participant has to respond to a left or right pointed arrow by pressing the right key.  
    Sometimes a red circle appears around the arrow, which means that the participant should not respond.  
    The participant has to stop his probably intialised response.  
    
    The test consists out of two phases:  
    - Training phase:  
    Consitst out of 50 stimili, the participant should respond to a left or right green pointing arrow by pressing the right key.  
    When a left arrow is shown, the ‘B’ key should be pressed and when a right arrow is shown, the ‘N’ key should be pressed. \n
    - Second phase:  
    Consists out of 40 stimuli,a red circle may appear around the arrow after the arrow is already shown.  
    If this red circle appears, the participant should not respond. 
    The time when this red circle is shown after the arrow appears, is 50, 100 or 450 ms.  
    '''
    return text

def stop_rt():
    text = '''
    In the stop signal test it was expected that the reaction time increases when the participant is dehydrated.  
    As can be seen in the barplot only one participant was negatively influenced by dehydration.  
    '''
    return text

def stop_corr():
    text = '''
    In the stop signal test it is expeced that the accuracy decreases when a participant is dehydrated.  
    As shown in the barplot, all participant but orange and red made fewer errors when dehydrated.  
    This is contradictory to the hypothesis.  
    '''
    return text


## HEALTH DATA

def health_info():
    text = '''
    In this section the health data can be explored:
    '''
    return text