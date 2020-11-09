from namedlist import namedlist


class Queue():
    _Node = namedlist('Node', 'value next')
    __slots__ = ['_front', '_back']


    def __init__(self, it=None):
        self._front = None
        self._back = None
        if it is not None:
            self.push(it)

    def push(self, value):
        nuevo = Queue._Node(value, self._back)
        if self.is_empty():
            self._front = nuevo
            self._back = self._front
        self._back = nuevo

    def is_empty(self):
       return self._back is None

    def contador(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.contador(node.next)

    def __len__(self):
        return self.contador(self._back)


    def pop(self):
        if not self.is_empty():
            aux = self._back
            temp = self._back.next
            temp2 = self._front
            while True:
                if aux is not temp2:
                    if temp != temp2:
                        aux = temp
                        temp = temp.next
                    else:
                        self._front = aux
                        self._front.next = None
                        return
                else:
                    return self.clear()
        return ("Cola vacia")

    
    def copy2(self, node, new_node):
        if node.next is not None:
            node = node.next
            new_node.next = Queue._Node(node.value, None)
            a = new_node.next
            return self.copy2(node, a)
        
        

    def copy(self, node):
        new_queue = Queue()
        if not self.is_empty():
            new_node = Queue._Node(node.value, None)
            new_queue._back = new_node
            self.copy2(node, new_node)
        if not new_queue.is_empty():
            while node.next is not None:
                node = node.next
        new_queue._front = node
        return new_queue
    


    def copiar(self):
        return self.copy(self._back)



    def __eq__(self, other):
        x= self._back
        y= other._back
        while x is not None and y is not None:
            if x.value != y.value:
                return False
            x= x.next
            y= y.next
        return x is None and y is None

    def __repr__(self):
        valor = []
        node = self._back
        while node is not None:
            valor.append(node.value)
            node = node.next
        return "Queue([" + ", ".join(repr(x) for x in valor) + "])"
                
        
    def adelante(self):
        if not self.is_empty():
            return self._front.value
        else:
            print("Cola vacia")
        
    def clear(self):
        if not self.is_empty():
            self._back = self._front = self._front.next
        else:
            print("Cola sin elementos")
            

""" VENTAJAS RECURSIVIDAD: Solucion de un problema recurrente, necesitan
menor cantidad de lineas de codigo.
DESVENTAJA RECURSIVIDAD: Mayor necesidad de espacio en la memoria.
VENTAJA ITERACION: Mayor eficiencia en la utilizacion de memoria.
DESVENTAJA ITERACION: Codigo menos legible que la recursividad, mayor utilizacion
de bucles. """



