# 1472. Design Browser History

class Node:
    def __init__(self, val=0):
        self.data = val  # Store the page URL or data
        self.next = None  # Pointer to the next page
        self.back = None  # Pointer to the previous page

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentPage = Node(homepage)  # Initialize the browser history with the homepage

    def visit(self, url: str) -> None:
        newPage = Node(url)  # Create a new page node with the given URL
        self.currentPage.next = newPage  # Set the next of the current page to the new page
        newPage.back = self.currentPage  # Set the back of the new page to the current page
        self.currentPage = newPage  # Update the current page to the new page
        return self.currentPage.data  # Return the URL of the current page
        
    def back(self, steps: int) -> str:
        # Move back 'steps' times or until the beginning of history is reached
        while steps:
            if self.currentPage.back:  # If there is a previous page
                self.currentPage = self.currentPage.back  # Move to the previous page
            else:
                break  # If no previous page, stop
            steps -= 1
        return self.currentPage.data  # Return the URL of the current page

    def forward(self, steps: int) -> str:
        # Move forward 'steps' times or until the end of history is reached
        while steps:
            if self.currentPage.next:  # If there is a next page
                self.currentPage = self.currentPage.next  # Move to the next page
            else:
                break  # If no next page, stop
            steps -= 1
        return self.currentPage.data  # Return the URL of the current page


# Time Complexity: O(steps)
# Space Complexity: O(n)