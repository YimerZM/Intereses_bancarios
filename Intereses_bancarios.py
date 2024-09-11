class InteresBancario:
    def ingresoDatos(self):
        capital = float(input("Ingrese el capital inicial: "))
        tasa_interes = float(input("Ingrese la tasa de interés (%): "))
        tiempo = float(input("Ingrese el tiempo en años: "))
        return capital, tasa_interes, tiempo

    def calcularInteres(self, capital, tasa_interes, tiempo):
        return capital * (tasa_interes / 100) * tiempo

if __name__ == '__main__':
    operacion = InteresBancario()
    capital, tasa, tiempo = operacion.ingresoDatos()
    interes = operacion.calcularInteres(capital, tasa, tiempo)
    print(f"El interés generado es: {interes:.2f}")
