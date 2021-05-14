from flask import Flask

class Decorator_Class:
    def __init__(self):
        self.metric = "metric"

    def decorator_p(self, value):
        print(f"Value received from declaring usage of decorator {value}")
        def decorator_c(func):
            print("First entry")
            def inner(*args, **kwargs):
                print("Second entry and function return")
                return func(*args, **kwargs)
            return inner
        return decorator_c

    def decorator_x(self, func):
        print("One less level decorator trying")
        def inner_x(*args, **kwargs):
            print("Function return")
            return func(*args, **kwargs)
        return inner_x

d = Decorator_Class()

# @d.decorator_p("rrr111")
# def mock(str):
#     print(str)

#mock("jjjj")


if __name__ == '__main__':
    app = Flask(__name__)

    #monitor(app)


    @app.route('/with_passing_value')
    @d.decorator_p("calling api")
    def index():
        return "one more level wrapped"

    @app.route('/without_passing_value')
    @d.decorator_x
    def index():
        return "one less level wrapped"

    # Run the application!
    app.run()