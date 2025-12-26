import uuid

_STORAGE = {}

def save_result(data: dict) -> str:
    result_id = str(uuid.uuid4())
    _STORAGE[result_id] = data
    return result_id

def get_result(result_id: str):
    return _STORAGE.get(result_id)

def update_result(result_id: str, data: dict):
    if result_id in _STORAGE:
        _STORAGE[result_id].update(data)
