class VersionManager:
    def __init__(self, version='0.0.1'):
        self.default = version
        self.version = version
        if(self.version.startswith('.')):
            self.version = self.version[1:]
            self.default = self.version
        for letter in self.version:
            if letter.isalpha():
                raise Exception('Error occured while parsing version!')

        if(len(self.version) == 3):
            self.version = self.version+'.0'
        if(len(self.version) == 2):
            self.version = self.version+'0.0'
        elif(len(self.version) == 1):
            self.version = self.version+'.0.0'
        elif(len(self.version) == 0):
            self.version = self.version+'.0.0.1'
        elif(len(self.version) == 4):
            self.version = self.version+'0'
        elif(len(self.version) > 5):
            self.version = self.version[:5]
            self.default = self.version[:5]

    def release(self):
        return self.version

    def major(self):
        self.default = self.version
        l = self.version.split('.')
        l[0] = int(l[0])+1
        l[0] = str(l[0])
        l[1] = '0'
        l[2] = '0'
        lf = '.'.join(l)
        self.version = lf
        return self

    def minor(self):
        self.default = self.version
        l = self.version.split('.')
        l[1] = int(l[1])+1
        l[1] = str(l[1])
        l[2] = '0'
        lf = '.'.join(l)
        self.version = lf
        return self

    def patch(self):
        self.default = self.version
        l = self.version.split('.')
        l[2] = int(l[2])+1
        l[2] = str(l[2])
        lf = '.'.join(l)
        self.version = lf
        return self

    def rollback(self):
        if(self.rollback == self.version):
            raise Exception('Cannot rollback!')
        self.version = self.default
        return self


print(VersionManager("1.d.3").patch().release())
