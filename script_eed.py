class eed:
    
    def __init__(self, s1, s2, print_steps = False):
        for s in [s1,s2]:
            if (not isinstance(s, str)):
                raise ValueError("the value %s is not of type String!"%(s))
        self.ps = print_steps
        self.__string_1=s1.lower()
        self.__string_2=s2.lower()
    
    def get_string_1(self):
        if self.__string_1:
            return self.__string_1
        return False
        
    def get_string_2(self):
        if self.__string_2:
            return self.__string_2
        return False
    
    def set_string_1(self, new_str):
        if (not isinstance(new_str, str)):
            raise ValueError("the value %s is not of type String"%(new_str))
        self.__string_1 = new_str.lower()
        
    def set_string_2(self, new_str):
        if (not isinstance(new_str, str)):
            raise ValueError("the value %s is not of type String"%(new_str))
        self.__string_2 = new_str.lower()

    def __create_matrix(self):
        for col_s2 in range(len(self.__string_2)+1):
            row_val = []
            for row_s1 in range(len(self.__string_1)+1):
                row_val.append("")
            self.__eed_matrix.append(row_val)
        for col_s2 in range(len(self.__string_2)+1):
            row_val = []
            for row_s1 in range(len(self.__string_1)+1):
                row_val.append("")
            self.__eed_operations.append(row_val)
            
    def create_edit_distance(self):
        self.__eed_matrix = []
        self.__eed_operations = []
        self.__create_matrix()
        self.__create_empty_rows()
        self.__create_empty_column()
        for row in range(1,len(self.__eed_matrix)):  
            for col in range(1,len(self.__eed_matrix[row])):
                if self.__check_case_nothing(row, col):
                    continue
                self.__check_rest(row, col)
        self.__eed = self.__eed_matrix[len(self.__eed_matrix)-1][len(self.__eed_matrix[0])-1]
        self.__calculate_eed_factor()
        self.__calculate_pfeed_factor()
        self.__print_result()
        
    def __print_result(self):
        print("String 1: "+self.__string_1.upper()+" to String 2: "+self.__string_2.upper())
        print("") 
        print("")
        print("Edit Steps") 
        print("")
        self.__print_edit_step()
        print(" ")
        self.__print_matrix_eed()
        print(" ")
        print(" ")
        self.__print_matrix_operations()
        print(" ")
        print("Mininmal number of operations") 
        print("")
        print(str(self.__eed))
        print("")
        print("Extended edit distance") 
        print("")
        print(str(self.__extended_edit_distance))
        print("")
        print("Parameter Free Extended edit distance") 
        print("")
        print(str(round(self.__para_free_extended_edit_distance,2)))
    
    def __print_matrix_operations(self):
        row_labels = [" "]
        col_labels = "         "
        for char in self.__string_2:
            row_labels.append(char.upper())
        for char in self.__string_1:
            col_labels+="%s   " % (char.upper())
        print(col_labels)
        for row_label, row in zip(row_labels, self.__eed_operations):
            print('%s [%s]') % (row_label, ' '.join('%03s' % i.upper() for i in row))
        print(" ")
        print("R = Replacement / N = Nothing / I = Insertion / D = Deletion")
        print(" ")
        
    
    def __print_edit_step(self):
        list_string_from = []
        list_string_to = []
        for char in self.__string_1:
            list_string_from.append(char.upper())
        for char in self.__string_2:
            list_string_to.append(char.upper())
        index_row = len(list_string_to)
        index_col = len(list_string_from)
        num_operation = 1
        n_operation = self.__eed
        print("Original String")
        print(list_string_from)
        print(" ")
        while(n_operation>0):
            operation = self.__eed_operations[index_row][index_col]
            if operation == "i":
                if index_row>0:
                    index_row-=1
                new_char = list_string_to.pop()
                list_string_from.insert(index_col, new_char)
                print("Operation Nr.%s: INSERTION of %s at Index %s")%(num_operation, new_char, index_col)
                print(list_string_from)
                print(" ")
                n_operation-=1
                num_operation+=1
            elif operation == "d":
                popped_string  = list_string_from.pop(index_col-1)
                index_col-=1
                print("Operation Nr.%s: DELETION of %s at Index %s")%(num_operation, popped_string, index_col)
                print(list_string_from)
                print(" ")
                n_operation-=1
                num_operation+=1
            elif operation == "r":
                new_char = list_string_to.pop()
                char = list_string_from[index_col-1]
                list_string_from[index_col-1]=new_char
                index_col-=1
                if index_row>0:
                    index_row-=1
                print("Operation Nr.%s: REPLACEMENT of %s with %s at Index %s")%(num_operation, char.upper(),
                                                                          new_char, index_col)
                print(list_string_from)
                print(" ")
                n_operation-=1
                num_operation+=1
            elif operation == "n":
                if index_row>0:
                    index_row-=1
                index_col-=1
                list_string_to.pop()
    
    def __print_header_top(self):
        list_c = []
        list_empty = []
        list_c.append(" ")
        list_empty.append(" ")
        for char in self.__string_1:
            list_c.append(char)
            list_empty.append(" ")
        print(list_c)
        print(list_empty)
    
    def __calculate_factor(self):
        self.__total_number_char = len(self.__string_1)+len(self.__string_2)
        set_char = set(self.__string_1+self.__string_2)
        self.__total_num = 0 
        for char in set_char:
            num_s1 = 0
            num_s2 = 0
            for char_s1 in self.__string_1:
                if char_s1 == char:
                    num_s1 = num_s1+1
            for char_s2 in self.__string_2:
                if char_s2 == char:
                    num_s2 = num_s2+1
            if num_s1<num_s2:
                self.__total_num = self.__total_num + num_s1
            else:
                self.__total_num = self.__total_num + num_s2
    
    def __calculate_pfeed_factor(self):
        nc = self.__total_number_char
        tn = self.__total_num
        f = float(1-(float(2*tn)/nc))
        self.__para_free_extended_edit_distance = float(self.__eed+f)

    def __calculate_eed_factor(self):
        self.__calculate_factor()
        self.__extended_edit_distance = self.__eed+(self.__total_number_char-(2*self.__total_num))
    
    def __print_matrix_eed(self):
        row_labels = [" "]
        col_labels = "         "
        for char in self.__string_2:
            row_labels.append(char.upper())
        for char in self.__string_1:
            col_labels+="%s   " % (char.upper())
        print(col_labels)
        for row_label, row in zip(row_labels, self.__eed_matrix):
            print('%s [%s]') % (row_label, ' '.join('%03s' % i for i in row))
                
    def __check_rest(self, row, col): 
        self.__lowest_val = 0
        self.__val_above = self.__eed_matrix[row-1][col]
        self.__val_left = self.__eed_matrix[row][col-1]
        self.__val_left_above = self.__eed_matrix[row-1][col-1]
        if self.__val_above < self.__val_left:
            self.__lowest_val = self.__val_above
            self.__eed_operations[row][col] = "i"
        else:
            self.__lowest_val = self.__val_left
            self.__eed_operations[row][col] = "d"
        if self.__val_left_above<=self.__lowest_val:
            self.__lowest_val=self.__val_left_above
            self.__eed_operations[row][col] = "r"
        self.__eed_matrix[row][col]=self.__lowest_val+1
        self.__eed_operations[0][0] = "n"
              
    def __check_case_nothing(self, row, col):
        s1 = self.__string_1
        s2 = self.__string_2
        if s1[col-1]==s2[row-1]:
            self.__eed_matrix[row][col]=self.__eed_matrix[row-1][col-1]
            self.__eed_operations[row][col] = "n"
            return True
    
    def __create_empty_rows(self):
        __num=0
        for col in self.__eed_matrix[0]:
            self.__eed_matrix[0][__num]=__num
            self.__eed_operations[0][__num]= "d"
            __num+=1
    
    def __create_empty_column(self):
        __num=0
        for col in range(len(self.__eed_matrix)):
            self.__eed_matrix[__num][0]=__num
            self.__eed_operations[__num][0]= 'i'
            __num+=1

e1 = eed(s1="Wirtschaft",s2="Kunst", print_steps=True)
e1.create_edit_distance()
