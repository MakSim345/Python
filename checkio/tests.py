    print "string to check:", _string_to_check
    ret_value = True

    stack_open = []
    array_of_open = ['{', '(', '[']
    array_of_close = ['}', ')', ']']
    
    dict_all = {'{':'}', '(':')', '[':']'}

    for i in _string_to_check:
        # print i        
        if i in array_of_open:
            stack_open.append(i)
            # print stack_open            
        #endif
        if i in array_of_close:
            # print "close:", i
            current_open = stack_open.pop()
            # print "open:", dict_all[current_open]
            if not i == dict_all[current_open]:
                print i, "not equal to", dict_all[current_open]
                ret_value = False
            #endif
        #endif
    #end_for
    print "return", ret_value
    return ret_value
