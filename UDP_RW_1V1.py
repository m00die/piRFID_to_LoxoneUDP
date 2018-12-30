import socket

xSendenOk = 0
xNewRFID = 0
iSendeVersuch = 0
i = 1
#MESSAGEold =
#rfidtag = "a"
#MESSAGE = 0


while (i == 1):
    print ("******************************************")
    print ("Warten auf RFID Tag")

    if (xSendenOk == 1):
        MESSAGEold = MESSAGE
    else:
        MESSAGEold ="12"

    print ("Letzter RFID Tag", MESSAGEold)
    print ("")

    rfidtag = input()
    str_rfid = str(rfidtag)
    MESSAGE = str_rfid
    
           
    if (MESSAGEold != MESSAGE):
        xNewRFID = 1

    if (xNewRFID == 1):
        xSendenOk = 0
        while (iSendeVersuch < 10 and xSendenOk == 0):

            iSendeVersuch = iSendeVersuch + 1

            UDP_IP = "192.168.100.77" #.77 Loxone
            UDP_PORT = 1234
            MESSAGE = str_rfid
            
            print ("")
            print ("#####################")
            print ("UDP target IP:", UDP_IP)
            print ("UDP target port:", UDP_PORT)
            print ("RFID Tag:", MESSAGE)
            print ("#####################")
            print ("")

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

            sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock2.bind( ("",4321) )
            datareturn, addr = sock2.recvfrom(1024)
            print (datareturn)

            if MESSAGE == datareturn:
                xSendenOk = 1
                print ("")
                print ("*******************************************")
                print ("RFID Chip gelesen und von Loxone bestaetigt!")
                print ("*******************************************")
                print ("")
                print ("")

            else:
                xSendenOk = 0
                print ("")
                print ("*********************************")
                print ("RFID von Loxone nicht akzeptiert!")
                print ("*********************************")
                print ("")
                print ("")
#        print ("RFID konnte nicht gelesen werden!")


