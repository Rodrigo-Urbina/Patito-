# Tabla

class tabla (object) :

    def __init__ (self, data_type, value = None, param = False, dim = 0, matrix = 0):
        self.data_type = str(data_type)
        self.value = value
        self.param = param
        self.dim = dim
        self.matrix = matrix
