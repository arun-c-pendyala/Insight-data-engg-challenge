
# coding: utf-8


import numpy as np
import collections as coll
import sys
import RunningMedian
import math



dict_zip = dict()

dict_date = dict()


def roundoff_median(num):
    if(num<0):  # as round(-1.5) = -2.0 , but requirements specify to round off to next dollar ,i.e,math.ceil(-ve)
        return  math.ceil(num)
    else:
        return round(num)

def check_date(date):
    month = int(date[:2])
    day = int(date[2:4])
    year = int(date[4:8])

    if(year>= 2018 or year< 1900): #check for valid year
        return False
    if(month> 12 or month<1): # check for valid month
        return False
    if(day>31 or day<1): # check for valid day
        return False

    if(month== 4 or month==6 or month ==9 or month==11): # these months have 30 days
        return (day<=30)
    elif(month==2):
        if(((year%4==0) and (year%100!=0)) or (year%400==0)): #check for leap year
            return (day<=29)
        else:
            return (day<=28)

    return True




with open(sys.argv[1]) as input_file:
    f_zip = open(sys.argv[2],"w+")
    f_date = open(sys.argv[3], "w+")
    zip_final_res = []
    
    for line in input_file:
        row = line.split('|')
        
        out_line_zip = ""
        amt_list_date = []
        amt_heap_zip = []
        
        if(row[0]!= ''  and row[14] != '' and row[15] == '' ): #ignore those rows with non empty OTHER_ID and empty CMTE_ID, TRANSACTION_AMT   
            zip = row[10]
            if(len(zip) >= 5 and zip[:5].isdigit()):    #check for  valid zipcodes
                out_line_zip = row[0] + "|" + zip[:5]  # select only first 5 digits
                zip_key = (row[0] , zip[:5]) # cmte_id and zip code
                
                if zip_key in dict_zip:
                    dict_zip[zip_key].add(int(row[14]))
                    amt_heap_zip = dict_zip[zip_key]
                    
                    
                    out_line_zip = out_line_zip + "|" + str(int(roundoff_median(amt_heap_zip.findMedian()))) + "|" + str(amt_heap_zip.size()) + "|" + str(amt_heap_zip.cur_sum())
                    
                    zip_final_res.append(out_line_zip)
                    
                else:
                    dict_zip[zip_key] = RunningMedian.RunningMedian()
                    dict_zip[zip_key].add(int(row[14])) # add contributions to the object
                    out_line_zip = out_line_zip + "|" + row[14] + "|" + "1" + "|" + row[14]
                    zip_final_res.append(out_line_zip)
        
        
            date_input = row[13]
            if(len(date_input) == 8 and date_input.isdigit() ):  # ignore invalid dates with length other than 8
                if(check_date(date_input)): # ignore malformed dates
                    date_key = (row[0],date_input[4:8] + date_input[:4] )  # converting date into yyyymmdd format , cmte_id and date as key
                    
                    if date_key in dict_date:
                        dict_date[date_key].append(int(row[14]))
                    
                    else:
                        dict_date[date_key] = [int(row[14])]
                                                
                        	
                    
    f_zip.write("\n".join(zip_final_res))


    out_dict_date = coll.OrderedDict(sorted(dict_date.items())) #sort first by alphabetical order and then by chronological order
    
    for key in out_dict_date.iterkeys():
        f_date.write(key[0] + "|" + (key[1][4:8] + key[1][:4]) + "|" +  str(int(roundoff_median(np.median(out_dict_date[key])))) + "|" + str(len(out_dict_date[key]))  + "|" + str(np.sum(out_dict_date[key])) + "\n" )

                    
f_date.close()      
f_zip.close()       



