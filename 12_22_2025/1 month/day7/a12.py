class Widget:
    def draw(self):
        print('Drawing base Widget')

class ClickableMixin:
    def draw(self):
        print('Adding click behavior')
        super().draw()

class ResizableMixin:
    def draw(self):
        print('Adding resize behavior')
        super().draw()


class Button(ClickableMixin,ResizableMixin,Widget):
    def draw(self):
        print('Drawing button')
        super().draw()


btn = Button()
btn.draw()