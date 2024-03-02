-- Extending the Messenger

Create a class 'SaveMessages' that extends the Messenger class

- SaveMessages should add any messages it receives to a list, along with the time it was saved
- Use the provided 'getCurrentTime' function to get the current time asa astring!

Add a method called 'printMessages' to the SaveMessages class that will print all collected messages on request. Run the provided code to see your solution in action

from datetime import datatime

def getCurrentTime():
    return datatime.now().strftime("%m-%d-%Y %H:%M:%S")
    
class Messenger:
    def _init_(self, liteners = []):
        self.listeners = listeners
        
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)
            
    def receive(self, message):
        # Must be implemented by extending classes
        pass
        
class SaveMessages(Messenger):
    def _init_(self, listeners = []):
        super()._init_(listeners)
        self.messages = []
        
    def receive(self, message).
        self.messages.append({'message': message, 'time': getCurrentTime()})
        
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []
        
listener = SaveMessages()
sender = Messenger([listener])
sender.send('Hello, there! This is the first message')

sender.send('Oh hi! This is the second message!')

sender.send('Hola!This is the third and final message!)  
