import urllib
import httplib
import json
import datetime, time
import pylab as pl
import pylab as pl1

xaxis = [0]*1200
yaxis = [0]*1200

hashtag2 = "#brandbowl"
hashtag1 = "#SB49"
start_date = datetime.datetime(2015,2,1, 16,0,0)
increment = 3.0
count = 0
while count < 1200:
	end_date = start_date + datetime.timedelta(seconds = increment)
	mintime = int(time.mktime(start_date.timetuple()))
	maxtime = int(time.mktime(end_date.timetuple()))

	API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
	host = 'api.topsy.com'
	url = '/v2/content/tweets.json'

    #########   set query parameters
	params = urllib.urlencode({'apikey' : API_KEY, 'q' : hashtag1, 'mintime': str(mintime), 'maxtime': str(maxtime), 'new_only': '1', 'include_metrics':'1', 'limit': 500})
	


    #########   create and send HTTP request
	req_url = url + '?' + params
	req = httplib.HTTPConnection(host)
	req.putrequest("GET", req_url)
	req.putheader("Host", host)
	req.endheaders()
	req.send('')


	#########   get response and print out status
	resp = req.getresponse()
	print (resp.status, resp.reason)


	#########   extract tweets
	resp_content = resp.read()
	ret = json.loads(resp_content.decode())
	tweets = ret['response']['results']['list']
	print(tweets.__len__())
	if(tweets.__len__() == 500):
		stri = "oops!"
	xaxis[count] = (tweets.__len__())/increment
	start_date = start_date + datetime.timedelta(seconds = increment)
	count = count + 1
	
start_date = datetime.datetime(2015,2,1, 16,0,0)
increment = 3.0
count = 0
while count < 1200:
	end_date = start_date + datetime.timedelta(seconds = increment)
	mintime = int(time.mktime(start_date.timetuple()))
	maxtime = int(time.mktime(end_date.timetuple()))

	API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
	host = 'api.topsy.com'
	url = '/v2/content/tweets.json'

    #########   set query parameters
	params = urllib.urlencode({'apikey' : API_KEY, 'q' : hashtag2, 'mintime': str(mintime), 'maxtime': str(maxtime), 'new_only': '1', 'include_metrics':'1', 'limit': 500})
	


    #########   create and send HTTP request
	req_url = url + '?' + params
	req = httplib.HTTPConnection(host)
	req.putrequest("GET", req_url)
	req.putheader("Host", host)
	req.endheaders()
	req.send('')


	#########   get response and print out status
	resp = req.getresponse()
	print (resp.status, resp.reason)


	#########   extract tweets
	resp_content = resp.read()
	ret = json.loads(resp_content.decode())
	tweets = ret['response']['results']['list']
	print(tweets.__len__())
	yaxis[count] = (tweets.__len__())/increment
	start_date = start_date + datetime.timedelta(seconds = increment)
	count = count + 1

pl.plot(xaxis,yaxis,'ro')
pl.plot(xaxis,yaxis)
pl.xlabel("Rate of tweets for next most popular tweet : #SB49")
pl.ylabel("Rate of tweets for most popular tweet : #Brandbowl")
pl.show()

pl1.plot(xaxis,yaxis,'ro')
pl1.xlabel("Rate of tweets for next most popular tweet : #SB49")
pl1.ylabel("Rate of tweets for most popular tweet : #Brandbowl")
pl1.show()
