"""
Application Configuration Management.

This module handles loading, saving, and providing default values for the
application's configuration. It abstracts the logic for determining storage
paths, making it compatible with both standard DEB installations and confined
Snap packages.
"""
import os
import json

from .colors import (
    PALETTE_COLORS, TEXT_COLORS, FONT_SIZES, 
    DEFAULT_COLOR
)

# --- Configuration Path Setup ---
# Compatibility Note:
# This logic determines where the `config.json` file is stored.
# - In a Snap environment (`SNAP_USER_DATA` is set), it uses the sandboxed
#   per-user directory to comply with strict confinement rules.
# - For a standard DEB install, it uses the conventional XDG Base Directory
#   Specification path (`~/.config/linsticky`).
if "SNAP_USER_DATA" in os.environ:
    CONF_DIR = os.path.join(os.environ["SNAP_USER_DATA"], ".config", "linsticky")
else:
    CONF_DIR = os.path.expanduser("~/.config/linsticky")
CONF_PATH = os.path.join(CONF_DIR, "config.json")


class ConfigManager:
    """
    Manages loading and saving of the application's configuration file.
    """
    @staticmethod
    def get_defaults() -> dict:
        """
        Returns the default configuration dictionary.

        Compatibility Note on `db_path`:
        To ensure the user's database persists across re-installations and is
        easily accessible, the default path is set to `~/Documents/LinSticky/notes.db`.
        - For DEB installs, `os.path.expanduser("~")` works directly.
        - For Snap installs, this requires the `home` plug to be connected. The
          code constructs the path to the real home directory, not the sandboxed one.
          `SNAP_REAL_HOME` is the preferred way to get this path if available.
        """
        # Determine the real home directory.
        if "SNAP_USER_DATA" in os.environ:
            home_dir = os.environ.get("SNAP_REAL_HOME")
            if not home_dir:
                # Fallback for environments where SNAP_REAL_HOME isn't set.
                home_dir = os.path.join("/home", os.environ.get("USER", ""))
        else:
            home_dir = os.path.expanduser("~")

        db_path = os.path.join(home_dir, "Documents", "LinSticky", "notes.db")

        return {
            "backend": "wayland",
            "db_path": db_path,
            "ui_scale": 1.0,
            "language": "en",
            "palette": PALETTE_COLORS,  # colors.py'dan
            "text_colors": TEXT_COLORS,  # colors.py'dan
            "font_sizes": FONT_SIZES,    # colors.py'dan
            "formatting": {
                "bold": True, "italic": True, "underline": True,
                "strikethrough": True, "list": True, "text_color": True,
                "font_size": True
            }
        }

    @classmethod
    def load(cls) -> dict:
        """
        Loads the configuration from `config.json`.

        If the file doesn't exist or is invalid, it creates a new one with
        default settings. It also merges the loaded config with defaults to
        ensure new keys from updates are present.

        Returns:
            A dictionary containing the application configuration.
        """
        defaults = cls.get_defaults()
        if not os.path.exists(CONF_PATH):
            try:
                os.makedirs(CONF_DIR, exist_ok=True)
                cls.save(defaults)
            except OSError as e:
                print(f"ERROR: Could not create config directory or file: {e}")
            return defaults

        try:
            with open(CONF_PATH, "r", encoding="utf-8") as f:
                loaded_config = json.load(f)
            
            # Merge loaded config into defaults to ensure all keys are present.
            config = defaults.copy()
            if isinstance(loaded_config.get('formatting'), dict):
                config['formatting'].update(loaded_config['formatting'])
            config.update(loaded_config)
            
            # Restore formatting if it got corrupted.
            if not isinstance(config.get("formatting"), dict):
                config["formatting"] = defaults["formatting"]

            return config
        except (json.JSONDecodeError, OSError) as e:
            print(f"WARNING: Error loading '{CONF_PATH}'. Resetting to defaults. Error: {e}")
            return defaults

    @staticmethod
    def save(config_dict: dict):
        """
        Saves the given configuration dictionary to `config.json`.

        Args:
            config_dict: The configuration dictionary to save.
        """
        try:
            os.makedirs(CONF_DIR, exist_ok=True)
            with open(CONF_PATH, "w", encoding="utf-8") as f:
                json.dump(config_dict, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"ERROR: Could not save config to '{CONF_PATH}': {e}")
