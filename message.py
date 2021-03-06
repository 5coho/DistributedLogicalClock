"""
--Message Class file--

This class is the object that gets communicated between nodes. gets
pickled in the node class.
Has 3 main variables:
    senderName: Name of the sender nodes
    msg:        message to be sent
    clockCount: the senders Timestamp
straight forward class, basically just hold info used by the node_gui class.

"""


#Metadata
__author__          = "Scott Howes"
__credits__         = "Scott Howes"
__email__           = "showes@unbc.ca"
__python_version__  = "3.8.1"


#message class for demo
class message:


    #constructor
    def __init__(self):
        self.senderName = ""
        self.msg = ""
        self.clockCount = 0


    #self explanatory setters bellow
    def setSenderName(self, name):
        self.senderName = name


    def setMsg(self, msg):
        self.msg = msg


    def setClockCount(self, count):
        self.clockCount = count


    #self explanatory getters
    def getSenderName(self):
        return self.senderName


    def getMsg(self):
        return self.msg


    def getClockCount(self):
        return self.clockCount


    #python special methods
    #python representation
    def __repr__(self):
        return f"message({self.senderName}, {self.clockCount}, {self.msg})"


    #to string
    def __str__(self):
        return f"Message Object\nSender: {self.senderName}\nClock: {self.clockCount}\nMessage: {self.msg}"
