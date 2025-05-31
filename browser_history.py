#browser history: visited sites, back and forward navigation
class browHistory:
    def __init__(self):
        self.history = []
        self.forward_stack = []

    def visit(self, url):
        self.history.append(url)
        self.forward_stack.clear()
        print(f"Visited: {url}")

    def back(self):
        if len(self.history) > 1:
            last_pg = self.history.pop()
            self.forward_stack.append(last_pg)
            print(f"Back to: {self.history[-1]}")
        else:
            print("No more history")

    def forward(self):
        if self.forward_stack:
            next_pg = self.forward_stack.pop()
            self.history.append(next_pg)
            print(f"Forward to: {next_pg}")
        else:
            print("No forward pages")

brow = browHistory()
brow.visit("google.com")
brow.visit("githiub.com")
brow.back()
brow.forward()
brow.visit("gmail.com")
brow.back()
brow.forward()