from jikanpy import Jikan
from pprint import pprint
from datetime import datetime, timedelta


jikan = Jikan()
def main():
    #jikan = Jikan()

    mushishi = jikan.anime(457)
    mushishi_with_eps = jikan.anime(457, extension='episodes')

    search_result = jikan.search('anime', 'Mushishi', page=2)

    winter_2018_anime = jikan.season(year=2018, season='winter')

    archive = jikan.season_archive()

    later = jikan.top(type='anime', page=1)

    upcoming = jikan.season_later()

    sched = jikan.schedule(day='saturday')

    yay = jikan.season(year=2020, season='fall')

    top = later['top']
    #pprint(top[0])
    print(len(top))
    #print(top[0]['title'])

    print("-------------------------TOP ANIME:--------------------------------")
    pprint(later['top'])

    for i in range(len(later['top'])):
        print(later['top'][i]['title'])
    
    print(later['top'][0]['title'])
    print(later['top'][49]['title'])
    
    #sort =  sorted(later['top'])
    print("-------------------------SORTED:--------------------------------")
    top.sort(key=lambda item: item.get("title"))
    pprint(top)

    #pprint(search_result['results'])

    #pprint(upcoming['anime'])
    print("-------------------------SATURDAY:--------------------------------")
    for i in range(len(sched['saturday'])):
        print(sched['saturday'][i]['title'])
    #pprint(sched['friday'])

    print("-------------------------2020 FALL:--------------------------------")
    test = yay['anime']
    test.sort(key=lambda item: item.get("title"))
    for i in range(len(yay['anime'])):
        if(test[i]['type']=='TV'):
            print(test[i]['title'])

    #pprint(yay['anime'])

def seasonal(option):
    #option = 0 sort by title
    #option = 1 #sort by score
    #option = 2 #sort by members
    seas = get_current_season()
    ye = get_current_year()

    yay = jikan.season(year=ye, season=seas)
    wow = yay['anime']
    wow.sort(key=lambda item: item.get("title"))

    today =datetime.today()

    for i in range(len(wow)):
        awareness = wow[i]['airing_start']
        if(awareness):
            d1 = datetime.fromisoformat(awareness)
            #wow[i]['airing_start'] = d1.strftime('%A')
            wow[i]['airing_start'] = d1.strftime('%A')
            wow[i]['abbrv'] = d1.strftime('%b %-d')

            future = d1.replace(tzinfo=None)
            #wiff = future - today
            #diff = wiff- timedelta(hours=7)
            #count_hours, rem = divmod(diff.seconds, 3600)
            if today>future:
                d1 = datetime.fromisoformat(awareness)
                while(today>future):
                    future = future+timedelta(days=7)
            wiff = future - today
            diff = wiff- timedelta(hours=7)
            count_hours, rem = divmod(diff.seconds, 3600)
            countdown = future-timedelta(hours=7)
            wow[i]['days_left']= int(diff.days)
            wow[i]['hours_left'] = int(count_hours)
            wow[i]['iso'] = countdown.isoformat()
        #else:
            wow[i]['days_left'] = 1001
            wow[i]['hours_left'] = 1001

    if option == "Score":
        for i in range(len(wow)):
            if wow[i]['score']== None:
                wow[i]['score']=0
        wow.sort(key=lambda item: item.get("score"),reverse=True)
    if option == "Members":
        for i in range(len(wow)):
            if wow[i]['members']== None:
                wow[i]['members']=0
        wow.sort(key=lambda item: item.get("members"),reverse=True)
    if option == "Countdown":
        for i in range(len(wow)):
            if wow[i]['days_left'] > 1000:
                wow[i]['days_left']= 1001
        wow.sort(key=lambda item: item.get("days_left"))
    return wow


def seasonal_input(year,season,option):

    try:
        yay = jikan.season(year=year, season=season)
    except:
        wow = []
        return wow

    wow = yay['anime']
    wow.sort(key=lambda item: item.get("title"))

    today =datetime.today()

    for i in range(len(wow)):
        awareness = wow[i]['airing_start']
        if(awareness):
            d1 = datetime.fromisoformat(awareness)
            #wow[i]['airing_start'] = d1.strftime('%A')
            wow[i]['airing_start'] = d1.strftime('%A')
            wow[i]['abbrv'] = d1.strftime('%b %-d')

            future = d1.replace(tzinfo=None)
            #wiff = future - today
            #diff = wiff- timedelta(hours=7)
            #count_hours, rem = divmod(diff.seconds, 3600)
            if today>future:
                d1 = datetime.fromisoformat(awareness)
                while(today>future):
                    future = future+timedelta(days=7)
            wiff = future - today
            diff = wiff- timedelta(hours=7)
            count_hours, rem = divmod(diff.seconds, 3600)
            countdown = future-timedelta(hours=7)
            wow[i]['days_left']= int(diff.days)
            wow[i]['hours_left'] = int(count_hours)
            wow[i]['iso'] = countdown.isoformat()
        else:
            wow[i]['days_left'] = 1001
            wow[i]['hours_left'] = 1001

    if option == "Score":
        for i in range(len(wow)):
            if wow[i]['score']== None:
                wow[i]['score']=0
        wow.sort(key=lambda item: item.get("score"),reverse=True)
    if option == "Members":
        for i in range(len(wow)):
            if wow[i]['members']== None:
                wow[i]['members']=0
        wow.sort(key=lambda item: item.get("members"),reverse=True)
    if option == "Countdown":
        for i in range(len(wow)):
            if wow[i]['days_left'] > 1000:
                wow[i]['days_left']= 1001
        wow.sort(key=lambda item: item.get("days_left"))

    return wow

def ses():
    yay = jikan.season(year=2020, season='fall')
    wow = yay['anime']
    #wow.sort(key=lambda item: item.get("title"))
    return wow

def search():
    search_result = jikan.search('anime', 'Mushishi', page=2)
    return search_result

def animeinfo(ans):
    mushishi = jikan.anime(ans)
    return mushishi
    
def get_current_day():
    d1 =datetime.today()
    d2 =d1.strftime('%A')
    return d2

def get_current_year():
    d1 =datetime.today()
    d2 =d1.year
    return d2

def get_current_season():
    doy = datetime.today().timetuple().tm_yday
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    if doy in spring:
        season = 'Spring'
    elif doy in summer:
        season = 'Summer'
    elif doy in fall:
        season = 'Fall'
    else:
        season = 'Winter'
    
    return season

if __name__ == "__main__":
    #main() 
    asdf = ses()
    #for i in range(len(asdf)):
    #    if(asdf[i]['type']=='TV'):
    #        print(asdf[i]['title'])
    #        print(asdf[i]['image_url'])

    #for i in range(len(asdf)):
    #    if(asdf[i]['type']=='TV'):
    #        print(asdf[i]['title'])
    #        print(asdf[i]['image_url'])
    #        for j in range(0,len(asdf[i]['genres'])):
    #            print(asdf[i]['genres'][j]['name'])
    #            #continue
                

    a = asdf[0]['mal_id']
    #pprint(asdf[0]['mal_id'])
    #print("enter")
    #x = input()
    
    #now = datetime.now() 

    
    #pprint(asdf[0])

    ser = animeinfo(a)
    #pprint(ser,depth=1)
    pprint(ser['opening_themes'])
    pprint(ser['ending_themes'][0])
    print(type(ser['ending_themes'][0]))
    print(type(a))
    che = seasonal_input(2000,"fall","Title")
    pprint(che[0],depth=1)
    if(che):
        print("exists")
    else:
        print("no info")

    d1 =datetime.today()
    d2 =datetime.fromisoformat(asdf[0]['airing_start'])
    naive = d2.replace(tzinfo=None)
    diff = naive - d1
    

    count_hours, rem = divmod(diff.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    print(str(diff)+" "+str(count_hours)+" "+str(count_minutes)+" "+str(count_seconds))
    pprint(asdf[0],depth=1)
    asdf[0]['days_left'] = diff.days
    asdf[0]['hours_left'] = count_hours
    pprint(asdf[0],depth=1)
    qwer = diff - timedelta(hours=7)
    print(qwer.days)

    qr = naive.isoformat()
    #pprint(asdf[12])
    print(d2)
    print(d2+timedelta(days=7))

    ok = d2+timedelta(days=7)
    vaice = d2.replace(tzinfo=None)
    what = vaice - diff
    print(what)
    pprint(asdf[18]['title'])

    d3 = datetime.fromisoformat(asdf[18]['airing_start'])
    again= d3.replace(tzinfo=None)
    print(again)
    if d1>again:
        print("d1 greater")
        while(d1>again):
            again = again+timedelta(days=7)
    print(again)

    toiso = what.isoformat()
    delta = what - timedelta(days=7)
    print(delta.isoformat())

    alrighty = asdf
    for i in range(len(alrighty)):
        if alrighty[i]['score']== None:
            alrighty[i]['score']=0
    alrighty.sort(key=lambda item: item.get("score"))


    lmk = seasonal("Title")
    ##pprint(lmk[0],depth=1)
    #for i in range(len(lmk)):
    #    pprint(str(lmk[i]['members'])+" "+lmk[i]['title'])
    d1 = datetime.fromisoformat(asdf[0]['airing_start'])
    print(d1.strftime('%b %-d'))

    u = animeinfo(41380)
    pprint(u)        

    yesterday = datetime.today() - timedelta(days=1)
    today = datetime.today()
    tomorrow = datetime.today() + timedelta(days=1)    
    print(today)
    print(tomorrow)

    date_list = [yesterday,tomorrow,today]     
    print(date_list)   
    date_list.sort()
    print(date_list)

    x = get_current_day()
    print(x)
    x = get_current_year()
    print(x)
    doy = datetime.today().timetuple().tm_yday
    doys = datetime.today().timetuple()
    doyss = datetime.today()

    print(doy)
    print(doys)
    print(doyss)
    print(get_current_season)
    #d1 = datetime.datetime.strptime("2013-07-12T07:00:00Z","%Y-%m-%dT%H:%M:%SZ")
    pprint(seasonal_input(2021,'Winter','Score')[0])