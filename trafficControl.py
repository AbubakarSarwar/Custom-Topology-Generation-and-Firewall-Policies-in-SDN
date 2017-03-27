#!/usr/bin/python
## Created by Muhammad Shahriyar Sheikh 
##            Hatim Ali Asghar
##            Abu Bakar Sarwar



import Tkinter
from Tkinter import *
import tkMessageBox
import tkSimpleDialog

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

root = Tk()



def add_new(textToDisplay):
    
    b = Label(root,text = textToDisplay, fg = "Black", font = "Fixedsys")
    b.pack()



def emptyNet():
    
    #root = Tk()
    
    
    #"Create an empty network and add nodes to it."

    #####################
    hostCount=0
    a=1 #Loop Variable to assign hosts of hostCount

    ipstring = "" 
    i=1 #Loop Variable to assign ip to hosts

    switchCount=0
    b=1 #Loop Variable for allocating switchCount switches
    j=1 #Loop Variable for assigning switches of switchCount

    hostLink=0 #Number of host to be connected in link
    switchLink=0 #Number of switch to be connected in link
    hostCounter = 0 #For it to stop asking for input when the number of hosts are completed

    #####################

    add_new("This window shows all\nthe progress the user generates \n\n\n\n\n\n\n")
    #roo = Tk()
    #roo.withdraw()

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    
    #hostCount=input('Enter the total number of hosts ')
    
    hostCount = tkSimpleDialog.askinteger("Number of Hosts","Enter the number of hosts? ")
    add_new("Number of hosts added are %s"%hostCount)   

    hosts=[Mininet(controller=Controller)] #List for hosts  
    #Loop for allocation host count hosts to list
    
    hosts.append(Mininet(controller=Controller)) #To avoid h0


    while a<=hostCount: 
    hosts.append(Mininet(controller=Controller))
    a=a+1
    #Loop to assign hosts of hostCount
    

    
    
    while i<=hostCount:
    k=str(i)
    #ipstring = raw_input("Enter an ip for host h"+k + " ")
    ipstring = tkSimpleDialog.askstring("IP for host h%s"%k,"Enter an ip for host h%s (Must be of xx.xx.xx.xx format) "%k)
    hosts[i]=net.addHost('h'+k,ip=ipstring)
    i=i+1
    info('Host added h'+k)
    info(' with ip of ' + ipstring)
    add_new("Host added h{0} with ip of {1}".format(k,ipstring))    
    info('\n')

#switchCount=input('Enter the total number of switches: ')
    switchCount = tkSimpleDialog.askinteger("Switches","Enter the total Number of switches")
    switches=[Mininet(controller=Controller)] #List for Switches
    add_new("Number of switches added = %s"%switchCount)

    
    switches.append(Mininet(controller=Controller)) #To avoid s0
    #Loop for allocating switchCount switches
    while b<=switchCount:
    switches.append(Mininet(controller=Controller))
    b=b+1


    
    #loop for assigning switches of switchCount
    while j<=switchCount:
    l=str(j)
    switches[j]=net.addSwitch( 's'+l)
    j=j+1
    info('Switch added s'+l)
    info('\n')
    

        
    #Loop for making links

    
    while hostCounter < hostCount or hostLink == -1:
        #hostLink=input("\nEnter host number that you want to link(-1 to finish or press cancel)\n")
    hostLink = tkSimpleDialog.askinteger("Linking ...","Enter the host number that you want to link (-1 to finish or press cancel)")
    if hostLink ==-1:
       break
        #switchLink=input("Enter switch number that you want to link it with\n")
    switchLink = tkSimpleDialog.askinteger("Linking ...","Enter switch number that you want to link h{0} with ".format(hostLink))
    
    add_new("\nEstablishing connectiong between desired host/switch")   
    #Establishing connectiong between desired host/switch
        net.addLink(hosts[hostLink],switches[switchLink])
    m=str(hostLink)
    n=str(switchLink)       
    info( "Link created between h"+m )
        info( " and s"+n)
    add_new("Link created between h{0} and s{1}".format(m,n))
    
    hostCounter = hostCounter + 1

    add_new("\n You can use the Command prompt from this point onwards. THANKS\n")
    info( '\n*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()
    exit()
    

if __name__ == '__main__':

    
    root.geometry('+900+50')
    root.minsize(420,600)
    root.wm_title("Progress Report")

    setLogLevel( 'info' )
    emptyNet()
    exit()
    #roo = mainloop()
    #roo.quit()
