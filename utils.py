import random
import string
import data as data

def term_match(term, predicateTerm):
    
    #print 'Inside Term Match term->', term.name, 'Predicate name->', predicateTerm.name
    
    validParam = 0        
    term_param_count = len(term.params)
                           
    cc = 0
    for p in predicateTerm.params:                            
        if p.is_const == True and term.params[cc].is_const == True and p.name != term.params[cc].name:
            #print 'p.name->', p.name, ' term.params[cc]->', term.params[cc].name, 'v.name->', predicateTerm.name
            break
        else:
            validParam = validParam + 1    
        
        cc = cc + 1
    
    if validParam == term_param_count:
        return True


def unify_args_not_implication_match(term, predicateTerm, predicateList):
    cc = 0   
    #print 'unify_args_not_implication_match term->', term.name, 'Predicate name->', predicateTerm.name
    #Resolve the parameters
    for p in predicateTerm.params:
            
        # since it is implication match assuming there are no constants on the right side
        if p.is_const == False and term.params[cc].is_const == False and p.name != term.params[cc].name:                                    
            for predicateTerm_1 in predicateList.predicateNodes:                                        
                if predicateTerm != predicateTerm_1:
                    for p_1 in predicateTerm_1.params:
                        if p_1.is_const == False and p_1.name == p.name: 
                            p_1.name = term.params[cc].name                                       
            p.name = term.params[cc].name
          
        elif p.is_const == False and term.params[cc].is_const == True:  
            for predicateTerm_1 in predicateList.predicateNodes:                                        
                if predicateTerm != predicateTerm_1:
                    for p_1 in predicateTerm_1.params:
                        if p_1.is_const == False and p_1.name == p.name: 
                            p_1.name = term.params[cc].name
            p.name = term.params[cc].name    
          
        cc = cc + 1
        
        # Assumption : such case would not come
        # elif p.is_const == True and term.params[cc].is_const == False:


def find_all_args_name(predicateList, args_name_dict):
    
    for predicateTerm_1 in predicateList.predicateNodes:
        
        for p_1 in predicateTerm_1.params:
                
            if p_1.is_const == False and p_1.name[0].islower() == True and args_name_dict.has_key(p_1.name) == False:
                
                args_name_dict[p_1.name] = True
            


def update_terms_with_same_var_name(term, predicateTerm, predicateList, name_to_check, args_name_dict):
    
    new_name = random.choice(string.ascii_lowercase)
    
    while(args_name_dict.has_key(new_name) == True):
        new_name = random.choice(string.ascii_lowercase)
    
    #print 'Name to check->', name_to_check, 'new name->', new_name
    
    for predicateTerm_1 in predicateList.predicateNodes:
        
        #if predicateTerm_1.operatorPrev != 2:
            
            for p_1 in predicateTerm_1.params:
                if p_1.is_const == False and p_1.name == name_to_check:
                    p_1.name = new_name
    

def update_terms_with_same_var_name_1(term, predicateTerm, predicateList, name_to_check, args_name_dict):
    
    do_update = False
    
    for pp in term.params:    
        if name_to_check == pp.name:
            do_update = True
        
    
    if do_update == True:
        new_name = random.choice(string.ascii_lowercase)
        
        while(args_name_dict.has_key(new_name) == True):
            new_name = random.choice(string.ascii_lowercase)
        
        #print 'Name to check->', name_to_check, 'new name->', new_name
        
        for predicateTerm_1 in predicateList.predicateNodes:
            
            #if predicateTerm_1.operatorPrev != 2:
                
                for p_1 in predicateTerm_1.params:
                    if p_1.is_const == False and p_1.name == name_to_check:
                        p_1.name = new_name
 
 
def update_param_name(predicateList, oldName, newName):
    
    for predicateTerm_1 in predicateList.predicateNodes:            
        for p_1 in predicateTerm_1.params:
            if p_1.is_const == False and p_1.name == oldName:
                #print 'p.name->', p.name, 'p_1.name->', p_1.name, 'term.params[cc].name->', term.params[cc].name
                p_1.name = newName
    
def update_param_name_randomly(predicateList, oldName, args_name_dict):

    new_name = random.choice(string.ascii_lowercase)
    
    while(args_name_dict.has_key(new_name) == True):
        new_name = random.choice(string.ascii_lowercase)
    
    for predicateTerm_1 in predicateList.predicateNodes:            
        for p_1 in predicateTerm_1.params:
            if p_1.is_const == False and p_1.name == oldName:
                p_1.name = new_name    
     
    
def update_terms_with_same_var_name_2(term, predicateTerm, predicateList, predicateParamName, termParamName, args_name_dict):
    
   
    if predicateParamName == termParamName:
        return
    else:
        if args_name_dict.has_key(termParamName) == False:
            update_param_name(predicateList, predicateParamName, termParamName)
        
        elif args_name_dict.has_key(termParamName) == True:
            update_param_name_randomly(predicateList, termParamName, args_name_dict)
            update_param_name(predicateList, predicateParamName, termParamName)
    
    

def unify_args_implication_match(term, predicateTerm, predicateList):
    
    #print 'unify_args_implication_match term->', term.name, 'Predicate name->', predicateTerm.name
    args_name_dict = {}
    find_all_args_name(predicateList, args_name_dict)
    
    cc = 0
    for p in predicateTerm.params:
                            
        # since it is implication match assuming there are no constants on the right side
        if p.is_const == False and term.params[cc].is_const == False and p.name != term.params[cc].name:                                    
            #Update the variable names of the other predicates
            
            #update_terms_with_same_var_name(term, predicateTerm, predicateList, p.name, args_name_dict)
            update_terms_with_same_var_name_2(term, predicateTerm, predicateList, p.name, term.params[cc].name, args_name_dict)
   
            for predicateTerm_1 in predicateList.predicateNodes:
                if predicateTerm_1.operatorPrev != 2:
                    
                    for p_1 in predicateTerm_1.params:
                        if p_1.is_const == False and p_1.name == p.name:
                            #print 'p.name->', p.name, 'p_1.name->', p_1.name, 'term.params[cc].name->', term.params[cc].name
                            p_1.name = term.params[cc].name
            
            p.name = term.params[cc].name

        elif p.is_const == True and term.params[cc].is_const == False:
                                            
            #Update the variable names of the other predicates
            for predicateTerm_1 in predicateList.predicateNodes:
                if predicateTerm_1.operatorPrev != 2:
                    
                    for p_1 in predicateTerm_1.params:
                        if p_1.is_const == False and p_1.name == p.name: 

                            #should be value assignment for term
                            p_1.name = term.params[cc].name   
            
            #should be value assignment for term
            #print 'DICTIONARY p.name->', p.name, ' value->', term.params[cc].name
            
            if p.name.islower():
                data.var_dict[p.name] = term.params[cc].name 
                p.name = term.params[cc].name
            
            elif term.params[cc].name.islower():
                data.var_dict[term.params[cc].name ] = p.name 
                term.params[cc].name = p.name
        
        elif p.is_const == False and term.params[cc].is_const == True:
            
            update_terms_with_same_var_name_1(term, predicateTerm, predicateList, p.name, args_name_dict)
                                            
            #Update the variable names of the other predicates
            for predicateTerm_1 in predicateList.predicateNodes:
                if predicateTerm_1.operatorPrev != 2:
                    
                    for p_1 in predicateTerm_1.params:
                        if p_1.is_const == False and p_1.name == p.name: 

                            p_1.name = term.params[cc].name 
            
            #print 'DICTIONARY p.name->', p.name, ' value->', term.params[cc].name
            
            if p.name.islower():
                data.var_dict[p.name] = term.params[cc].name 
                p.name = term.params[cc].name
            
            elif term.params[cc].name.islower():
                data.var_dict[term.params[cc].name ] = p.name 
                term.params[cc].name = p.name
        
        
        cc = cc + 1 