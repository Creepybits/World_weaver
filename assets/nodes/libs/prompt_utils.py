import os

ASSETS_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROMPTS_DIR = os.path.join(ASSETS_DIR, "prompts")


def prompt_path(filename):
    """filename may be a tuple of candidates; the first one that exists is used."""
    if isinstance(filename, (tuple, list)):
        for candidate in filename:
            if os.path.exists(os.path.join(PROMPTS_DIR, candidate)):
                return os.path.join(PROMPTS_DIR, candidate)
        filename = filename[-1]
    return os.path.join(PROMPTS_DIR, filename)


def prompt_mtime(filename):
    """Used by IS_CHANGED so editing a prompt file re-runs the node without restarting ComfyUI."""
    try:
        return os.path.getmtime(prompt_path(filename))
    except OSError:
        return 0.0


def read_prompt(filename):
    """Returns the prompt file's text, or an ERROR string (passed downstream) if it can't be read."""
    filepath = prompt_path(filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[Creepybits] Error: prompt file not found at {filepath}")
        return "ERROR: Prompt file not found."
    except Exception as e:
        print(f"[Creepybits] Error reading {filepath}: {e}")
        return f"ERROR: Could not read prompt file: {e}"


class FixedPromptNode:
    """Base for nodes that prepend a fixed prompt file to the user's text.
    Subclasses only set PROMPT_FILE."""
    PROMPT_FILE = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_2": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "concat_texts"
    CATEGORY = "Creepybits/World_weaver"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return prompt_mtime(cls.PROMPT_FILE)

    def concat_texts(self, text_2):
        return (read_prompt(self.PROMPT_FILE) + text_2,)

