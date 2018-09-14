'''
Provide trace output for simulation
'''
import net
import gate
import getopt
import time
import testbench
import imp
import sys

class trace:

    def __init__( self, trace_list, testbench):        
        self.trace_obj = []
        self.trace = []
        self.padded_names = []

        # build the list of objects to trace
        for n in trace_list:
            if n == '-':
                self.trace_obj.append( None )
            else: 
                # Ensure that regexps result in sensible net name orderings
                unsorted_list = []
                for i in testbench.get_nets(regexp="^%s$"%n,hier=True):
                    unsorted_list.append((i.fullname, i))
                for (name,net) in sorted(unsorted_list, reverse=True):
                    self.trace_obj.append(net) 
                    net.poc_prev_value = 'X'

    def log_header(self):
        # build an ASCII header file      
        header = []

        self.padded_names = []
        if self.trace_obj :
            l = max( [ len(i.fullname) for i in self.trace_obj if i!= None ] )

            for i in self.trace_obj:
                if i != None:
                    self.padded_names.append( (' '*(l -len(i.fullname))) + i.fullname)
                else:
                    self.padded_names.append( ' '*l)

            for i in xrange(0, l):
                t = [' ' *11]
                for n in self.padded_names:
                    t.append( n[i] )
                header.append(''.join(t))
            header.append( '-' * (10 + 1 + 1*len(self.padded_names)))

        return '\n'.join(header)
        
    def log_changes(self, ticker, po_events=[], disable_check=False, stats=None, traceon=True, force=False):
        # Check for 'print on change' at end of each event processing
        emit = force
        result = ""
        passes = 0
        fails = 0
        s = ['%9d: ' % ticker]        

        # check for any changes
        for n in self.trace_obj:
            if n != None:
                s.append(n.value)
                if n.value != n.poc_prev_value: 
                    emit = True
                    n.poc_prev_value = n.value
            else:
                s.append(' ')


        if po_events and not disable_check:
            strobe_result = ' PASS'
            for p in po_events:
                if p[0].value != p[1]:
                    strobe_result=" FAIL"
                    fails +=1
                else:
                    passes +=1 
            s.append(strobe_result)
            
        if stats:
            for k in stats:
                s.append("\n* %9d: %s="%(ticker,k))
                s.append(str(stats[k]))
                s.append(" Total=%d" %(sum(stats[k])))

        if emit and traceon:
            result = ''.join(s)
            self.trace.append(result)

        return (result, passes, fails)
        

    def log_footer(self):
        trace = []
        if self.trace_obj:
            trace.append( '-' * (10 + 1 + len(self.padded_names)))
        return ''.join(trace)


    def to_string(self, tail=0):
        trace = []
        trace.append( self.log_header())
        trace.append('\n')
        trace.append( '\n'.join(self.trace[-tail:]))
        trace.append('\n')
        trace.append( self.log_footer())


        return ''.join(trace)
