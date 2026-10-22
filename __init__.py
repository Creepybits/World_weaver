import importlib
import traceback

# --- ALL NODE MODULES IN assets/nodes ---
# Add new node files here. Each module must define NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS.
NODE_MODULES = [
    "DelayTextNode",
    "GeminiAPI",
    "conditional_lora_selector",
    "MasterKey",
    "SceneDirector",
    "QwenAspectRatio",
    "CharacterVault",
    "CharacterSelect",
    "WorldWeaverPrompt",
]

# --- CONSOLIDATE ALL NODE MAPPINGS ---
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
FAILED_MODULES = {}

for module_name in NODE_MODULES:
    try:
        module = importlib.import_module(f".assets.nodes.{module_name}", __name__)
    except Exception as e:
        # One node with a missing dependency (e.g. google-genai) shouldn't take down the whole pack.
        FAILED_MODULES[module_name] = e
        traceback.print_exc()
        continue
    NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)

__version__ = "1.3.0"


WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

print("-------------------------------------------------------------------")
print("Thank you for using World Weaver! - Nova was here, probably looking for snacks.")
print(f"Loaded {len(NODE_CLASS_MAPPINGS)} nodes.")
for module_name, error in FAILED_MODULES.items():
    print(f"  ! Could not load {module_name}: {error}")
print("-------------------------------------------------------------------")
