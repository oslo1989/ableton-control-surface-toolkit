from typing import Any


def create_instance(c_instance: Any) -> Any:
    from .control_surface import EnablerDocSurface

    return EnablerDocSurface(c_instance)
