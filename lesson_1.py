class A():
    ALL_OBJ = []
    def __init__(self, a, b=0):
        self.__a = a # PRIVATE
        self._b = b  # PROTECTED
        self.c = 5
        A.ALL_OBJ.append(self)

    def __str__(self):
        return f"Обект A: {self.__a}, {self._b}"

    def __get_a(self):
        return self.__a

    def __set_a(self):
        pass

    my_setter = property(__get_a(), __set_a())


obj_a = A(10)
print(obj_a)
obj_a_2 = A(20)
print(obj_a_2)

# for elem in A.ALL_OBJ:
#     print(elem)

