def remove_match_char(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[i]:
                c=list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1+ ["*"] + list2
                return [list3 ,True] 
    
    list3 = list1 + ["*"] + list2
    return [list3 , False]

if __name__=="__main__":
    p1 = input("Player 1 name : \n")
    p1 = p1.lower()
    p1 = p1.replace(" ", "")          # Corrected to replace instead of just calling replace
    p1_list = list(p1)
    
    p2 = input("Player 2 name : \n")
    p2 = p2.lower()
    p2 = p2.replace(" ", "")
    p2_list = list(p2)
    
    proceed = True
    
    while proceed:
        ret_list = remove_match_char (p1_list,p2_list)
        con_list = ret_list[0]        #Retrieves the first element of the returned list from the remove_match_char function. 
        proceed = ret_list[1]         #Retrieves the second element of the returned list 
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]
        
    count = len(p1_list) + len(p2_list)
    
    result = ["Friends" , "Love" , "Affectionate" , "Marriage" , "Enemy" , "Siblings"]
    
    while len(result)>1:
        split_index = (count % len(result) - 1)
        if split_index >=0:
            right = result[split_index + 1:]   #right is assigned the portion of the result list starting from the index after split_index to the end of the list.
            left = result[:split_index]        #left is assigned the portion of the result list from the beginning of the list to the split_index
            result = right + left           
        else:
            result = result[:len(result) - 1]   #In this case, it means there is no circular shift to perform, and the last element of the result list is removed.This is done by assigning a slice of the result list that excludes the last element back to the result variable.
      
    print ("Relationship Status:" , result[0])
    
    
    
    