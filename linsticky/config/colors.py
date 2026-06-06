"""
Centralized color management for LinSticky.
All colors used throughout the application are defined here.
"""

# === PRIMARY COLORS ===
# Note background colors (palette)
COLOR_NOTE_YELLOW = "#FFF59D"
COLOR_NOTE_PINK = "#F8BBD0"
COLOR_NOTE_GREEN = "#C8E6C9"
COLOR_NOTE_LIGHT_BLUE = "#B3E5FC"

PALETTE_COLORS = [
    COLOR_NOTE_YELLOW,
    COLOR_NOTE_PINK,
    COLOR_NOTE_GREEN,
    COLOR_NOTE_LIGHT_BLUE,
]

# === TEXT COLORS ===
TEXT_COLORS = [
    '#000000', '#424242', '#D32F2F', '#C2185B', '#7B1FA2', '#303F9F',
    '#1976D2', '#0288D1', '#0097A7', '#00796B', '#388E3C', '#689F38',
    '#AFB42B', '#FBC02D', '#FFA000', '#E64A19'
]

COLOR_TEXT_PRIMARY = "#000000"
COLOR_TEXT_SECONDARY = "#424242"

# === UI COLORS ===
COLOR_HEADER_BG = "rgba(0, 0, 0, 0.05)"
COLOR_FORMAT_BAR_BG = "rgba(0, 0, 0, 0.03)"
COLOR_BORDER_LIGHT = "rgba(0, 0, 0, 0.08)"
COLOR_BUTTON_HOVER = "rgba(0, 0, 0, 0.1)"
COLOR_BUTTON_TEXT = "#444"
COLOR_PIN_BORDER = "rgba(0, 0, 0, 0.2)"

# === DEFAULTS ===
DEFAULT_COLOR = COLOR_NOTE_YELLOW
DEFAULT_TEXT_COLOR = COLOR_TEXT_PRIMARY

# === FONT SIZES ===
FONT_SIZES = [8, 10, 12, 14, 16, 18, 20, 24, 32, 48, 72]

def get_palette():
    """Returns the default palette colors."""
    return PALETTE_COLORS

def get_text_colors():
    """Returns available text colors."""
    return TEXT_COLORS

def get_font_sizes():
    """Returns available font sizes."""
    return FONT_SIZES