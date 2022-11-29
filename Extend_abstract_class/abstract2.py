import abstract

class Sport(abstract.Car):
    def do_something(self):
        super().do_something()
        print("But Bike are good for short distance travel.")
        
        