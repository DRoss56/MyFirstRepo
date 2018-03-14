import pyautogui as pg
import time
import webbrowser
points = 0

#Question
answer = pg.prompt(
"""
How do you spend most saterdays?

a)With the boys
b)Doing mathematics
c)Gaming
d)Sports

"""
    )

#Give points
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "d":
    points +=3
elif answer == "c":
    points +=4

#Question
answer = pg.prompt(
"""
In which situation is it okay to cry?

a)When you are sad
b)At the Grand Canyon
c)When you are shot
d)None of the above

"""
    )

#Give points
if answer == "a":
    points +=4
elif answer == "b":
    points +=1
elif answer == "d":
    points +=2
elif answer == "c":
    points +=3



#Question
answer = pg.prompt(
"""
How many Fortnight wins do you have?

a)0
b)1
c)2
d)3+



"""
    )

#Give points
if answer == "a":
    points +=4
elif answer == "b":
    points +=3
elif answer == "d":
    points +=1
elif answer == "c":
    points +=2


#Question
answer = pg.prompt(
"""
What role do you play in the social heirarchy?

a)Nerd
b)Jock
c)Dominant Male
d)Scholar
"""
    )

#Give points
if answer == "a":
    points +=4
elif answer == "b":
    points +=2
elif answer == "d":
    points +=3
elif answer == "c":
    points +=1


# END OF SURVEY

pg.alert("Wow ")

# it must be Dashiell because you are a cool cat
if points <= 4:
    pg.alert("it must be Dashiell because you are a cool cat")
    webbrowser.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1366&bih=637&tbm=isch&sa=1&ei=XE9vWqGYCJKR_QbPp5rYDg&q=cool+club+penguin&oq=cool+club+penguin&gs_l=psy-ab.3..0l4j0i30k1j0i8i30k1j0i24k1l2.27862.30678.0.31043.17.17.0.0.0.0.88.966.17.17.0....0...1c.1.64.psy-ab..0.17.962...0i67k1.0.NuTVNZcmZ_g#imgrc=g5nLA4zZ8AI1QM:")
# Somewhat cool
if points <= 8 and points > 4:
    pg.alert("You are pretty cool, not quite a cool cat")
    webbrowser.open ("https://www.youtube.com/watch?v=TcWPiHjIExA")
# Not cool
if points > 8 and points < 12:
    pg.alert("Sorry but you just dont have the cool factor to you, try to take your cool pills daily")
    webbrowser.open ("https://www.youtube.com/watch?v=TcWPiHjIExA")
# Nerd
if points > 12:
    pg.alert("You aren't cool at all you nerdface jk just take more cool pills")
    webbrowser.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1366&bih=637&tbm=isch&sa=1&ei=0E9vWs-9E4-zggeXzq_4CA&q=h3+h3+cool&oq=h3+h3+cool&gs_l=psy-ab.3...12944.18738.0.19010.19.13.4.2.4.0.78.692.13.13.0....0...1c.1.64.psy-ab..0.17.605...0j0i67k1j0i10k1j0i13k1j0i13i30k1.0.YvatKkwjCjU#imgrc=DdiTPoO3lB6ITM:")
