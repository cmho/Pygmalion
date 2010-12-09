init -1 python:

    import random
    import re
    
    username = "Eliza"
    
    # list of moods for identification purposes and calculating how a character is feeling
    moods = {
                'positive': ["happy", "joyful", "accomplished", "hopeful", "peaceful", "energetic", "rested"],
                'negative': ["tired", "stressed", "frustrated", "unhappy", "upset", "angry", "uncomfortable", "injured", "in-pain"]
            }
    
    def ClassifyQuery(qstr):
        querytype = None
        
        match = None
        
        # do some pattern matching stuff
        if re.match("Hello", qstr) is not None or re.match("Hi", qstr) is not None:
            querytype = "hello"
        elif re.search(qstr, "My name is (?P<name>\w+)") is not None:
            match = re.search("My name is (?P<name>\w+)", qstr)
            querytype = "self-intro"
        elif re.search(qstr, "My name's (?P<name>\w+)") is not None:
            match = re.search("My name's (?P<name>\w+)", qstr)
            querytype = "introduction"
        elif re.match("How are you (?P<feeling>\w+)", qstr) is not None:
            querytype = "mood-inquiry"
        elif re.search("What do you think of (?P<subj>\w+)", qstr) is not None or re.search("What's your opinion of(?P<subj>\w+)", qstr):
            querytype = "opinion-query"
        elif re.search(qstr, "goodbye") is not None or re.search(qstr, "bye") is not None:
            querytype = "goodbye"
        else:
            querytype = "unknown"
            
        if match is not None:
            qvars = match.groupdict()
        else:
            qvars = {}
        
        return (querytype, qvars)

    class KnowledgeBaseItem(object):
        def __init__(self, pronoun, infostrings):
            self.pronoun = pronoun
            self.infostrings = infostrings # hash
            
        def GetInfo(self):
            return self.infostrings[random.random(0, len(self.infostrings))]

    class Preference(object):
        def __init__(self, name, lev):
            self.name = name
            self.level = lev
            #self.vals = vals # a hash of feelings about the preference
            
            #for val in self.vals:
            #    self.level += val
        
    class Relationship(object):
        def __init__(self, attrs, reltype, label, info):
            self.attributes = attrs #hash
            self.reltype = reltype #string
            self.label = label #string
            self.info = info #hash
    
    class AICharacter(object):
        """
        The character object contains information about a character. When
        passed as the first argument to a say statement, it can control
        the name that is displayed to the user, and the style of the label
        showing the name, the text of the dialogue, and the window
        containing both the label and the dialogue.
        """
    
        # Properties beginning with what or window that are treated
        # specially.
        special_properties = [
            'what_prefix',
            'what_suffix',
            'who_prefix',
            'who_suffix',
            'show_function',
            ]
    
        # When adding a new argument here, remember to add it to copy below.
        def __init__(
            self,
            name,
            **properties):
    
            # This grabs a value out of properties, and then grabs it out of
            # kind if it's not set.
            def v(n):
                if n in properties:
                    return properties.pop(n)
    
    
            # Similar, but it grabs the value out of kind.display_args instead.            
            def d(n):
                if n in properties:
                    return properties.pop(n)
                
            self.name = v('name')
            self.who_prefix = v('who_prefix')
            self.who_suffix = v('who_suffix')
            self.what_prefix = v('what_prefix')
            self.what_suffix = v('what_suffix')
    
            self.show_function = v('show_function')
            self.predict_function = v('predict_function')
    
            self.condition = v('condition')
            self.dynamic = v('dynamic')
            self.screen = v('screen')
            self.mode = v('mode')
            
            # AI-specific variables
            self.attributes = v('attrs')       # hash
            self.relationships = v('rels')     # hash of relationships
            self.prefs = v('prefs')            # list of prefs
            self.stocktext = v('text')         # dialogue set
            self.behaviors = v('behaviors')    # list of strings
            
            # keep track of who you're talking to
            self.speakingto = "<noname>"
            
            # thresholds for how much "like" or "dislike" it'll take for the character to decide whether they
            # want to be your bff or to hate you.
            self.befriend = 3
            self.hate = -5
            
            # This keeps track of the last thing you were talking about so if the user uses a pronoun
            # in the next query rather than a name it'll guess that you were talking about the last
            # subject.
            self.lastsubj = None
            
            self.display_args = dict(
                interact = d('interact'),
                slow = d('slow'),
                afm = d('afm'),
                ctc = renpy.easy.displayable_or_none(d('ctc')),
                ctc_pause = renpy.easy.displayable_or_none(d('ctc_pause')),
                ctc_timedpause = renpy.easy.displayable_or_none(d('ctc_timedpause')),
                ctc_position = d('ctc_position'),
                all_at_once = d('all_at_once'),
                with_none = d('with_none'),
                callback = d('callback'),
                type = d('type'),
                )
                
            self.who_args = { }
            self.what_args = { }
            self.window_args = { }
            self.show_args = { }
            self.cb_args = { }
    
            if "image" in properties:
                self.show_args["image"] = properties.pop("image")
    
            if "slow_abortable" in properties:
                self.what_args["slow_abortable"] = properties.pop("slow_abortable")
                
            for k in list(properties):
    
                if "_" in k:
                    prefix, suffix = k.split("_", 1)
    
                    if prefix == "show":
                        self.show_args[suffix] = properties[k]
                        continue
                    elif prefix == "cb":
                        self.cb_args[suffix] = properties[k]
                        continue
                    elif prefix == "what":
                        self.what_args[suffix] = properties[k]
                        continue
                    elif prefix == "window":
                        self.window_args[suffix] = properties[k]
                        continue
                    elif prefix == "who":
                        self.who_args[suffix] = properties[k]
                        continue
    
                self.who_args[k] = properties[k]
    
        def copy(self, name, **properties):
            return type(self)(name, **properties)
    
        # This is called before the interaction. 
        def do_add(self, who, what):
            return
    
        # This is what shows the screen for a given interaction.
        def do_show(self, who, what):
            return self.show_function(
                who,
                what, 
                who_args=self.who_args,
                what_args=self.what_args,
                window_args=self.window_args,
                screen=self.screen,
                **self.show_args)
    
        # This is called after the last interaction is done.
        def do_done(self, who, what):
            return
        
        # This is called when an extend occurs, before the usual add/show
        # cycel.
        def do_extend(self):
            return
    
        # This is called to actually do the displaying.
        def do_display(self, who, what, **display_args):
            display_say(who,
                        what,
                        self.do_show,
                        **display_args)
            
        
        # This is called to predict images that will be used by this
        # statement.
        def do_predict(self, who, what):
            return self.predict_function(
                who,
                what,
                who_args=self.who_args,
                what_args=self.what_args,
                window_args=self.window_args,
                **self.show_args)
        
        def __call__(self, what, interact=True, **kwargs):
    
            # Check self.condition to see if we should show this line at all.
    
            if not (self.condition is None or renpy.python.py_eval(self.condition)):
                return True
    
            if interact:
                renpy.exports.mode(self.mode)
        
            # Figure out the arguments to display.
            display_args = self.display_args.copy()
            display_args.update(kwargs)
            display_args["interact"] = display_args["interact"] and interact
            
            who = self.name
    
            # If dynamic is set, evaluate the name expression.
            if self.dynamic:
                who = renpy.python.py_eval(who)
    
            if who is not None:
                who = self.who_prefix + who + self.who_suffix
    
            what = self.what_prefix + what + self.what_suffix
    
            # Run the add_function, to add this character to the
            # things like NVL-mode.
            self.do_add(who, what)
    
            # Now, display the damned thing.
            self.do_display(who, what, cb_args=self.cb_args, **display_args)
    
            # Indicate that we're done.
            self.do_done(who, what)
    
            # Finally, log this line of dialogue.        
            if who and isinstance(who, (str, unicode)):
                renpy.exports.log(who)
            renpy.exports.log(what)
            renpy.exports.log("")
                    
        def predict(self, what):
    
            if self.dynamic:
                who = "<Dynamic>"
            else:
                who = self.name
    
            return self.do_predict(who, what)
    
        def will_interact(self):
    
            if not (self.condition is None or renpy.python.py_eval(self.condition)):
                return False
    
            return self.display_args['interact']
            
        def HasRelationshipTo(self, name):
            if name in self.relationships:
                return True
            return False
            
        def InitReact(self, other):
            reactval = 0
            
            for pref in self.prefs:
                if pref in other.attrs:
                    pref.level += reactval
                    
            if other.name not in self.relationships:
                # Need to add relationship
                # Initialize relationship attributes
                relattrs = {}
                
                if reactval > self.befriend:
                    relattrs['liked'] = reactval - self.befriend
                elif reactval < self.hate:
                    relattrs['hated'] = reactval - self.hate
                    
                otherinfo = []
                    
                AddRelationship(other, relattrs, "personal", "acquaintance", otherinfo)
        
        # Most of these are so I don't have to type ridiculous strings of references all the time
        # And also for readability        
        def AddRelationship(self, other, attrs, reltype, label, info):
            otherr = Relationship(attrs, reltype, label, info)
            self.relationships[other.name] = otherr
            
        def ModRelAttr(self, name, attrname, value):
            if attrname in self.relationships[name].attrs:
                self.relationships[name].attrs[attrname] += value
                return
            self.relationships[name].attrs[attrname] = value
            
        def ChangeRelLabel(self, name, newlabel):
            self.relationships[name].label = newlabel
            
        def AddRelInfo(self, name, infostr):
            self.relationships[name].info.append(infostr)
            
        def RandomRelInfo(self, name):
            return random.choice(self.relationships[name].info)
            
        def InfoLookup(self, item, querytype):
            if querytype == "who" or querytype == "what":
                if HasRelationshipTo(item):
                    return RandomRelInfo(item)
            if item in knowledgebase:
                if querytype in knowledgebase[item]:
                    return knowledgebase[item][querytype]
                else:
                    return random.choice(knowledgebase[item][adjectives])
            return -1
            
        def HasBehavior(self, behave):
            if behave in self.behaviors:
                return True
            return False
            
        def GetRandomResponse(self, situation):
            if situation in self.stocktext:
                return random.choice(self.stocktext[situation])
            
        def Respond(self, qstring):
            # who/what query
            
            (querytype, qvars) = ClassifyQuery(qstring)
            
            if "subject" in qvars:
                if qvars['subject'] is not ("he" or "she" or "it" or "they"):
                    self.lastsubject = qvars['subject']
            
            expression = "happy"
            
            cont = True
            
            self.speakingto = username
            
            if querytype == "hello":
                respstr = self.GetRandomResponse("hello")
                if self.speakingto in self.relationships:
                    namequery = ""
                else:
                    namequery = random.choice(self.stocktext['name-query'])
                    re.subn("?NAMEQUERY", namequery, respstr)
            elif querytype == "introduction":
                respstr = self.GetRandomResponse("introduction")
                re.subn("?NAME", self.speakingto, respstr)
            elif querytype == "info-query":
                if HasRelationshipTo(qvars['subject']):
                    if self.relationships[qvars['subject']].reltype == "personal":
                        respstr = self.GetRandomResponse("personal-who-query")
                        infostr = self.RandomRelInfo(qvars['subject'])
                        re.subn("?SUBJ", qvars['subject'], respstr)
                        re.subn("?INFO", infostr, respstr)
                else:
                    if qvars['subject'] in knowledgebase:
                        if "who" in knowledgebase[qvars['subject']]:
                            respstr = knowledgebase[item]['who']
                        elif "what" in knowledgebase[qvars['subject']]:
                            respstr = knowledgebase[item]['what']
                # if false, check in general knowledge base
                
                # else: generate "unknown" response
                respstr = self.GetRandomResponse("dont-know")
            # location query
            elif querytype == "where-query":
                if qvars['subject'] in knowledgebase:
                    if "where" in knowledgebase[qvars['subject']]:
                        qvars['where'] = knowledgebase[qvars['subject']]['where']
                        respstr = self.GetRandomResponse("where-query")
                        re.subn("?SUBJ", qvars['subject'], respstr)
                        re.subn("?WHERE", qvars['where'], respstr)
                else:
                    respstr = "I don't know where " + qvars['subject'] + "is."
                
            elif querytype == "opinion-query":
                if qvars['subj'] in self.prefs:
                    if self.prefs[qvars['subj']] > 0:
                        respstr = self.GetRandomResponse("pos-opinion-query")
                    elif self.prefs[qvars['subj']] < 0:
                        respstr = self.GetRandomResponse("neg-opinion-query")
                    else:
                        respstr = self.GetRandomResponse("neutral-opinion")
                        
                re.subn("?SUBJ", qvars['subject'], respstr)
                
            elif querytype == "goodbye":
                goodbye = True
                respstr = self.GetRandomResponse("unknown")
                
            elif querytype == "unknown":
                respstr = self.GetRandomResponse("unknown")
                
            return (respstr, expression, cont)
