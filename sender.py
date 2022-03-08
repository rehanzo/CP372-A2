from common import *
from NetworkSimulator import *

class sender:
    RTT = 20
    
    def isCorrupted (self, packet):
        '''Checks if a received packet (acknowledgement) has been corrupted
        during transmission.
        Return true if computed checksum is different than packet checksum.
        '''
        # return packet.c != checksumCalc(packet.data)
        return False

    def isDuplicate(self, packet):
        '''checks if an acknowledgement packet is duplicate or not
        similar to the corresponding function in receiver side
        '''
        # return packet.a != self.sequenceNum
        return False
            
 
    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''
        self.sequenceNum = self.sequenceNum * -1 + 1

        return 

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: "+str(self.entity))

    def init(self):
        '''initialize the sequence number and the packet in transit.
        Initially there is no packet is transit and it should be set to None
        '''
        self.sequenceNum = 0
        self.packet = None

        return

    def timerInterrupt(self):
        '''This function implements what the sender does in case of timer
        interrupt event.
        This function sends the packet again, restarts the time, and sets
        the timeout to be twice the RTT.
        You never call this function. It is called by the simulator.
        '''
        self.RTT *= 2
        self.networkSimulator.startTimer(A, self.RTT)
        self.networkSimulator.udtSend(A, self.packet)

        return


    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        '''
        if self.packet is None:
            self.packet = Packet(self.sequenceNum, 0, checksumCalc(message.data), message.data)
            self.networkSimulator.udtSend(A, self.packet)
            self.networkSimulator.startTimer(A, self.RTT)


        return
 
    
    def input(self, packet):

        '''If the acknowlegement packet isn't corrupted or duplicate, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.

        In the case of duplicate or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.
        '''

        if not(self.isDuplicate(packet) or self.isCorrupted(packet)):
            self.networkSimulator.stopTimer(A)
            self.getNextSeqNum()
            self.packet = None
        return 

