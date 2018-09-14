import gate

class pin :
    '''
    Pin is a terminal which can drive or receive signals from a net.
    '''
    def __init__ (self, name, parent=None, netconn=None,  value='Z', strength=0, direction=gate.IN):
        if parent:
            self.fullname = '.'.join([parent.fullname(), name])
        else:
            self.fullname = name
        self.name = name        
        self.parent = parent
        self.netconn = netconn
        self.state = (value, strength)
        self.direction = direction

    def to_str(self):
        return "%s %s "%(self.fullname, self.netconn.fullname), self.state
        

