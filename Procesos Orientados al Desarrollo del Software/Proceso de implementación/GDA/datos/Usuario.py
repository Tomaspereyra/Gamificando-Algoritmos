class Usuario:
    def __init__(self, username, password, email, nombre, apellido):
      self.username = username
      self.password = password
      self.email = email
      self.nombre = nombre
      self.apellido = apellido

    def setIdUsuario(self, idUsuario):
        self.idUsuario=idUsuario

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username=username

    def getPassword(self):

        return self.password

    def setPassword(self, password):
        self.password=password

    def getEmail(self):

        return self.email

    def setEmail(self, email):

        self.email=email

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getId(self):
        return self.idUsuario

    def __str__(self):
        return str("Usuario: "+self.getUsername() + " Password: "+self.getPassword() + " E-mail: "+self.getEmail() + " Nombre: "+self.getNombre() + " Apellido: "+self.getApellido())
