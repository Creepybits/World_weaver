from .libs.prompt_utils import FixedPromptNode


class WW_MasterKey(FixedPromptNode):
    PROMPT_FILE = "prompt.txt"


NODE_CLASS_MAPPINGS = {
      "WW_MasterKey": WW_MasterKey,
}

NODE_DISPLAY_NAME_MAPPINGS = {
      "WW_MasterKey": "Master Key (World Weaver)",
}
