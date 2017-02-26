#1. Dokimaste to me profil me poli ligous followers logo tou oti afksanete o
#xronos pou prepei na kanei sleep (sleeptime) me geometriki proodo kai
#den kserw ton akrivi xrono pou afksanete
#2.Sta onomata doste to onoma xristi pou vriskete katw apo to kanoniko kai
#arxizei me "@" p.x. @hfgibv kai @wugokong11

user1=raw_input("Dose onoma xristi sto tweeter")
user2=raw_input("Dose onoma allou xristi gia evresi koinon follower")
import tweepy
import time
auth = tweepy.OAuthHandler('6Js2ODbpDsI7iF4NzZG1zwG21','kErunboiWsP8ngIuwquCps0IcPymrrvD2LKmoofxkWLU37Ojih')
auth.set_access_token('820965378511765505-aEPIH09Y0NEO15BVQhvB92mjtD6QCFL','x7wbXCqHKunq0GFYfuFxuFf0esbtrf1q5JlQikyS0ys3p')
api = tweepy.API(auth)
sleeptime = 10
i=0
list1= []
pages = tweepy.Cursor(api.followers, screen_name=user1).pages()
while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(1) 
        page = next(page)
    except StopIteration:
        break
    for user in page:
        list1.append(user.screen_name)
       
sleeptime = 10
pages = tweepy.Cursor(api.followers, screen_name=user2).pages()
while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(1) 
        page = next(page)
    except StopIteration:
        break
    for user in page:
        item = user.screen_name
        if item in list1:
            print (user.screen_name)

