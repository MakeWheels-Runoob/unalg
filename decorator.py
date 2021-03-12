from builtin import *


_indent: dict = {}


class Decorator(object):
    def __init__(self, name: str, file: TextIOWrapper = STD_OUT) -> None:
        self.name: str = name
        self.file: TextIOWrapper = file

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            _indent[self.name] = _indent.get(self.name, -1) + 1
            self.start(func, *args, **kwargs)
            re_val: Any = None
            try:
                re_val: Any = func(*args, **kwargs)
            except Exception as e:
                self.stop(e, func, *args, **kwargs)
            else:
                self.end(re_val, func, *args, **kwargs)
            finally:
                _indent[self.name] -= 1
            return re_val

        return wrapper

    def start(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        pass

    def stop(self, exception: Exception, func: Callable, *args: Any, **kwargs: Any) -> None:
        pass

    def end(self, re_val: Any, func: Callable, *args: Any, **kwargs: Any) -> None:
        pass

    def _print_massage(self, msg: str, end: str = "\n") -> None:
        self.file.write(_indent.get(self.name, 0) * TABS + msg + end)


class Logger(Decorator):
    def __init__(self, level: LoggerLevels = LoggerLevels.INFO, file: TextIOWrapper = STD_OUT) -> None:
        super().__init__("logger", file)
        self.level: LoggerLevels = level

    def start(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        self.__print_logger("start", func, *args, **kwargs)

    def stop(self, exception: Exception, func: Callable, *args: Any, **kwargs: Any) -> None:
        self.__print_logger("stop", func, *args, **kwargs)
        self._print_massage(
            "Wrong type: {types}, Wrong reason: {reason}".format(types=type(exception).__name__, reason=str(exception)))
        raise exception

    def end(self, re_val: Any, func: Callable, *args: Any, **kwargs: Any) -> None:
        self.__print_logger("end", func, *args, **kwargs)
        self._print_massage("Return value: {val}".format(val=re_val))

    def __print_logger(self, action: str, func: Callable, *args: Any, **kwargs: Any) -> None:
        self._print_massage("[{level}] The function {item} is {action}.".format(level=self.level.name,
                                                                                item=func_item(func, *args, **kwargs),
                                                                                action=action))


if __name__ == '__main__':
    @Logger()
    def func(x):
        if x == 2:
            raise TypeError("A error")
        if x:
            print(x)
            func(x - 1)
            print(x)

    func(5)
