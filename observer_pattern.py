class Observer:
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)
    
    def notifiy(self, message):
        for observer in self._observers:
            observer.update(message)

class Student(Observer):
    def update(self, message):
       print(f"Student wacthed {message}") 

class Faculty(Observer):
    def update(self, message):
       print(f"Facultly wacthed {message}") 

#Subject
fau_podcast_service = Subject()

#Observers
student = Student()
faculty = Faculty()

fau_podcast_service.subscribe(student)
fau_podcast_service.subscribe(faculty)

fau_podcast_service.notifiy("Breaking news: Observer pattern is awesome !!!")