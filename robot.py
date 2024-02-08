#!/usr/bin/python3

import urllib.request


class Robot:
    def __init__(self, url):
        # Initialize the Robot object with the given URL and set data_text to
        # None
        self.url = url
        self.__data_text = None

    def retrieve(self):
        # Retrieve the content of the URL if it hasn't been downloaded yet
        if self.__data_text is None:
            try:
                # Open the URL and read its content
                endpoint = urllib.request.urlopen(self.url)
                self.__data_text = endpoint.read().decode("utf-8")
                print(f"Downloading the URL ({self.url})")
            except urllib.error.HTTPError as e:
                # Handle HTTP errors
                print(f"Error during the download of {self.url}")
            except urllib.error.URLError as e:
                # Handle URL errors
                print(f"Error: the URL ({self.url}) is not correct")
        else:
            # If the data_text is not None, the URL has already been downloaded
            print(f"The URL {self.url} has already been downloaded")

    def show(self):
        # Display the content of the URL
        self.retrieve()
        print(self.__data_text)

    def content(self):
        # Return the content of the URL
        self.retrieve()
        return self.__data_text


if __name__ == "__main__":
    robot_1 = Robot("https://www.urjc.es/")
    robot_1.retrieve()
    robot_1.show()
    robot_1.content()
    robot_2 = Robot("https://bobbyhadz.com/blog/python-count-in-for-loop")
    robot_2.retrieve()
    robot_2.show()
    robot_2.content()
