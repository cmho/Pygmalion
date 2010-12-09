# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    
    image bg convo = "images/bg.png"
    
    image current = "images/galatea/happy.png"
    
    image galatea default = "images/galatea/happy.png"
    
    image bg white = "#FFFFFF"
    
    # Common (and some uncommon) pronoun sets
    # identified by the nominative for easy lookup because that's what I ask you to enter at the beginning
    $ pronouns = {
                     'he':   {'nom': 'he',   'obj': 'him',  'posd': 'his',    'pos': 'his',    'ref': 'himself'},
                     'she':  {'nom': 'she',  'obj': 'her',  'posd': 'her',    'pos': 'hers',   'ref': 'herself'},
                     'it':   {'nom': 'it',   'obj': 'it',   'posd': 'its',    'pos': 'its',    'ref': 'itself'},
                     'one':  {'nom': 'one',  'obj': 'one',  'posd': 'one\'s', 'pos': 'one\'s', 'ref': 'oneself'},
                     'they': {'nom': 'they', 'obj': 'them', 'posd': 'their',  'pos': 'theirs', 'ref': 'themself'},
                     'xe':   {'nom': 'xe',   'obj': 'xem',  'posd': 'xyr',    'pos': 'xyrs',   'ref': 'xemself'},
                     'ey':   {'nom': 'ey',   'obj': 'em',   'posd': 'eir',    'pos': 'eirs',   'ref': 'emself'},
                     'hu':   {'nom': 'hu',   'obj': 'hum',  'posd': 'hus',    'pos': 'hus',    'ref': 'humself'},
                     'ze':   {'nom': 'ze',   'obj': 'zir',  'posd': 'zir',    'pos': 'zirs',   'ref': 'zirself'}
                 }
    
    # Knowledge for import into characters.  Used for general knowledge items.
    # One could also specify special knowledge bases for specific or certain types of characters.
    $ knowledgebase = {
                        'Harris Hall': KnowledgeBaseItem("it", {'where': "to the south", 'what': "liberal arts building", 'status': "being renovated", 'adjectives': ["old", "stone"]}),
                        'Tech': KnowledgeBaseItem("it", {'where': "up north", 'what': "engineering school building", 'adjectives': ["huge", "hard to navigate", "always full of students"]}),
                        'Professor Smith': KnowledgeBaseItem("he", {'who': "a computer science professor", 'does': "research", 'adjectives': ["old", "busy", "a genius"]}),
                        'Claire Lew': KnowledgeBaseItem("she", {'who': "the student body president"}),
                        'Schapiro': KnowledgeBaseItem("he", {'who': "university president"}),
                        'Kellogg': KnowledgeBaseItem("it", {'where': "between north and south campus", 'what': "the business school", 'adjectives': ["well known", "bustling"]})
                       }
                       
    $ gal_kb =         {
                        'databases': KnowledgeBaseItem("it", {'what': "storing information for retrieval", 'adjectives': ["interesting", "useful"], 'teacher': "Professor Jones"}),
                        'algorithms': KnowledgeBaseItem("it", {'what': "designing efficient problem-solving methods for computing", 'teacher': "Professor Smith", 'adjectives': ["complicated", "difficult"]}),
                        'public speaking': KnowledgeBaseItem("it", {'what': "composing essays and speeches", 'teacher': "Professor Johnson", 'adjectives': ["okay, I guess", "not really something I look forward to"]}),
                       }
    
    # Character definitions.
    
    $ gal_attrs = {'shy': 1, 'intelligent': 3, 'stressed': 8, 'frustrated': 2, 'tired': 3}
    $ gal_prefs = {'books': 2, 'writing': 3, 'math': 1, 'computer science': 5, 'fish': -5, 'Professor Smith': -2, 'finals': -4}
    $ gal_text = {
                     "unknown": ["I'm sorry, I'm not sure I understood you.", "Sorry, what was that?"],
                     "personal-who-query": ["Oh, ?SUBJ\?  ?PNOUN is ?WHAT\.", "?SUBJ\? I think ?PNOUN ?OPINION\."],
                     "where-query": ["?SUBJ is ?WHERE\.  Does that help\?"],
                     "pos-opinion-query": ["Oh, I ?FEELING ?SUBJ\.", "?SUBJ\?  ?ADJ\."],
                     "pos-opinion-respond": ["Me too\!", "I like ?SUBJ too\."],
                     "neg-opinion-query": ["Eh\, it\'s okay\.", "I\'m not that keen on ?SUBJ\."],
                     "neg-opinion-respond": ["?SUBJ\.\.\. Eh.", "I never really got into ?SUBJ\."],
                     "what-doing": ["Oh, I'm ?ACTION\.", "?ACTION\."],
                     "pos-feeling-query": ["Oh, I\'m doing great\, thanks\!", "Doing well\. You\?"],
                     "neg-feeling-query": ["Ugh\. I don\'t want to talk about it\.", "Eh\.  I'm really ?ADJ\."],
                     "classes-query": ["I\'m taking databases\, algorithms\, and public speaking\."],
                     "class-specific": ["It\'s a course on ?DESC\.  It\'s ?ADJ\.", "It\'s about ?DESC\.  It\'s ?ADJ\."],
                     "class-where": ["It\'s in ?LOC\."],
                     "class-teacher": ["?NAME is the professor\.", "It\'s taught by ?NAME\."],
                     "hobbies-query": ["I like to ?ITEM\.", "I ?ITEM\."],
                     "goals-query": ["I want to ?GOAL someday\.", "I\'m going to ?GOAL\."],
                     "neutral-opinion": ["I don\'t really know about ?SUBJ\.", "I can\'t really say I feel strongly either way about ?SUBJ\, I guess\."]
                 }
                 
    $ smith_attrs = {'strict': 2, 'opinionated': 3, 'intelligent': 5, 'lonely': 1, 'sciencey': 5}
    $ smith_prefs = {'students handing in late homework': -10, 'grading homework': -20, 'c': 10, 'vegetables': 3, 'students': -5, 'computer science': 10, 'algorithms': 5}
    
    $ smith_text = {
                     "unknown": ["Eh\, speak up\.", "What\'d you say\?"],
                     "personal-who-query": ["?SUBJ\?  ?PNOUN is ?WHAT\.", "?PNOUN ?OPINION\."],
                     "where-query": ["?WHERE\."],
                     "pos-opinion-query": ["I ?FEELING ?SUBJ\.", "?SUBJ\ is ?ADJ\."],
                     "pos-opinion-respond": ["Me too\!", "I like ?SUBJ too\."],
                     "neg-opinion-query": ["Eh\, it\'s okay\.", "I\'m not that keen on ?SUBJ\."],
                     "neg-opinion-respond": ["?SUBJ\.\.\. Eh.", "I never really got into ?SUBJ\."],
                     "what-doing": ["Oh, I'm ?ACTION\.", "?ACTION\."],
                     "pos-feeling-query": ["Oh, I\'m doing great\, thanks\!", "Doing well\. You\?"],
                     "neg-feeling-query": ["Ugh\. I don\'t want to talk about it\.", "Eh\.  I'm really ?ADJ\."],
                     "classes-query": ["I\'m taking databases\, algorithms\, and public speaking\."],
                     "class-specific": ["It\'s a course on ?DESC\.  It\'s ?ADJ\.", "It\'s about ?DESC\.  It\'s ?ADJ\."],
                     "class-where": ["It\'s in ?LOC\."],
                     "class-teacher": ["?NAME is the professor\.", "It\'s taught by ?NAME\."],
                     "hobbies-query": ["I like to ?ITEM\.", "I ?ITEM\."],
                     "goals-query": ["I want to ?GOAL someday\.", "I\'m going to ?GOAL\."],
                     "neutral-opinion": ["I don\'t really know about ?SUBJ\.", "I can\'t really say I feel strongly either way about ?SUBJ\, I guess\."]
                 }
    
    $ galatea = AICharacter('Galatea', attrs=gal_attrs, prefs=gal_prefs, text=gal_text)
    $ profsmith = AICharacter('Professor Smith', attrs=smith_attrs, prefs=smith_prefs)


# The game starts here.
label start:
    
    scene bg white
    
    "Hey there!  Just a few things to start."
    
    # O hai.  Enter your information.
    $ username = renpy.input("What's your name?", "Eliza")
    
    "Thanks, %(username)s!  And one more thing:"
    
    $ userpronoun = renpy.input("What's your preferred nominal pronoun? (e.g. he, she, ey, etc.)")
    
    $ pronounset = None
    
    if userpronoun == "he":
        $ pronounset = pronouns['he']
    elif userpronoun == "she":
        $ pronounset = pronouns['she']
    elif userpronoun == "ey":
        $ pronounset = pronouns['ey']
    elif userpronoun == "xe":
        $ pronounset = pronouns['xe']
    elif userpronoun == "zie":
        $ pronounset = pronouns['ze']
    elif userpronoun == "one":
        $ pronounset = pronouns['one']
    elif userpronoun == "it":
        $ pronounset = pronouns['it']
    elif userpronoun == "hu":
        $ pronounset = pronouns['hu']
    else:
        $ pronounset = pronouns['they']
    
    "All right, good to go."
    
    "A tip: for purposes of this demo, you...{w=3} {i}might{/i} want to ask about simple things, or school-related things.  Just a suggestion."
    
label chooseconvo:
    
    "Who would you like to talk to?"
    
    # Choose which character with which you would like to interact.
    menu:
        "Galatea":
            $ talkingto = galatea
        "Professor Smith":
            $ talkingto = profsmith
        "Exit":
            return
            
    scene bg convo with fade
        
label convo:
    
    # for each input: feed to $ talkingto.Respond("the string").  For the ones that end in ..., such as
    # "What do you think of...", the query string is concatenated to the user's input before feeding to
    # the response function.
    
    # The response function of the character will classify the query type (e.g. info-query, opinion-query,
    # etc.) and then pull out the variables and generate an appropriate response to the query.  Probably.
    
    # The response is then returned and fed to
    
    show current at left
    
    $ query = renpy.input("What would you like to say?")
    $ (reply, expr, cont) = talkingto.Respond(query)
    
    #$ renpy.image(('current'), "images/%s/%s.png" % (talkingto.name, expr))
    
    show current at left
    
    $ renpy.say(talkingto.name, reply)
    
    # cont will be False if the user says goodbye, or the character doesn't want to talk anymore.
    if cont:
        jump convo
    
    # To exit to menu
    jump chooseconvo
    
