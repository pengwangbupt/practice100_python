#!/usr/bin/python
# coding:utf-8
'''
sunday
monday
tuesday
wednesday
thursday
friday
saturday

'''
def inputchar():
    ch = raw_input();
    return ch

def main():
    print "Please input the char of week:"
    week_ch = inputchar()
    
    if week_ch == 's':
        print "Please input the next char:"
        week_ch = inputchar()
        if week_ch == 'u':
            print "Sunday"
        elif week_ch == 'a':
            print "Saturday"
        else:
            print "------The input is error!!!"
    elif week_ch == 't':
        print "Please input the next char:"
        week_ch = inputchar()
        if week_ch == 'h':
            print "Thursday"
        elif week_ch == 'u':
            print "Tuesday"
        else:
            print "The input is error!!!"
    elif week_ch == 'm':
        print 'Monday'
    elif week_ch == 'f':
        print 'Friday'
    elif week_ch == 'w':
        print 'Wednesday'
    else:
        print "The input is error!!"
if __name__ == "__main__":
    main()
