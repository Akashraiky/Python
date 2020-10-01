#importing modules for required functions

import pyttsx3
import os

pyttsx3.speak("Welcome user I'm Raiky's Assistant How can I help you ? ")

while True:
    print("Tell Me How can I help you ?")
    pyttsx3.speak("Tell Me How can I help you ?")
    p = input().lower()
    
    if  (("run" in p) or  ("open" in p) or ("launch" in p))  and  (("notepad" in p) or  ("editor" in p)):
         pyttsx3.speak("Opening notepad for you please wait")
         os.system("notepad")

    elif  (("run" in p) or ("open" in p) or  ("launch" in p))  and  (("chrome" in p) or  ("browser" in p)) :
         pyttsx3.speak("Opening chrome for you please wait")
         os.system("start chrome")

    elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("linkedin" in p) :
         pyttsx3.speak("Opening your linked account  you plz wait")
         os.system("start chrome linked.in")
         
    elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("codeblocks" in p):
         pyttsx3.speak("Opening codeblocks for you please wait")
         os.system("start codeblocks.exe")
         
    elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ('task manager' in p or 'taskmanager' in p):
         pyttsx3.speak("Opening task manager for you please wait")
         os.system("taskmgr")

    elif  (("run" in p) or  ("open" in p) or ("launch" in p)) and ("calculator" in p):
         pyttsx3.speak("Opening calculator for you please wait")
         os.system("calc")
         
    elif  (("run" in p) or  ("open" in p) or ("launch" in p))  and  ("virtual box" in p) :
         pyttsx3.speak("Opening virtual box for you plz wait")
         os.system("start Oracle VM VirtualBox")
         
    elif (("make" in p) or ("create" in p) or ("new" in p))  and  (("folder" in p) or ("directory" in p)):
           print("Enter full path with new folder name :")
           pyttsx3.speak("Enter full path with new folder name")
           path = input() 
           os.mkdir(path)
                                                                   
    elif (("current" in p) or ("working" in p))  and  (("folder" in p) or ("directory" in p)):
           di = os.getcwd()
           pyttsx3.speak("Current working directory is")
           print("Current working directory is :",di)
           
    elif (("hi" in p) or ("hello" in p) or ("hey" in p)):
         print("Hello I'm Raiky's Assistant How can I help you ?")
         pyttsx3.speak("Hello I'm Raiky's Assistant")

    elif (("thought" in p) or ("idea" in p) or ("notion" in p) or ("motivation" in p) or ("motivate" in p) or ("say" in p) or ("something" in p) ):
         print("Always Remember your focus determines your reality")
         pyttsx3.speak("Always Remember your focus determines your reality")

    elif ("exit" in p) or ("quit" in p) or ("shutdown" in p) or ("close" in p) or ("kill" in p) or ("stop" in p) :
         pyttsx3.speak("Shutting down ")
         break
        
    else:
         pyttsx3.speak("such application doesn't exist in your computer plz tell again")
    
