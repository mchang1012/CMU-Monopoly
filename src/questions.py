import random
def makeQuestions():
    return {
    1: {
        'question': 'When does the 2025 First-Year Orientation at CMU begin?',
        'options': ['August 10', 'August 16', 'August 23', 'September 1'],
        'answer': 'August 16'
    },
    2: {
        'question': ("What is the name of the weekly summer newsletter " +
            "sent to incoming first-year students and their families?"),
        'options': ['Tartan Times', 'CMU Chronicle', 'Talking Tartan', 
                    "Scotty's Scoop"],
        'answer': 'Talking Tartan'
    },
    3: {
        'question': ("""Which event during Orientation""" + 
                     """emphasizes community """ +
            """and belonging through performances and storytelling?"""),
        'options': ['Playfair', 'Community Collage', 'Tartan Talent Show', 
                    "Scotty's Showcase"],
        'answer': 'Community Collage'
    },
    4: {
        'question': """What is the name of CMU's mascot?""",
        'options': ['Tartan Tom', 'Scotty the Scottish Terrier', 
                    'Carnegie Cat', 'Mel the Mole'],
        'answer': 'Scotty the Scottish Terrier'
    },
    5: {
        'question': ("""Which band is known for wearing """ +
            """kilts and performing at CMU events?"""),
        'options': ['The Tartan Tunes', 'The Kiltie Band', 
                    'The Scotty Ensemble', 'The Highland Harmonies'],
        'answer': 'The Kiltie Band'
    },
    6: {
        'question': "What is the name of CMU's student newspaper?",
        'options': ['The Tartan', 'The Scotty Times', 
                    'The Carnegie Chronicle', 'The Mellon Monthly'],
        'answer': 'The Tartan'
    },
    7: {
        'question': ("""Which event is considered the biggest of the """ +
            """CMU school year, featuring booths and a four-day weekend?"""),
        'options': ['Spring Fling', 'Tartan Fest', 
                    'Spring Carnival', 'Scotty Fair'],
        'answer': 'Spring Carnival'
    },
    8: {
        'question': ('What is the primary purpose of the' + 
        ' First-Year Orientation program?'),
        'options': [
            'To assign dorm rooms',
            "To introduce students to Pittsburgh's nightlife",
            'To build a foundation for academic success and' + 
            ' community membership',
            'To select student organizations'
        ],
        'answer': ('To build a foundation for academic success and ' +
                'community membership')
    },
    9: {
        'question': ("""Which office provides leadership for """ + 
            """new student orientation and transition programs?"""),
        'options': ['Office of Student Affairs', 
                    'Office of First-Year Orientation', 
                    'Academic Advising Center', 'Student Life Services'],
        'answer': 'Office of First-Year Orientation'
    },
    10: {
        'question': ("""What is the name of the competition""" + 
            """awarded after Orientation week """ + 
            """to recognize student engagement?"""),
        'options': ['The Scotty Shield', 'The Carnegie Cup', 
                    'The Tartan Trophy', 
                    'The Mellon Medal'],
        'answer': 'The Carnegie Cup'
    },
    11: {
        'question': ("Which platform do CMU students use " +
            "to access their class schedules, " +
            "grades, and financial information?"),
        'options': ['Canvas', 'The HUB', 'SIO (Student Information Online)', 
                    'Tartan Connect'],
        'answer': 'SIO (Student Information Online)'
    },
    12: {
        'question': ("""What is the name of the online learning """ + 
            """management system used for coursework at CMU?"""),
        'options': ['Blackboard', 'Moodle', 'Canvas', 'Brightspace'],
        'answer': 'Canvas'
    },
    13: {
        'question': ("""Which office offers in-person and """ +
        """online enrollment services related to financial aid,""" + 
        """billing, and academic records?"""),
        'options': ['The HUB', 'Student Affairs', 'Academic Advising Center', 
                    'Registrar\'s Office'],
        'answer': 'The HUB'
    },
    14: {
        'question': ("Which program provides first-year engineering students " +
            """with resources and programming for a successful transition?"""),
        'options': ['Engineering Launch', 'First-Year Experience (FYE)', 
                    'Tartan Engineering Program', 'CMU Engineering Start'],
        'answer': 'First-Year Experience (FYE)'
    },
    15: {
        'question': ("""During the summer before starting at CMU, """ +
            """how do engineering students receive advising?"""),
        'options': ['In-person meetings', 'Through technologies like Skype, '
        'IM, and email', 'Only via phone calls', 
        'They don’t receive advising until fall'],
        'answer': 'Through technologies like Skype, IM, and email'
    },
    16: {
        'question': ("""Which department is known for pioneering """ +
            """research in machine learning and robotics at CMU?"""),
        'options': ['Tepper School of Business', 
                    'School of Computer Science', 'Mellon College of Science', 
                    'Heinz College'],
        'answer': 'School of Computer Science'
    },
    17: {
        'question': ("""What is the name of CMU's initiative""" +
            """ that integrates innovation across disciplines?"""),
        'options': ['Innovation Hub', 'Integrated Innovation Institute', 
                    'Carnegie Innovation Center', 'Tartan Innovation Lab'],
        'answer': 'Integrated Innovation Institute'
    },
    18: {
        'question': ("""Which CMU library houses the """ +
            """Million Book Project and various special collections?"""),
        'options': ['Hunt Library', 'Mellon Institute Library', 
                    'Posner Center', 'Sorrells Engineering & Science Library'],
        'answer': 'Hunt Library'
    },
    19: {
        'question': ("""What is the name of the CMU department """ +
            """that focuses on secure communication networks and systems?"""),
        'options': ['CyLab', 'Information Networking Institute', 
                    'Security Systems Lab', 'Tartan Defense Group'],
        'answer': 'CyLab'
    },
    20: {
        'question': ("""Which CMU resource helps students """ + 
            """with writing assignments, presentations, """ + 
            """and public speaking?"""),
        'options': ['The HUB', 
                    'Career and Professional Development Center', 
                    'Global Communication Center (GCC)', 
                    'Academic Success Center'],
        'answer': 'Global Communication Center (GCC)'
    },
    21: {
        'question': ("""What does the Career and Professional """ +
            """Development Center (CPDC) at CMU primarily help with?"""),
        'options': ['Course selection', 'Health services', 
                    'Career exploration and job/internship preparation', 
                    'Housing assignments'],
        'answer': 'Career exploration and job/internship preparation'
    },
    22: {
        'question': ("""Which CMU center provides support for """ +
            """mental health and emotional well-being?"""),
        'options': ['Student Health Services', 'Wellness Hub', 
                    'Counseling and Psychological Services (CaPS)', 
                    'Campus Mindfulness Center'],
        'answer': 'Counseling and Psychological Services (CaPS)'
    },
    23: {
        'question': ("""Which CMU college is known """ +
            """for design, architecture, and drama?"""),
        'options': ['Heinz College', 'Mellon College of Science', 
                    'College of Fine Arts (CFA)', 
                    'School of Computer Science'],
        'answer': 'College of Fine Arts (CFA)'
    },
    24: {
        'question': ("Where is the CMU Student Academic Success " +
        "Center (SASC) located?"),
        'options': ['Posner Hall', 'Cyert Hall', 'Hunt Library', 'West Wing'],
        'answer': 'Hunt Library'
    },
    25: {
        'question': """What is the Tartan Scholars program designed for?""",
        'options': ['Students with military backgrounds', 
                    'First-generation and/or low-income students', 
                    'International transfer students', 
                    'Study abroad participants'],
        'answer': 'First-generation and/or low-income students'
    },
    26: {
        'question': ("""Which app is used by CMU students """ +
        """for dining services, menus, and mobile orders?"""),
        'options': ['Tartan Eats', 'GrubCMU', 'GET', 'Scotty Food'],
        'answer': 'GET'
    },
    27: {
        'question': """Which location on campus is best """ +
            """known for late-night dining and events like karaoke?""",
        'options': ['Randy Pausch Cafe', 'Entropy+', 'Resnik Cafe', 
                    'The Underground'],
        'answer': 'The Underground'
    },
    28: {
        'question': ("""Which CMU building is home to the School """ +
            """of Computer Science and features an """ +
            """iconic spiral staircase?"""),
        'options': ['Doherty Hall', 'Wean Hall', 'Gates-Hillman Complex', 
                    'Porter Hall'],
        'answer': 'Gates-Hillman Complex'
    },
    29: {
        'question': ("""Which CMU initiative offers funding and """ +
            """support for student-led startups?"""),
        'options': ['Project Olympus', 'Scotty Startups', 
                    'Innovation Launchpad', 
                    'Carnegie Incubator'],
        'answer': 'Project Olympus'
    },
    30: {
        'question': ("""Which famous CMU professor gave """ +
        """“The Last Lecture” that became a global phenomenon?"""),
        'options': ['Randy Pausch', 'Alan Perlis', 'Herbert Simon', 
                    'Manuela Veloso'],
        'answer': 'Randy Pausch'
    },
    31: {
        'question': ("""What is CMU’s official student portal """ +
        """for organizations, events, and involvement?"""),
        'options': ['The Tartan Connection', 'Scotty Central', 
                    'TartanConnect', 'CMU Link'],
        'answer': 'TartanConnect'
    },
    32: {
        'question': ("""Which residence hall is known for housing """ +
        """first-years in the College of Fine Arts?"""),
        'options': ['Mudge House', 'Scobell House', 'Stever House', 
                    'The Residence on Fifth'],
        'answer': 'Mudge House'
    },
    33: {
        'question': ("""What is the name of the CMU shuttle system """ +
        """available to students?"""),
        'options': ['CMU Express', 'Tartan Shuttle', 'Scotty Transit', 
                    'Pittsburgh Loop'],
        'answer': 'Tartan Shuttle'
    },
    34: {
        'question': ("""Which annual CMU event features student-built """ +
        """buggies racing around campus?"""),
        'options': ['Tech Drive', 'Scotty Sprint', 'Buggy Sweepstakes', 
                    'Tartan Roll'],
        'answer': 'Buggy Sweepstakes'
    },
    35: {
        'question': ("""Which center helps CMU students with tutoring, """ +
            """workshops, and academic coaching?"""),
        'options': ['Student Learning Hub', 
                    'Global Communication Center', 
                    'Academic Resource Center', 
                    'Student Academic Success Center'],
        'answer': 'Student Academic Success Center'
    },
    36: {
        'question': ("""Which CMU dining location is located in""" + 
        """the Cohon University Center?"""),
        'options': ['Resnik Café', 'Schatz Dining Room', 'Tepper Eats', 
                    'Randy Pausch Café'],
        'answer': 'Schatz Dining Room'
    },
    37: {
        'question': """What is the name of CMU’s esports and gaming club?""",
        'options': ['Tartan Gaming League', 'CMU Esports', 
                    'Scotty Gaming Society', 'Pixel Club'],
        'answer': 'CMU Esports'
    },
    38: {
        'question': ("""Which CMU department should students """ +
        """contact for disability resources and accommodations?"""),
        'options': ['Office of Diversity and Inclusion', 'Student Affairs', 
                    'Disability Resources Office', 'Academic Support Center'],
        'answer': 'Disability Resources Office'
    },
    39: {
        'question': ("""What is the name of CMU’s iconic red """ +
            """sculpture near the Purnell Center?"""),
        'options': ['Abstract Flame', 'Walking to the Sky', 'The Spiral', 
                    'Ascending Steel'],
        'answer': 'Walking to the Sky'
    },
    40: {
        'question': 'What is the official CMU student ID card called?',
        'options': ['Scotty Card', 'CMU Pass', 'Tartan ID', 'Andrew Card'],
        'answer': 'Tartan ID'
    }
}

def loadQuestion(app):
    app.optionCircles = []
    app.optionLabels = []

    app.questionIndex = random.choice(app.availableQuestions)
    questionData = app.questions[app.questionIndex]
    app.currQuestion = questionData['question']
    app.options = questionData['options']
    app.answer = questionData['answer']

    # get locations for multiple-choice circles and options
    spacing = 80
    startY = app.height/4 + 120
    for i in range(len(app.options)):
        cy = startY + (i * spacing)
        app.optionCircles.append(cy)
        app.optionLabels.append((app.options[i],cy))