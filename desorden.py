import random
import time

class desorden():
    datos = []

    def __init__  (self, elementos : int):
        self.datos = list(range(elementos))

    def __len__ (self):
        return len(self.datos)

    def __str__ (self):
        return str(self.datos)

    def __rango (self, argumentos):
        if len(argumentos) > 1:
            fin = argumentos[1]
            if fin > len(self.datos):
                fin = len(self.datos)
        else:
            fin = len(self.datos)
        if len(argumentos) > 0:
            inicio = argumentos[0]
            if inicio < 0:
                inicio = 0
        else:
            inicio = 0
        tramo = self.datos[inicio:fin]
        return inicio, fin, tramo


    def invertir (self, *args):
        inicio, fin, tramo = self.__rango(args)
        self.datos = self.datos[:inicio] + tramo[::-1] + self.datos[fin:]


    def barajar (self, *args):
        inicio, fin, tramo = self.__rango(args)
        random.shuffle(tramo)
        self.datos = self.datos[:inicio] + tramo + self.datos[fin:]


    def ordenar (self, *args):
        inicio, fin, tramo = self.__rango(args)
        tramo.sort()
        self.datos = self.datos[:inicio] + tramo + self.datos[fin:]


    def repetir (self, elementos=1, *args):
        inicio, fin, tramo = self.__rango(args)
        longitud = len(tramo)
        repeticiones = random.sample(tramo, elementos)
        tramo = [random.choice(repeticiones) for _ in range(longitud)]
        self.datos = self.datos[:inicio] + tramo + self.datos[fin:]


    def cambiar (self, pct=0.1, *args):
        if not (0.0 < pct < 1.0):
            raise Exception("pct fuera de rango")
        inicio, fin, tramo = self.__rango(args)
        lp = random.sample(range(len(tramo)), int(pct * len(tramo)))
        lv = [tramo[lp[c]] for c in range(len(lp))]
        random.shuffle(lv)
        for c in range(len(lv)):
            tramo[lp[c]] = lv[c]
        self.datos = self.datos[:inicio] + tramo + self.datos[fin:]


    def rotar (self, unidades=1, *args):
        inicio, fin, tramo = self.__rango(args)
        if unidades >= fin - inicio:
            raise Exception("Desplazamiento inválido")
        self.datos = (self.datos[:inicio] + tramo[unidades:] + tramo[:unidades] + self.datos[fin:])

def main():

    cuantos = 5_000_000
    minimo  = 1_000_000
    maximo  = 4_000_000

    t1 = time.process_time()
    lista = desorden(cuantos)
    print("Crear    %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    t1 = time.process_time()
    lista.invertir(minimo, maximo)
    print("Invertir %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    t1 = time.process_time()
    lista.barajar(minimo, maximo)
    print("Barajar  %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    t1 = time.process_time()
    lista.repetir(100_000, minimo, maximo)
    print("Repetir  %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    t1 = time.process_time()
    lista.cambiar(0.5, minimo, maximo)
    print("Cambiar  %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    t1 = time.process_time()
    lista.rotar(2, minimo, maximo)
    print("Rotar    %d. %f" % (len(lista), time.process_time() - t1))

    lista = desorden(cuantos)
    lista.barajar()
    t1 = time.process_time()
    lista.ordenar(minimo, maximo)
    print("Ordenar  %d. %f" % (len(lista), time.process_time() - t1))

if __name__ == "__main__":
    main()