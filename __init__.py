import os
import sys

import folder_paths as comfy_paths


ROOT_PATH = os.path.join(
    comfy_paths.get_folder_paths("custom_nodes")[0], "ComfyUI-3D-Pack-Lite"
)
sys.path.append(ROOT_PATH)

from . import nodes


NODE_CLASS_MAPPINGS = nodes.NODE_CLASS_MAPPINGS

NODE_DISPLAY_NAME_MAPPINGS = nodes.NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
