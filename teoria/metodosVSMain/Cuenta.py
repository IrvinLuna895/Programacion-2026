class Menu:
    def __init__(self, mensaje, fecha, tipo, saldo):
        self.mensajeBienvenida = mensaje
        self.fechaCreacion = fecha
        self.tipoCuenta = tipo
        self.saldo = saldo

    def darBienvenida(self):
        print(self.mensajeBienvenida)

    def despliegaOpciones(self):
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver información de la cuenta")

        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            self.saldo += cantidad
            print("Depósito exitoso. Nuevo saldo:", self.saldo)

        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print("Retiro exitoso. Nuevo saldo:", self.saldo)
            else:
                print("Fondos insuficientes.")

        elif opcion == "3":
            print("--- Información de la cuenta ---")
            print("Fecha de creación:", self.fechaCreacion)
            print("Tipo de cuenta:", self.tipoCuenta)
            print("Saldo actual:", self.saldo)

        else:
            print("Opción no válida.")
