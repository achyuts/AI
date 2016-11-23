import sys
import re
import hw2cs561s16 as main
import output_gen as helper
import data as data


def parse_input_predicate(predicate, position):

             
    predicate_split = re.split(r'[;,\s()]\s*', predicate)

    for v in predicate_split:
        if v == '':
            predicate_split.remove(v)
  
    isPredicateName = True
    predicateName = None;
    invr = False
    
    isPredicateArgs = False
    predicateArgs = []
    
    predicateList =[]
    pOp = 3
    
    isImplicationCheck = False
        
    for v in predicate_split:
        
        if isPredicateName:
            #print "Predicate name->", v
            predicateName = v
            isPredicateName = False
            isPredicateArgs = True
            predicateArgs = []
            continue
        
        if v == '&&' or v == '=>':
            
            op = 3
            
            if v == '&&':
                op = 1
            elif v == '=>':
                op = 2
                isImplicationCheck = True
            
            isPredicateArgs = False
            invr = False
            
            if predicateName[0] == '~':
                invr = True
                predicateName = predicateName[1:]
            
            #print 'Predicate Args->0', predicateArgs[0].name, '1->', predicateArgs[1].name    
            predicateNode = main.PredicateNode(predicateName, predicateArgs, pOp ,op)
            predicateList.append(predicateNode)
            
            isPredicateName = True
            pOp = op
            
        if isPredicateArgs:
            
            #print "Inside args search->", v
            
            if re.match(r'[A-Z]', v[0], 0):
                                
                valueNode = main.ValueNode(True, v)
                predicateArgs.append(valueNode)
                
            else:
                                
                valueNode = main.ValueNode(False, v)
                predicateArgs.append(valueNode)        
    
    predicateNode = main.PredicateNode(predicateName, predicateArgs, pOp, 3)
    predicateList.append(predicateNode)
    
    predicateVar = main.Predicate(predicateList, isImplicationCheck)
    data.input_predicate.append(predicateVar)



def parse_input():
    
        
    lines = [line.strip() for line in open(str(sys.argv[2]),"r")]
        
    line_no = 0
    predicate_count_calc = 0
    
    for line in lines:
        
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        
        if line_no == 0:
                        
            parse_predicate_to_prove(line)
                  
        elif line_no == 1:
            
            data.input_predicate_count = int(line) 
            
                   
        else:
           
            parse_input_predicate(line, line_no-2)
         
        line_no = line_no + 1
        
    #helper.print_predicate_list_all()     
    return




def parse_predicate_to_prove(predicate):
    
    global input_to_prove
    
    #print "Predicate To Prove" 
              
    predicate_split = re.split(r'[;,\s()]\s*', predicate)
    
    for v in predicate_split:
        if v == '':
            predicate_split.remove(v)
    
    #print predicate_split
    
    isPredicateName = True
    predicateName = None;
    invr = False
    
    isPredicateArgs = False
    predicateArgs = []
    
    pOp = 3;

    for v in predicate_split:
        #print v
        if isPredicateName:
            #print "Predicate name->", v
            predicateName = v
            isPredicateName = False
            isPredicateArgs = True
            predicateArgs = []
            continue
        
        if v == '&&' or v == '=>':            
            op = 3            
            if v == '&&':
               op = 1
            elif v == '=>':
                op = 2    
            
            isPredicateArgs = False
            invr = False
            
            if predicateName[0] == '~':
                invr = True
                predicateName = predicateName[1:]
            
            #print 'Predicate Args->0', predicateArgs[0].name, '1->', predicateArgs[1].name    
            predicateNode = main.PredicateNode(predicateName, predicateArgs, pOp ,op)
            data.input_to_prove.append(predicateNode)
            
            isPredicateName = True
            pOp = op
            
        if isPredicateArgs:
            
            #print "Inside args search->", v
            
            if re.match(r'[A-Z]', v[0], 0):
                                
                valueNode = main.ValueNode(True, v)
                predicateArgs.append(valueNode)
                
            else:
                                
                valueNode = main.ValueNode(False, v)
                predicateArgs.append(valueNode)
                    
    
    predicateNode = main.PredicateNode(predicateName, predicateArgs, pOp, 3)    
    data.input_to_prove.append(predicateNode)                    
    #helper.print_predicate_list()