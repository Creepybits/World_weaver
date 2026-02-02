import os
import sys
import subprocess


# Add the path to your custom nodes directory to the Python path
custom_nodes_path = os.path.dirname(os.path.abspath(__file__))
assets_nodes_path = os.path.join(custom_nodes_path, "assets", "nodes")
sys.path.append(assets_nodes_path)

# --- IMPORT ALL YOUR NODES FROM assets/nodes ---
from .assets.nodes.DelayTextNode import NODE_CLASS_MAPPINGS as WW_DelayTextNode_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_DelayTextNode_NODE_DISPLAY_NAMES
from .assets.nodes.GeminiAPI import NODE_CLASS_MAPPINGS as WW_GeminiAPI_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_GeminiAPI_NODE_DISPLAY_NAMES
from .assets.nodes.conditional_lora_selector import NODE_CLASS_MAPPINGS as WW_ConditionalLoRAApplier_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_ConditionalLoRAApplier_NODE_DISPLAY_NAMES
from .assets.nodes.MasterKey import NODE_CLASS_MAPPINGS as WW_MasterKey_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_MasterKey_NODE_DISPLAY_NAMES
from .assets.nodes.SceneDirector import NODE_CLASS_MAPPINGS as WW_SceneDirector_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_SceneDirector_NODE_DISPLAY_NAMES
from .assets.nodes.QwenAspectRatio import NODE_CLASS_MAPPINGS as WW_QwenAspectRatio_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_QwenAspectRatio_NODE_DISPLAY_NAMES
from .assets.nodes.CharacterVault import NODE_CLASS_MAPPINGS as WW_CharacterVault_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_CharacterVault_NODE_DISPLAY_NAME_MAPPINGS
from .assets.nodes.CharacterSelect import NODE_CLASS_MAPPINGS as WW_CharacterSelect_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_CharacterSelect_NODE_DISPLAY_NAME_MAPPINGS
from .assets.nodes.WorldWeaverPrompt import NODE_CLASS_MAPPINGS as WW_WorldWeaverPrompt_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WW_WorldWeaverPrompt_NODE_DISPLAY_NAME_MAPPINGS



import comfy.sd
import comfy.utils
import time
import re
import json


try:
    import folder_paths
except ImportError:
    print("Warning: Could not import folder_paths from ComfyUI")
    folder_paths = None

# --- CONSOLIDATE ALL NODE MAPPINGS ---
NODE_CLASS_MAPPINGS = {
    **WW_DelayTextNode_NODE_MAPPINGS,    
    **WW_GeminiAPI_NODE_MAPPINGS,    
    **WW_ConditionalLoRAApplier_NODE_MAPPINGS,    
    **WW_MasterKey_NODE_MAPPINGS,    
    **WW_SceneDirector_NODE_MAPPINGS,    
    **WW_QwenAspectRatio_NODE_MAPPINGS,   
    **WW_CharacterVault_NODE_CLASS_MAPPINGS,
    **WW_CharacterSelect_NODE_CLASS_MAPPINGS,
    **WW_WorldWeaverPrompt_NODE_CLASS_MAPPINGS,

}

NODE_DISPLAY_NAME_MAPPINGS = { 
    **WW_DelayTextNode_NODE_DISPLAY_NAMES,   
    **WW_GeminiAPI_NODE_DISPLAY_NAMES,   
    **WW_ConditionalLoRAApplier_NODE_DISPLAY_NAMES,    
    **WW_MasterKey_NODE_DISPLAY_NAMES,   
    **WW_SceneDirector_NODE_DISPLAY_NAMES,   
    **WW_QwenAspectRatio_NODE_DISPLAY_NAMES,   
    **WW_CharacterVault_NODE_DISPLAY_NAME_MAPPINGS,
    **WW_CharacterSelect_NODE_DISPLAY_NAME_MAPPINGS,
    **WW_WorldWeaverPrompt_NODE_DISPLAY_NAME_MAPPINGS,
}

CREEPY_HEADER_COLOR = "#500b50"  # Purple
CREEPY_BG_COLOR = "#0b500b"      # Green

for node_name, node_class in NODE_CLASS_MAPPINGS.items():
    # Only target nodes that are in your category
    if hasattr(node_class, "CATEGORY") and "Creepybits" in node_class.CATEGORY:
        setattr(node_class, "color", CREEPY_HEADER_COLOR)
        setattr(node_class, "bgcolor", CREEPY_BG_COLOR)

__version__ = "1.2.0"


WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

print("-------------------------------------------------------------------")
print("Thank you for using Creepybits Custom Nodes! - Nova was here, probably looking for snacks.")
print("Loading nodes:")
for node_name in NODE_CLASS_MAPPINGS.keys():
    print(f"  - {node_name}")
if 'WEB_DIRECTORY' in locals():
    print(f"Web directory for custom UI: {WEB_DIRECTORY}")
print("-------------------------------------------------------------------")







