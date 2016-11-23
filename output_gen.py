import string
import data as data

def print_dict():
    for keys, values in data.var_dict.items():
        print keys
        print values


def print_input():
   
    print ":::::INPUT::::"
    print "\nTo Prove:", data.input_to_prove
    print "\nPredicate Count:", data.input_predicate_count
    
    print "\nGiven Predicates:"
    for num in range(data.input_predicate_count):
        print data.input_predicate[num]


# isinstance        
def print_predicate_list():
       
    print ':: Predicate Parsed::::'
    
    for v in data.input_to_prove:
        print '\n',v.name, ' ', v.operatorPrev, ' ', v.operatorNext
        
        for j in v.params:        
            print 'Params->', j.name, ' ', j.is_const          
            

def print_predicate_list_all():
 
    #input_predicate.append(list(predicateList))
    
    print "\n\nPrint Predicate List All"
    pos = 0
    for k in data.input_predicate:
        pos = pos +1           
        print "\nCount->", pos       
        for v in k.predicateNodes:
            print 'New ===>' , v.name, ' ', v.operatorPrev, ' ', v.operatorNext
        
            for j in v.params:        
                print 'Params->', j.name, ' ', j.is_const
 

def print_a_clause(term):
    
    s = term.name+ ' '+ str(term.operatorPrev)+ ' '+ str(term.operatorNext)
    #print 'New ===>' , v.name, ' ', v.operatorPrev, ' ', v.operatorNext
    
    for j in term.params:        
        #print 'Params->', j.name, ' ', j.is_const
        s = s+ ' ('+ j.name+ ' '+ str(j.is_const) +')'
    print s    
                
    
def print_a_predicate(predVal):
    
    print '\n\n Print A Predicate\n\n'
    
    for v in predVal.predicateNodes:
        s = v.name+ ' '+ str(v.operatorPrev)+ ' '+ str(v.operatorNext)
        #print 'New ===>' , v.name, ' ', v.operatorPrev, ' ', v.operatorNext
        
        for j in v.params:        
            #print 'Params->', j.name, ' ', j.is_const
            s = s+ ' ('+ j.name+ ' '+ str(j.is_const) +')'
        print s    

def generateOutputString(term, value):
    
    printValue = value+' '+term.name+'(' 
    count = 0;
    
    for p in term.params:
        
        if count == 0:
            if p.name[0].islower() == True:
                printValue = printValue + '_'
            else:
                printValue = printValue + p.name   
        else:
            if p.name[0].islower() == True:
                printValue = printValue+ ', ' + '_'
            else:
                printValue = printValue+ ', ' + p.name    
        
        
        count = count + 1
    
    printValue = printValue + ')'
    return printValue
