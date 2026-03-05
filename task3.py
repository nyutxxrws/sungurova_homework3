def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list | str:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.
    Параметры:
    search: str - определяет режим работы функции ("args" или "kwargs")
    status: bool - определяет режим фильтрации для args
    *args: tuple - произвольное количество позиционных аргументов
    **kwargs: dict - произвольное количество именованных аргументов
    Возвращаемое значение:
    list | str - возвращает список, строку или вызывает исключение ValueError
    """
    result: list = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")