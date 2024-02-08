#!/usr/bin/python3

from robot import Robot  # Import the Robot class


class Cache:
    def __init__(self):
        # Initialize the Cache object with an empty dictionary to store
        # downloaded URLs and their content
        self.cache = {}

    def retrieve(self, url):
        # Retrieve the content of the URL using a Robot object if it hasn't
        # been downloaded yet
        if url not in self.cache:
            # Create a Robot object to download the content
            robot = Robot(url=url)
            # Retrieve the content using the Robot object and store it in the
            # dictionary
            self.cache[url] = robot.content()

    def show(self, url):
        # Display the content of the specified URL
        if url not in self.cache:
            # If the URL is not in the dictionary, retrieve its content
            self.retrieve(url)
        # Print the URL and its content
        print(url)
        print(self.cache[url])

    def show_all(self):
        # Display all downloaded URLs
        print("All these URLs have been downloaded:")
        for number, url in enumerate(self.cache):
            print(f"{number}. {url}")

    def content(self, url):
        # Return the content of the specified URL
        if url not in self.cache:
            # If the URL is not in the dictionary, retrieve its content
            self.retrieve(url)
        # Return the content of the URL
        return self.cache[url]


if __name__ == "__main__":
    cache_1 = Cache()
    cache_1.retrieve("https://www.urjc.es/")
    cache_1.show("https://www.urjc.es/")
    cache_1.show_all()
    cache_1.content("https://bobbyhadz.com/blog/python-count-in-for-loop")
    cache_1.show_all()
    
    cache_2 = Cache()
    cache_2.show("https://docs.python.org/3/library/urllib.request.html#examples")
    cache_2.retrieve("https://docs.python.org/3/library/urllib.request.html#examples")
    cache_2.show_all()
    cache_2.content("https://docs.python.org/3/library/urllib.request.html#httpredirecthandler-objects")
    cache_2.show_all()
    
