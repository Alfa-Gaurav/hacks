import asyncio
import inspect
from typing import Callable, Any


async def async_operation(func: Callable, *args, **kwargs) -> Any:
    if inspect.iscoroutinefunction(func):
        return await func(*args, **kwargs)
    else:
        return await asyncio.to_thread(func, *args, **kwargs)
