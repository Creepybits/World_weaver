# 🌍 World Weaver: The Consistent Character System

**Status:** V1.0 - Active Development (Initial Private Commit: 2025-11-09)  

### Todo
* Finetune LLM for local use

---

## 🎯 The Problem: Why Consistency is Broken

In generative AI, true character consistency is an illusion built on fragile dependencies. Traditional methods rely on complex, heavy files:
*   ❌ **LoRAs:** Require training, large files, and often fail when changing clothes or environments.
*   ❌ **IP-Adapters / FaceSwap:** Require manual intervention and often cause flickering in video.
*   ❌ **ControlNet:** Good for pose, but fails to maintain the likeness's subtle essence.

## ✨ The Solution: Written DNA

The **World Weaver System** solves this by establishing **Textual Inheritance**. It is a unique methodology that uses a suite of connected workflows and custom prompt logic to force the diffusion model to respect an unshakeable, text-based blueprint—the character's **DNA**.

**Results:** Flawless character consistency maintained across radical changes in lighting, pose, clothing, and environment, without any external files required for the core likeness.

---

## 🏗️ Core Components (The System Architecture)

The World Weaver is an ecosystem of three key parts:

### 1. [The Prompt Helper](./docs/Prompt_Helper.md) (Discovery)
*(JSON included in this repo)*
*   **Function:** Uses the Gemini Vision API to analyze any image and convert it into a perfectly structured, ready-to-use text description (the character's DNA).

### 2. [The Genesis](./docs/Genesis.md) (Tester)
*(JSON and Custom Node included in this repo)*
*   **Function:** A simple workflow that will test your prompt before you decide if you want to save it to your database.

### 3. [The Character Vault](./docs/Character_Vault.md) (Database)
*(JSON and Custom Node included in this repo)*
*   **Function:** A database tool that permanently saves the character's DNA to your ComfyUI file system for instant, one-click retrieval in future projects.

### 4. The World Weaver (The Engine)
*(JSON included in this repo)*
*   **Function:** The main, complex workflow that combines the character DNA with modular inputs for Clothes, Action, and World, enabling seamless creation of new, consistent scenes.

---

## 🚀 Get Started & Learn the Method

This repository contains the foundational components. To fully understand the philosophy and access the complete **World Weaver main workflow**, please visit my channels:

*   **📺 Video Tutorial (The Masterclass):** [World Weaver Masterclass](https://www.youtube.com/watch?v=EzmYPvP-oZU&list=PLabSj7CHUKn3yK8lOmKrzwxv8ZDkpM6TT)
*   **✍️ Deep Dive Article (The Concept):** [Creating Consistent AI Characters Without LoRAs or ReActor](https://zanno.se/creating-consistent-ai-characters-without-loras-or-reactor/)

---

Licence: MIT  

Contact: business@zanno.se
