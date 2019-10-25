class eed:
    
    def __init__(self, s1, s2):
        self.__string_1=s1.lower()
        self.__string_2=s2.lower()
        self.__create_matrix()
                    
    def __create_matrix(self):
        self.__eed_matrix = []
        for col_s2 in range(len(self.__string_2)+1):
            row_val = []
            for row_s1 in range(len(self.__string_1)+1):
                row_val.append("")
            self.__eed_matrix.append(row_val)
        
    def _create_eed(self):
        self.__create_empty_rows()
        self.__create_empty_column()
        for row in range(len(self.__eed_matrix)):  
            if row == 0:
                continue 
            for col in range(len(self.__eed_matrix[row])):
                if col == 0:
                    continue 
                if self._check_case_nothing(row, col):
                    continue
                self.check_rest(row, col)
        self.__eed = self.__eed_matrix[len(self.__eed_matrix)-1][len(self.__eed_matrix[0])-1]
        self.__calculate_eed_factor()
        self.__calculate_pfeed_factor()
        self.__print_result()
        
    def __print_result(self):
        print("Edit Distance Matrix") 
        print("")
        print("")
        print("String 1: "+self.__string_1+" to String 2: "+self.__string_2)
        print("") 
        self.__print_matrix()
        print("")
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
    
    def _print_string_list(self):
        list_c = []
        list_c.append(" ")
        list_c.append(" ")
        for char in self.__string_1:
            list_c.append(char)
        print(list_c)
            
    
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
    
    def __print_matrix(self):
        num = 0
        for row in range(len(self.__eed_matrix)):
            list_d = []
            list_c = self.__eed_matrix[row]
            
            for char in list_c:
                list_d.append(str(char))
                
            print(list_d)
                
    def check_rest(self, row, col): 
        self.__lowest_val = 0
        self.__val_above = self.__eed_matrix[row-1][col]
        self.__val_left = self.__eed_matrix[row][col-1]
        self.__val_left_above = self.__eed_matrix[row-1][col-1]
        if self.__val_above < self.__val_left:
            self.__lowest_val = self.__val_above
        else:
            self.__lowest_val = self.__val_left
        if self.__val_left_above<self.__lowest_val:
            self.__lowest_val=self.__val_left_above
        self.__eed_matrix[row][col]=self.__lowest_val+1
              
    def _check_case_nothing(self, row, col):
        s1 = self.__string_1
        s2 = self.__string_2
        if s1[col-1]==s2[row-1]:
            self.__eed_matrix[row][col]=self.__eed_matrix[row-1][col-1]
            return True
    
    def __create_empty_rows(self):
        __num=0
        for col in self.__eed_matrix[0]:
            self.__eed_matrix[0][__num]=__num
            __num=__num+1
        
    
    def __create_empty_column(self):
        __num=0
        for col in range(len(self.__eed_matrix)):
            self.__eed_matrix[__num][0]=__num
            __num=__num+1

e1 = eed("kleider","leid")
e1._create_eed()
        
        