# pyautowire ![PyPI](https://img.shields.io/pypi/v/pyautowire) ![Linting and Tests](https://github.com/twaslowski/py-autowire/actions/workflows/test.yml/badge.svg)

Lightweight dependency injection for Python that autowires into _anything_.

## The Quick Pitch

Do you love `pytest` fixtures? Do you wish you could have the flexibility of fixtures without actually having to worry
about the complications of using Dependency Injection? Then `pyautowire` is for you!

## The Longer Version

Dependency Inversion is a common design pattern across a variety of languages. It most often occurs in object-oriented
programming languages, where you can choose from a variety of flavours, such as constructor injection, setter injection,
or interface injection [[1]](https://martinfowler.com/articles/injection.html#FormsOfDependencyInjection).

The most popular dependency injection library in Python is the aptly named `Dependency Injector`
[[2]](https://github.com/ets-labs/python-dependency-injector), which comes with a massive variety of configuration
options.

I personally primarily use Python for medium-sized pet projects, and I found those configuration options to be a bit
too complex for my usecase. Specifically, there are cases where I don't necessarily want to turn everything into a
class to inject dependencies into; sometimes I just want a lightweight function that I can inject values into.
Enter `pyautowire`, for all of your _good enough™️_ dependency injection needs.

## Installation

You can install `pyautowire` via pip:

```bash
pip install pyautowire
```

or via Poetry:

```bash
poetry add pyautowire
```

It is compatible with Python3.7 and above.

## Usage

To use `pyautowire`, you need to have your injectable classes inherit from the `Injectable` class and use the
`@autowire` decorator on the methods you want to inject values into. For example:

```python
from pyautowire import Injectable, autowire

class Configuration(Injectable):
    def __init__(self, config_value: str):
        self.config_value = config_value

@autowire('configuration')
def my_function(configuration: Configuration):
    print(configuration.config_value)

if __name__ == '__main__':
    configuration = Configuration('Hello, World!').register()
    my_function()
```

You can see that you can call `my_function` without passing in any arguments; `pyautowire` will automatically inject them.

Admittedly, this is a rather silly example, since you could have just passed the configuration value as an argument to `my_function`.
However, imagine you can use the `configuration` object across your entire application without ever using an `import`,
having to store a global configuration object somewhere, or pass it around as an argument.

Note that you **have** to call `register()` on your `Injectable` objects before you can use them.
You also **have** to specify all the arguments you would like to inject into your function in the `@autowire` decorator.
Given enough time, I might come up with a smarter solution to automatically handle that, but for now, this works fine.

## Constructor Injection

`pyautowire` _technically_ supports constructor injection. I'll be honest: This is a hack at the moment. But if you
really want to do it, it works:

```python
class MyDatabase(Injectable):
    @autowire('configuration')
    def __init__(self, configuration: Configuration):
        self.db_url = configuration.db_url
        self.db_user = configuration.db_user
        self.db_password = configuration.db_password
```

# Should I use this?

As a rule of thumb: For small projects where you want to avoid the complexity of a full-blown dependency injection library,
while getting all of its benefits: sure. It is genuinely fun to work with, and it'll accelerate your workflow in rapid prototyping.

For larger projects, I would recommend using a more established library like `Dependency Injector`. The amount of complexity
this library can handle is very limited.
