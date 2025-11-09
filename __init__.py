import os
import sys
import subprocess


# Add the path to your custom nodes directory to the Python path
custom_nodes_path = os.path.dirname(os.path.abspath(__file__))
assets_nodes_path = os.path.join(custom_nodes_path, "assets", "nodes")
sys.path.append(assets_nodes_path)

# --- IMPORT ALL YOUR NODES FROM assets/nodes ---
from .assets.nodes.DelayTextNode import NODE_CLASS_MAPPINGS as DelayTextNode_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as DelayTextNode_NODE_DISPLAY_NAMES
from .assets.nodes.GeminiAPI import NODE_CLASS_MAPPINGS as GeminiAPI_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as GeminiAPI_NODE_DISPLAY_NAMES
from .assets.nodes.conditional_lora_selector import NODE_CLASS_MAPPINGS as ConditionalLoRAApplier_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as ConditionalLoRAApplier_NODE_DISPLAY_NAMES
from .assets.nodes.MasterKey import NODE_CLASS_MAPPINGS as MasterKey_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as MasterKey_NODE_DISPLAY_NAMES
from .assets.nodes.SceneDirector import NODE_CLASS_MAPPINGS as SceneDirector_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as SceneDirector_NODE_DISPLAY_NAMES
from .assets.nodes.QwenAspectRatio import NODE_CLASS_MAPPINGS as QwenAspectRatio_NODE_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as QwenAspectRatio_NODE_DISPLAY_NAMES
from .assets.nodes.CharacterVault import NODE_CLASS_MAPPINGS as CharacterVault_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as CharacterVault_NODE_DISPLAY_NAME_MAPPINGS
from .assets.nodes.CharacterSelect import NODE_CLASS_MAPPINGS as CharacterSelect_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as CharacterSelect_NODE_DISPLAY_NAME_MAPPINGS
from .assets.nodes.WorldWeaverPrompt import NODE_CLASS_MAPPINGS as WorldWeaverPrompt_NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS as WorldWeaverPrompt_NODE_DISPLAY_NAME_MAPPINGS



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
    **DelayTextNode_NODE_MAPPINGS,    
    **GeminiAPI_NODE_MAPPINGS,    
    **ConditionalLoRAApplier_NODE_MAPPINGS,    
    **MasterKey_NODE_MAPPINGS,    
    **SceneDirector_NODE_MAPPINGS,    
    **QwenAspectRatio_NODE_MAPPINGS,   
    **CharacterVault_NODE_CLASS_MAPPINGS,
    **CharacterSelect_NODE_CLASS_MAPPINGS,
    **WorldWeaverPrompt_NODE_CLASS_MAPPINGS,

}

NODE_DISPLAY_NAME_MAPPINGS = { 
    **DelayTextNode_NODE_DISPLAY_NAMES,   
    **GeminiAPI_NODE_DISPLAY_NAMES,   
    **ConditionalLoRAApplier_NODE_DISPLAY_NAMES,    
    **MasterKey_NODE_DISPLAY_NAMES,   
    **SceneDirector_NODE_DISPLAY_NAMES,   
    **QwenAspectRatio_NODE_DISPLAY_NAMES,   
    **CharacterVault_NODE_DISPLAY_NAME_MAPPINGS,
    **CharacterSelect_NODE_DISPLAY_NAME_MAPPINGS,
    **WorldWeaverPrompt_NODE_DISPLAY_NAME_MAPPINGS,
}

__version__ = "1.0.0"


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




