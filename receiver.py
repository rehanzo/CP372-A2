from common import *

class receiver:
    def isCorrupted(self, packet):
        ''' Checks if a received packet has been corrupted during transmission.
        Return true if computed checksum is different than packet checksum.'''

        return
   
    def isDuplicate(self, packet):
        '''checks if packet sequence number is the same as expected sequence number'''
        return packet.seqNum == self.expectedSeqNum
    
    def getNextExpectedSeqNum(self):
        '''The expected sequence numbers are 0 or 1'''
        self.expectedSeqNum = not self.expectedSeqNum
        return
    
    
    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: "+str(self.entity))


    def init(self):
        '''initialize expected sequence number'''
        self.expectedSeqNum = 0;
        return
         

    def input(self, packet):
        '''This method will be called whenever a packet sent 
        from the sender arrives at the receiver. If the received
        packet is corrupted or duplicate, it sends a packet where
        the ack number is the sequence number of the  last correctly
        received packet. Since there is only 0 and 1 sequence numbers,
        you can use the sequence number that is not expected.
        
        If packet is OK (not a duplicate or corrupted), deliver it to the
        application layer and send an acknowledgement to the sender
        '''


        return
