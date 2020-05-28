class Edureka():
    def _init_(self):
        self.__pri=("i am private")
        self._pro=("i am protactive")
        self.pub=("i am public")

ob=Edureka()
print(ob.pub)
print(ob._pro)
print(ob.__pri)
