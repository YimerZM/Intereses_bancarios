from Intereses_bancarios import InteresBancario

if __name__ == '__main__':
    operacion = InteresBancario()
    capital, tasa, tiempo = operacion.ingresoDatos()
    interes = operacion.calcularInteres(capital, tasa, tiempo)
    print(f"El interés generado es: {interes:.2f}")