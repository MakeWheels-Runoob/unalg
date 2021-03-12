# unalg
Some algorithms

> builtin.py:
>
> Variable: 
> > `TABS: str = "  "`
> > 
> > `STD_OUT: _io.TextIOWrapper = sys.stdout`
> > 
> > `STD_ERR: _io.TextIOWrapper = sys.stdout`
> > 
> > `STD_IN: _io.TextIOWrapper = sys.stdin`
>
> Function:
> > `func_item(func: Callable, *args: Any, **kwargs: Any) -> str`: return the function items like`p(1, 2, 3, a=3, b=4)`
> 
> Class:
> > `LoggerLevels(Enum)`: the logger levels
> > > `OTHER = 0`
> > > 
> > > `INFO = 1`
> > > 
> > > `DEBUG = 2`
> > > 
> > > `WARNING = 4`
> > > 
> > > `ERROR = 8`
> > > 
> > > `COLLAPSE = 16`
