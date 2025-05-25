class LoginRequiredMixin:
    def dispatch(self):
        print('Checking login')
        super().dispatch()

class ActivityLoggingMixin:
    def dispatch(self):
        print('Loggin activity')
        super().dispatch()

class DataView:
    def dispatch(self):
        print('Displaying data')

class MyView(LoginRequiredMixin,ActivityLoggingMixin,DataView):
    def dispatch(self):
        print('MyView Dispatch')
        super().dispatch()


view = MyView()
view.dispatch()