"""Tests for the Hi Streamlit app."""

import os
import sys
import importlib


def test_app_imports():
    """Test that streamlit can be imported and app structure is valid."""
    import streamlit
    assert streamlit is not None


def test_page_config():
    """Test set_page_config import."""
    from streamlit import set_page_config
    assert callable(set_page_config)


def test_theme_key_constant():
    """Verify the theme key is correctly defined."""
    # Read the app source and check for the theme key
    with open("app.py", "r") as f:
        content = f.read()
    
    assert 'THEME_KEY' in content
    assert 'theme_hi_app' in content
    assert 'localStorage' in content
    assert 'prefers-color-scheme' in content


def test_dark_theme_css():
    """Verify dark theme CSS is present."""
    with open("app.py", "r") as f:
        content = f.read()
    
    assert '[data-theme="dark"]' in content
    assert '--bg-primary' in content
    assert '--text-primary' in content


def test_light_theme_css():
    """Verify light theme CSS is present."""
    with open("app.py", "r") as f:
        content = f.read()
    
    assert '[data-theme="light"]' in content
    assert '--bg-primary' in content
    assert '--text-primary' in content


def test_both_themes_have_all_variables():
    """Ensure both themes define all CSS variables."""
    with open("app.py", "r") as f:
        content = f.read()
    
    # Extract CSS variable names from dark theme
    dark_start = content.index('[data-theme="dark"]')
    dark_end = content.index('[data-theme="light"]')
    dark_section = content[dark_start:dark_end]
    
    light_start = content.index('[data-theme="light"]')
    # Find end of light section (next closing brace after light start)
    brace_count = 0
    light_end = light_start
    for i, ch in enumerate(content[light_start:], light_start):
        if ch == '{':
            brace_count += 1
        elif ch == '}':
            brace_count -= 1
            if brace_count == 0:
                light_end = i + 1
                break
    
    light_section = content[light_start:light_end]
    
    dark_vars = {line.split(':')[0].strip() for line in dark_section.split('\n') if '--' in line and ':' in line}
    light_vars = {line.split(':')[0].strip() for line in light_section.split('\n') if '--' in line and ':' in line}
    
    assert dark_vars == light_vars, f"CSS variable mismatch: dark has {dark_vars - light_vars}, light has {light_vars - dark_vars}"


def test_theme_toggle_present():
    """Verify theme toggle is in the app."""
    with open("app.py", "r") as f:
        content = f.read()
    
    assert 'theme_toggle' in content


def test_greeting_logic():
    """Verify the app has greeting functionality."""
    with open("app.py", "r") as f:
        content = f.read()
    
    assert 'Hi' in content
    assert 'name' in content.lower()
    assert 'greeting' in content.lower()


def test_requirements():
    """Verify requirements.txt is valid."""
    with open("requirements.txt", "r") as f:
        content = f.read()
    
    assert 'streamlit' in content
