from .libs.prompt_utils import FixedPromptNode


class WW_SceneDirector(FixedPromptNode):
    # Scene_Director.md isn't shipped with World Weaver; use it if you have one, else the bundled .txt.
    PROMPT_FILE = ("Scene_Director.md", "Scene_Director.txt")


NODE_CLASS_MAPPINGS = {
      "WW_SceneDirector": WW_SceneDirector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
      "WW_SceneDirector": "Scene Director (World Weaver)",
}
