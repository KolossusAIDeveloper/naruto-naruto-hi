"""Tests for the Hi Streamlit app."""

import os


def _repo_root():
    """Get the repository root directory (parent of tests/)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _read_app():
    """Read the app.py file."""
    with open(os.path.join(_repo_root(), "app.py"), "r") as f:
        return f.read()


def _read_req():
    """Read the requirements.txt file."""
    with open(os.path.join(_repo_root(), "requirements.txt"), "r") as f:
        return f.read()


def test_streamlit_imports():
    """Test that streamlit can be imported."""
    import streamlit
    assert streamlit is not None


def test_set_page_config_importable():
    """Test set_page_config is importable."""
    from streamlit import set_page_config
    assert callable(set_page_config)


def test_theme_key_defined():
    """Verify the theme localStorage key is defined."""
    content = _read_app()
    assert 'theme_hi_app' in content


def test_dark_theme_present():
    """Verify dark theme CSS block exists."""
    content = _read_app()
    assert '[data-theme="dark"]' in content


def test_light_theme_present():
    """Verify light theme CSS block exists."""
    content = _read_app()
    assert '[data-theme="light"]' in content


def test_css_variables_present():
    """Verify CSS custom properties are used."""
    content = _read_app()
    assert '--bg-primary' in content
    assert '--text-primary' in content
    assert '--accent' in content


def test_theme_toggle_exists():
    """Verify theme toggle functionality."""
    content = _read_app()
    assert 'theme_toggle' in content


def test_localstorage_persistence():
    """Verify localStorage is used for theme persistence."""
    content = _read_app()
    assert 'localStorage' in content


def test_prefers_color_scheme_fallback():
    """Verify OS preference fallback."""
    content = _read_app()
    assert 'prefers-color-scheme' in content


def test_greeting_card_present():
    """Verify greeting card markup exists."""
    content = _read_app()
    assert 'greeting-card' in content
    assert 'Hi' in content


def test_name_input_present():
    """Verify text input for name."""
    content = _read_app()
    assert 'text_input' in content


def test_requirements_has_streamlit():
    """Verify streamlit is in requirements.txt."""
    content = _read_req()
    assert 'streamlit' in content


def test_dockerfile_exists():
    """Verify Dockerfile is present."""
    dockerfile = os.path.join(_repo_root(), "Dockerfile")
    assert os.path.exists(dockerfile)


def test_dockerfile_has_streamlit():
    """Verify Dockerfile runs streamlit."""
    with open(os.path.join(_repo_root(), "Dockerfile"), "r") as f:
        content = f.read()
    assert 'streamlit' in content
    assert '8501' in content
