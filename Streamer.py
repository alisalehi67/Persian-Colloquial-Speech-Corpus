from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'xxx'
csecret = 'xxx'
atoken = 'xxx'
asecret = 'xxx'

class listener(StreamListener):

    def on_data(self, data):
        try: #using try to get an if there is a problem otherwise the code keeps running
            print (data)
            #to filter out just the text of the tweets
            # tweet = data.split(',"text":"')[1].split('","source')[0] #[1]give me the right side of the split i.e. beginnig.[0] is the left side
            # print(tweet)
            # onlytweets = ':::'+tweet
            # saveFile = open('twitFA2.csv', 'a')
            # saveFile.write(onlytweets)
            # saveFile.write('\n')
            # # for tweets in saveFile:
            # #     tweets.decode('utf-8')
            # saveFile.close()
            # return True

            saveFile = open('abcd.csv', 'a') #makes a csv file that appends all tweets to that file
            saveFile.write(data) #writes the collected data on the file
            saveFile.write('\n') #write each file in a new line
            # for eachline in saveFile:
            #     eachline.decode('unicode-escape')
            saveFile.close() #closes the file after writing on it
            return True
        except BaseException as e: #throwing an error in case of any problems e.g. internet stops working
            print ('failed on data', str(e))
            time.sleep(5)


    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ['ا','آ','ب','پ','ث','ج','چ','ح','خ','د','ذ','ر','ز','ژ','س','ش','ص','ض','ط','ظ','ع','غ','ف',
                              'ق','ک','گ','ل','م','ن','و','ه','ی','أ','إ','ي','ئ','ؤ','ك'], languages=["fa"], encoding='utf8' )
                                #spitting out all tweets with Persian characters in them

