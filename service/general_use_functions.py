class GeneralUseFunctions:
    @staticmethod
    def __merge(left : int, right : int, lst : list, reverse = False, key = lambda x : x, sort_function = lambda x,y: x < y):
        n_steps = right - left + 1
        st = left
        dr = (left+right+1) // 2
        new_lst = []
        for i in range(n_steps):
            if st >= (left+right+1) // 2:
                mn = lst[dr]
                dr += 1
            elif dr >= right+1:
                mn = lst[st]
                st += 1
            elif (sort_function(key(lst[dr]),key(lst[st])) and not reverse) or (sort_function(key(lst[st]),key(lst[dr])) and reverse):
                mn = lst[dr]
                dr += 1
            else:
                mn = lst[st]
                st += 1
            new_lst.append(mn)
        for i in range(len(new_lst)):
            lst[left+i] = new_lst[i]
    def __merge_sort(self, left : int, right : int, lst : list, reverse = False, key = lambda x : x, sort_function = lambda x,y: x < y):
        if left >= right:
            return
        middle = (left+right+1) // 2
        self.__merge_sort(left, middle-1, lst, reverse, key, sort_function)
        self.__merge_sort(middle, right, lst, reverse, key, sort_function)
        self.__merge(left, right, lst, reverse, key, sort_function)
    def true_merge_sort(self, lst : list, * ,reverse = False, key = lambda x : x, sort_function = lambda x,y: x < y):
        self.__merge_sort(0, len(lst)-1, lst, reverse, key, sort_function)
