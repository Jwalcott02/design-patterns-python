class Memento:
    def __init__(self, state):
        self.state = state


    def get_saved_state(self):
        return self.state

class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self,state):
        print(f"Setting state to {state}")
        self._state = state

    def save_to_memento(self):
        print("Saving to memento...")
        return Memento(self._state)
    
    def restore_from_memento(self,memento):
        self._state = memento.get_saved_state()
        print(f"State afer restoring {self._state}")

class CareTaker:
    def __init__(self):
        self.mementos = []

    def add_mementos(self,memento):
        self.mementos.append(memento)

    def get_mementos(self, index):
        return self.mementos[index]
    
originator = Originator()
caretaker = CareTaker()

originator.set_state("State1")
caretaker.add_mementos(originator.save_to_memento())

originator.set_state("State2")
caretaker.add_mementos(originator.save_to_memento())

originator.set_state("State3")

originator.restore_from_memento(caretaker.get_mementos(0))