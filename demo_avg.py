import datetime
print("Internship task for Vaizle")
def mainFunct():
    dict = {'2020-10-20':10 }
    print('Initial Date and its value',dict)

    n = 1;
    for i in range(n):
        print('Please Input a Date and its Value')
        k = (input("Enter key Date in format YYYY-MM-DD:"))
        v = int(input("Enter key value:"))
        dict.update({k:v})
        print('Current Dict',dict)
    print("Total no of entries:", len(dict))
    def returnSum(myDict):
        sum = 0
        for i in myDict:
            sum = sum + myDict[i]
        return sum
    print ("Sum of Values:", returnSum(dict))

    def returnmean(myDict):
        filtered_vals= [v for _, v in myDict.items() if v !=0]
        average = sum(filtered_vals)/ len(filtered_vals)
        return average
    print ("Avg values:", returnmean(dict))

    def returnmeanDate(myDict):
        print("Init Average Date")
        for i in myDict.keys():
            i=0
            year, month , day = map(int, date_entry.split('_'))
            date1 = datetime.date(date, month, day)
        print("date1", returnmeanDate(dict))

print("Sorry, But i cant figure it out, and i dont have any idea about the time limit so im submiting is now.")
"""sum = 0
        for i in myDict:
            sum = int(sum)/float(len(myDict))
        return sum
    print ("Sum:", returnmean(dict))"""

"""mean = sum(keys)/float(len(myDict))
        return mean
        print("Mean", returnmean(dict))"""
"""def avg_value():
        for dicts in a:
            for values in a:
                dicts[values] = int(dicts[values])
                calc= sum(values)
                print(calc)
                return
avg_value()"""
        

    
"""def avg_date():
    e= {}
    for k in a.items():
        if k.len()!= 0:
               
            e= sum(k)/float(len(k))
            print('Average of Date :', e)
avg_date();"""


"""df = .DataFrame(a)
def get_avg(d):
    for k,v in a.iteritems():
       df = sum(k)/float(len(k))
print(get_avg(d))"""

        
"""def average():
    for k,v in a.iteritems():
        average[k] = sum(v)/float(len(v))
print(average[k])"""        

mainFunct()
