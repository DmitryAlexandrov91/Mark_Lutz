def addDict(
        obj_1: dict | list | None, obj_2: dict | list | None
) -> dict | list | None:
    """Возвращает один объединённый словарь."""

    if any(not x for x in (obj_1, obj_2)):
        return obj_1 or obj_2

    if all(isinstance(x, list) for x in (obj_1, obj_2)):
        return list(set(obj_1 + obj_2))

    if all(isinstance(x, dict) for x in (obj_1, obj_2)):
        return {**obj_1, **obj_2}
