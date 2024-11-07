class Subscriber:
    def __init__(self, name):
        self.name = name
        self.channel = None  # Will be set when subscribing to a channel

    def update(self):
        if self.channel:
            print(f"Hey {self.name}, Video Uploaded: {self.channel.title}")

    def subscribe_channel(self, channel):
        self.channel = channel



class Channel:
    def __init__(self):
        self.subscribers = []
        self.title = ""

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def upload(self, title):
        self.title = title
        self.notify_subscribers()




if __name__ == "__main__":
    program = Channel()

    # Create subscriber instances
    s1 = Subscriber("Rama")
    s2 = Subscriber("Omar")
    s3 = Subscriber("Mohamed")
    s4 = Subscriber("Ahmed")
    s5 = Subscriber("Jana")

    # Subscribe subscribers to the channel
    program.subscribe(s1)
    program.subscribe(s2)
    program.subscribe(s3)
    program.subscribe(s4)
    program.subscribe(s5)

    # Unsubscribe a subscriber
    program.unsubscribe(s3)

    # Subscribers link themselves to the channel
    s1.subscribe_channel(program)
    s2.subscribe_channel(program)
    s3.subscribe_channel(program)
    s4.subscribe_channel(program)
    s5.subscribe_channel(program)

    # Upload a new video to notify all subscribers
    program.upload("How to learn Programming?")
