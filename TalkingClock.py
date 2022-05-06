import inflect
from datetime import datetime
class TalkingClock(object):
    def __init__(self, currenttime):  # validating and initializing the instance variable
        self.hh = currenttime.hour
        self.mm = currenttime.minute

    # Human readable format of clock display function
    def humanFriendlyText(self):
        if self.mm==0:  # for case 1: 1:00 One o'clock
            string = self.time2WordConvert(self.hh)
            readAs='O\'clock'
            minute=None
        elif self.mm<=30: # for case 2: 13:05 Five past one
            if self.mm==30: # for case 2.1:	13:30 Half past one
                minute='Half'
            else:
                minute=self.time2WordConvert(self.mm) #conerting minute to word format
            readAs='past'
            hour=self.time2WordConvert(self.hh%12)  #converting hour to 12 hour clock  word format
        else:      # for case 3: 13:35 Twenty five to two
            minute = self.time2WordConvert(60-self.mm) # remaining minutes calculation in word format
            readAs = 'to'
            hour = self.time2WordConvert((self.hh % 12)+1) #converting hour to 12 hour clock word format
        return(minute + ' '+readAs+' '+hour)



        #string=self.time2WordCovert(self.hh)

# time2WordConvert function for converting number format to word format.
    def time2WordConvert(self,number):
        numtowordconverter=inflect.engine() #Create an inflect engine
        wordform=numtowordconverter.number_to_words(number) #convert number to Word format represent - for connecting words
        wordform=wordform.replace('-', ' ').capitalize() #replace - with space and capitaliz first letter of string
        return(wordform)

if __name__ == '__main__':
    clk=TalkingClock(datetime.now())
    print(clk.humanFriendlyText())
