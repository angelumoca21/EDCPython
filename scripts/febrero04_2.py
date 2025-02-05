# Generar clase Cuenta: beneficiario,saldo
# Al realizar la instancia de cuenta se mostrara un mensaje donde se indique el nombre del beneficiario y el monto de apertura.
# 1er método: retirar(monto), haciendo verificación de saldo suficiente y que la cuenta este activa.
# 2do método: depositar(monto), verificar que la cuenta este activa.
# 3er activarCuenta
# 4er desactivarCuenta

class Cuenta:
    def __init__(self,beneficiario,saldo):
        self.beneficiario = beneficiario
        self.saldo = saldo
        self.estado = True
        print(f"{self.beneficiario} abrió su cuenta con ${self.saldo} de saldo.")

    def retirar(self,monto):
        if self.estado:
            if self.saldo > monto:
                print(f"Se retirara ${monto} de la cuenta de {self.beneficiario}.")
                self.saldo = self.saldo - monto
                print(f"El saldo después del retiro es de ${self.saldo}.")
            else:
                print("No tiene saldo suficiente para realizar la transacción.")
        else:
            print(f"{self.beneficiario}, no se puede realizar el movimiento ya que tu cuenta esta inactiva.")

    def depositar(self,monto):
        if self.estado:
            print(f"Se depositará ${monto} a la cuenta de {self.beneficiario}.")
            self.saldo = self.saldo + monto
            print(f"El saldo después del deposito es de ${self.saldo}.")
        else:
            print(f"{self.beneficiario}, no se puede realizar el movimiento ya que tu cuenta esta inactiva.")

    def activarCuenta(self):
        if self.estado:
            print(f"{self.beneficiario} tu cuenta ya estaba activada.")
        else:
            self.estado = True
            print(f"{self.beneficiario} tu cuenta ha sido activada.")

    def desactivarCuenta(self):
        if self.estado:
            self.estado = False
            print(f"{self.beneficiario} tu cuenta ha sido desactivada.")
        else:
            print(f"{self.beneficiario} tu cuenta ya estaba desactivada.")