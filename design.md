classDiagram
    class Channel {
        - List~Subscriber~ subscribers
        + subscribe(Subscriber)
        + unsubscribe(Subscriber)
        + notifySubscribers()
        + upload(String title)
    }

    class Subscriber {
        - String name
        - Channel channel
        + Subscriber(String name)
        + update()
        + subscribeChannel(Channel ch)
    }

    Channel --> Subscriber : "1..*"