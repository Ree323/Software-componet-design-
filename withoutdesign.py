class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, title):
        print(f"Hey {self.name}, Video Uploaded: {title}") 



class Channel:
    def __init__(self):
        self.subscribers = [
            Subscriber("Rama"),
            Subscriber("Omar"),
            Subscriber("Mohamed"),
            Subscriber("Ahmed"),
            Subscriber("Mariam")
        ]
        self.title = ""

    def upload(self, title):
        self.title = title
        # Directly notifies all subscribers when a new video is uploaded
        for subscriber in self.subscribers:
            subscriber.notify(self.title)




if __name__ == "__main__":
    # Create the channel instance
    program = Channel()
    
    # Upload a new video, directly notifying all subscribers
    program.upload("How to learn Programming?")
