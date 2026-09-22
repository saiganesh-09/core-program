'''11. Using abc module: 
        • Create an abstract class Shape with area(), perimeter() 
        • Implement Circle, Rectangle, Triangle Demonstrate: 
        • why base class should NOT contain calculation logic 
        • what happens if a subclass fails to implement one of the methods '''
# from abc import ABC,abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius*self.radius
#     def perimeter(self):
#         return 2*math.pi* self.radius
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.lenght=length
#         self.width=width
#     def area(self):
#         return self.lenght*self.width
#     def perimeter(self):
#         return 2*(self.lenght+self.width)
# class Triangle(Shape):
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def perimeter(self):
#         return self.a+self.b+self.c
#     def area(self):
#         s=self.perimeter()/2
#         return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
# c=Circle(5)
# r=Rectangle(10,5)
# t=Triangle(5,6,7)
# print('Circle Area:',c.area())
# print('Circle Perimeter:',c.perimeter())
# print(Shape.__abstractmethods__)
# print('Rectangle Area:',r.area())
# print('Recangle perimeter:',r.perimeter())
# print('Triangle Area:',t.area())
# print('Triangle Perimeter:',t.perimeter())
'''12. Design an abstract class PaymentGateway with: 
    • authenticate() 
    • pay(amount) 
    • refund(amount) Implement subclasses: 
    • UPIPayment • CardPayment 
    • NetBankingPayment 
    Show how abstraction helps your main program call payment 
            methods without caring about the payment type. '''
# from abc import ABC,abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def authenticate(self):
#         pass
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def refund(self,amount):
#         pass
# class UPIPayment(PaymentGateway):
#     def authenticate(self):
#         print("UPI Authentication Succesfully")
#     def pay(self,amount):
#         print(f'Paid {amount} paid successfully using UPI')
#     def refund(self,amount):
#         print(f'{amount} refunded successfully using UPI')
# class CardPayment:
#     def authenticate(self):
#         print('Card authentication Successfully')
#     def pay(self,amount):
#         print(f'Paid {amount} using Card')
#     def refund(self,amount):
#         print(f'Refunded {amount} using Card')
# class Netbanking:
#     def authenticate(self):
#         print('Netbanking authentication Succesfully')
#     def pay(self,amount):
#         print(f'Paid {amount} using Netbanking')
#     def refund(self,amount):
#         print(f'Refunded {amount} using Netbanking')
# def make_payment(payment,amount):
#     payment.authenticate()
#     payment.pay(amount)
#     payment.refund(amount)
# u=UPIPayment()
# c=CardPayment()
# n=Netbanking()
# make_payment(u,1000)
# print()
# make_payment(c,1000)
# print()
# make_payment(u,1000)
# print()
'''13. Create:
    • Abstract class VehicleControl with methods accelerate(), brake(), steer() 
    • Implement CarControl, BikeControl, TruckControl 
            Demonstrate calling each through a single interface. '''
# from abc import ABC,abstractmethod
# class VehicleControl:
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def brake(self):
#         pass
#     @abstractmethod
#     def steer(self):
#         pass
# class CarControl(VehicleControl):
#     def accelerate(self):
#         print('Car is accelerating')
#     def brake(self):
#         print('Car having brake')
#     def steer(self):
#         print('Car having steering')
# class BikeControl(VehicleControl):
#     def accelerate(self):
#         print('Bike is accelerating')
#     def brake(self):
#         print('Bike having brake')
#     def steer(self):
#         print('Bike dont having steering')
# class TruckControl(VehicleControl):
#     def accelerate(self):
#         print('Truck is accelerating')
#     def brake(self):
#         print('Truck having brake')
#     def steer(self):
#         print('Truck having steering')
# def control_vehicles(vehicle):
#     vehicle.accelerate()
#     vehicle.brake()
#     vehicle.steer()
# c=CarControl()
# b=BikeControl()
# t=TruckControl()
# print("Car:")
# control_vehicles(c)
# print("\n Bike:")
# control_vehicles(b)
# print("\n Truck:")
# control_vehicles(t)
'''14. Create an abstract class DatabaseDriver with: 
    • connect()
    • execute(query) 
    • close() Implement concrete drivers: 
    • MySQLDriver 
    • PostgresDriver 
    • SQLiteDriver 
    Show how abstraction helps switch databases without rewriting main code.'''
# from abc import ABC,abstractmethod
# class DatabaseDriver(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     def execute(self,query):
#         pass
#     def close(self):
#         pass
#
# class MySQLDriver(DatabaseDriver):
#     def connect(self):
#         print('My SQL Driver connect DatabaseDriver')
#     def execute(self,query):
#         print(f'My SQL Driver execute {query} DatabaseDriver')
#     def close(self):
#         print('My SQL Driver close DatabaseDriver')
#
# class PostgresDriver(DatabaseDriver):
#     def connect(self):
#         print('PostgresDriver Driver connect DatabaseDriver')
#     def execute(self,query):
#         print(f'PostgresDriver Driver execute {query} DatabaseDriver')
#     def close(self):
#         print( 'PostgresDriver Driver close DatabaseDriver')
#
# class SQLiteDriver(DatabaseDriver):
#     def connect(self):
#         print('SQLiteDriver connect DatabaseDriver')
#     def execute(self,query):
#         print(f'SQLiteDriver execute {query} DatabaseDriver')
#     def close(self):
#         print('SQLiteDriver close DatabaseDriver')
#
# def run_database(driver):
#     driver.connect()
#     driver.execute('SELECT*FROM query')
#     driver.close()
# m=MySQLDriver()
# p=PostgresDriver()
# s=SQLiteDriver()
# print('My SQL:')
# run_database(m)
# print('\nPostgreSQL:')
# run_database(p)
# print('\nSQLite:')
# run_database(s)
'''15. Design a class ReportGenerator (abstract) with: 
    • load_data() 
    • process() 
    • export() 
    Implement: 
    • PDFReport 
    • ExcelReport 
    Demonstrate how abstraction enforces a multi-step structure. '''
# from abc import ABC,abstractmethod
# class ReportGenerator(ABC):
#     @abstractmethod
#     def load_data(self):
#         pass
#     @abstractmethod
#     def process(self):
#         pass
#     @abstractmethod
#     def export(self):
#         pass
# class PDFReport(ReportGenerator):
#     def load_data(self):
#         print('loading data for a PDF Report')
#     def process(self):
#         print('Processing for a PDF Report')
#     def export(self):
#         print('Exporting data for a PDF Report')
#
# class ExcelReport(ReportGenerator):
#     def load_data(self):
#         print('loading data for a Excel Report')
#     def process(self):
#         print('Processing for a Excel Report')
#     def export(self):
#         print('Exporting data for a Excel Report')
# def generate_report(report):
#     report.load_data()
#     report.process()
#     report.export()
# p=PDFReport()
# e=ExcelReport()
# print("Pdf:")
# generate_report(p)
# print("Excel:")
# generate_report(e)

'''16. Create an abstract class RobotCommand with: 
    • execute() 
    • undo() 
    Implement: 
        • PickCommand 
        • PlaceCommand 
        • MoveCommand Demonstrate how abstraction cleanly represents 
                commands without revealing details. '''
# from abc import ABC,abstractmethod
# class RobotCommand(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#     @abstractmethod
#     def undo(self):
#         pass
# class PickCommand:
#     def execute(self):
#         print('Pick Command executed successfully')
#     def undo(self):
#         print('Pick Command Undo successfully')
# class PlaceCommand:
#     def execute(self):
#         print('Place Command executed successfully')
#     def undo(self):
#         print('Place Command Undo successfully')
# class MoveCommand:
#     def execute(self):
#         print('Move Command executed successfully')
#     def undo(self):
#         print('Move Command Undo successfully')
# def commands(command):
#     command.execute()
#     command.undo()
# pc=PickCommand()
# p=PlaceCommand()
# m=MoveCommand()
# print('PickCommand:')
# commands(pc)
# print('\nPlaceCommand:')
# commands(p)
# print('\nMoveCommand:')
# commands(m)
'''17. Create an abstract class MLModel with: 
    • train(data) 
    • predict(x) 
    • evaluate(test_set) 
        Implement models: 
            • LinearRegressionModel- some different logic 
            • DecisionTreeModel – some logic Show how a generic training 
                loop works for any model without caring about details. '''
# from abc import ABC, abstractmethod
# class MLModel(ABC):
#     @abstractmethod
#     def train(self, data):
#         pass
#     @abstractmethod
#     def predict(self, x):
#         pass
#     @abstractmethod
#     def evaluate(self, test_set):
#         pass
#
# class LinearRegressionModel(MLModel):
#     def train(self, data):
#         print("Training Linear Regression model")
#     def predict(self, x):
#         print(f"Linear Regression prediction for {x}")
#     def evaluate(self, test_set):
#         print("Evaluating Linear Regression model")
#
# class DecisionTreeModel(MLModel):
#     def train(self, data):
#         print("Training Decision Tree model")
#     def predict(self, x):
#         print(f"Decision Tree prediction for {x}")
#     def evaluate(self, test_set):
#         print("Evaluating Decision Tree model")
# # Generic training loop
# def train_model(model, data):
#     model.train(data)
# # Create objects
# linear = LinearRegressionModel()
# tree = DecisionTreeModel()
#
# # Same function, different models
# train_model(linear, "Training Data")
# train_model(tree, "Training Data")
#
# # Prediction
# linear.predict(100)
# tree.predict(100)
#
# # Evaluation
# linear.evaluate("Test Data")
# tree.evaluate("Test Data")
'''18. Design a system without abstraction first: 
    • Write separate functions for EmailSender, SMSSender, PushSender 
        Show how the main program becomes a mess with constant if/else. 
    Then: 
        • Redesign using an abstract base class Notifier. '''
'''19. Create an abstract MediaPlayer with: 
        • load() 
        • play() 
        • stop() 
    Implement: 
        • MP3Player 
        • WAVPlayer 
        • AACPlayer Demonstrate calling each via a unified interface. '''
# from abc import ABC,abstractmethod
# class MediaPlayer(ABC):
#     @abstractmethod
#     def load(self):
#         pass
#     @abstractmethod
#     def play(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class MP3Player(MediaPlayer):
#     def load(self):
#         print('Mp3Player loaded the songs')
#     def play(self):
#         print('Mp3Player played the songs')
#     def stop(self):
#         print('Mp3Player stops the songs')
#
# class WAVPlayer(MediaPlayer):
#     def load(self):
#         print('WAVPlayer loaded the songs')
#     def play(self):
#         print('WAVPlayer played the songs')
#     def stop(self):
#         print('WAVPlayer stops the songs')
#
# class AACPlayer(MediaPlayer):
#     def load(self):
#         print('AACPlayer loaded the songs')
#     def play(self):
#         print('AACPlayer played the songs')
#     def stop(self):
#         print('AACPlayer stops the songs')
# def player(songs):
#     songs.load()
#     songs.play()
#     songs.stop()
# m=MP3Player()
# w=WAVPlayer()
# a=AACPlayer()
# print('MP3Player:')
# player(m)
# print('\nWAVPlayer:')
# player(w)
# print('\nAACPlayer:')
# player(a)
'''20. Design: 
    • Abstract base class Sensor with functions read_value() and calibrate() 
    • Subclasses: 
        TemperatureSensor, PressureSensor, HumiditySensor Encapsulate: 
    • internal raw sensor readings 
    • calibration factor Hide all raw operations and allow only a public, clean get_reading() method.'''
from abc import ABC,abstractmethod
class Sensor(ABC):
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
class TemperatureSensor(Sensor):
    def