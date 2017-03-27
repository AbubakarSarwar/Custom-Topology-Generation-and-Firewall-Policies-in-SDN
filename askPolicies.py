##Created by Muhammad Shahriyar Sheikh '_'
##           Hatim Ali Asghar .-.
##           AbuBakar Sarwar ._.


import csv
import tkMessageBox
import tkSimpleDialog
from Tkinter import *




###################################
root = Tk()
root.withdraw()
noOfPolicies = 0
host1=0
host2=0
macstring = "00:00:00:00:00:0"

###################################


writer = csv.writer(open('firewall.csv','wb'))
writer.writerow(["id","mac_0","mac_1"])

noOfPolicies = tkSimpleDialog.askinteger("Number of Policies","Enter the number of policies you wish to apply on the controller ? ")


for i in range(0,noOfPolicies):
    hoststr = tkSimpleDialog.askstring("Traffic Generation Scheme","Type in x,y which means x will not be able to ping y (Like 1,2)")
    writer.writerow([str(i+1),macstring+hoststr[0:1],macstring+hoststr[-1:]])
