"""
Antonio Aguilar Salgado

REGLAS DEL ARCHIVO TXT
1. estados 
2. alfabeto
3. estado inicial
4. estados de aceptacion (separados por espacios)
5. estados de transcision (estado simbolo estado)
"""
class automataFD:
    def __init__(self, from_file=False, file_name=None):
        if from_file and file_name:
            self.load_from_file(file_name)
        else:
            self.Q = self.definir_estados()
            self.SIGMA = self.definir_alfabeto()
            self.DELTA = self.definir_transicion()
            self.START_STATES, self.ACCEPT_STATES = self.set_start_start_accept()
        self.EstadoActual = None

    def set_start_start_accept(self):
        while True:
            start = input("dame el estado inicial del automata: ")
            accept = input('Dame el o los estados de aceptación: ').split()
            if (start in self.Q) and (set(accept).issubset(set(self.Q))):
                return start, accept
            else:
                print("Tafavor dame el START_STATE y el ACCEPT_STATES que deben estar en Q:{}.".format(self.Q))

    def definir_estados(self):
        Q_in = input("Dame el conjunto de estados, separados por espacios en blanco: ").split()
        print("STARES : {}".format(Q_in))
        return Q_in

    def definir_alfabeto(self):
        SIGMA_in = input("Dame el alfabeto del automata, separados por espacios en blanco: ").split()
        print("ALPHABET : {}".format(SIGMA_in))
        return SIGMA_in

    def definir_transicion(self):
        transi_dict = {q: {a: "JACHI" for a in self.SIGMA} for q in self.Q}
        for key, dic_val in transi_dict.items():
            print("Estoy en el estado {}. Escribir JACHI si no existe estado de transicion: ".format(key))
            for alphabet_in, transi_state in dic_val.items():
                transi_dict[key][alphabet_in] = input("Estoy en {} y veo {} a que estado voy:  ".format(key, alphabet_in))
        print("TRANSITION FUNCTION Q X SIGMA -> Q")
        print("\tCURRENT STATE \t INPUT ALPHABET \t NEXT STATE")
        for key, dic_val in transi_dict.items():
            for alphabet_in, transi_state in dic_val.items():
                print("\t{}\t\t{}\t\t{}".format(key, alphabet_in, transi_state))
        return transi_dict

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.Q = lines[0].strip().split()
            self.SIGMA = lines[1].strip().split()
            self.START_STATES = lines[2].strip()
            self.ACCEPT_STATES = lines[3].strip().split()
            self.DELTA = {}
            for state in self.Q:
                self.DELTA[state] = {}
            for line in lines[4:]:
                estado_actual, simbolo, estado_siguiente = line.strip().split()
                self.DELTA[estado_actual][simbolo] = estado_siguiente

    def checar_estado_aceptacion(self):
        if self.EstadoActual in self.ACCEPT_STATES:
            return True
        else:
            return False

    def recorrer_automata(self, w):
        self.EstadoActual = self.START_STATES
        for x in w:
            self.EstadoActual = self.DELTA[self.EstadoActual][x]
            if self.EstadoActual == 'JACHI':
                return False
        return self.checar_estado_aceptacion()


def main():
    while True:
        choice = input("¿Deseas crear un nuevo autómata (c) o leer desde archivo (l)? ").lower()
        if choice == 'l':
            file_name = input("Proporcione el nombre del archivo: ")
            m = automataFD(from_file=True, file_name=file_name)
        else:
            m = automataFD()

        while True:
            input_w = list(input("Proporcione la cadena: "))
            if m.recorrer_automata(input_w):
                print("Cadena Aceptada")
            else:
                print("Cadena Rechazada")

            again = input("¿Quieres evaluar otra cadena con este automata? (s/n): ").lower()
            if again != 's':
                break

        new_automata = input("¿Quieres crear un nuevo automata? (s/n): ").lower()
        if new_automata != 's':
            break


if __name__ == "__main__":
    main()
