#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Unit tests for init-sanctum.py"""

import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch

import sys
import os

# Add scripts directory to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent))
os.chdir(Path(__file__).parent.parent)

# Import init_sanctum from the scripts directory
import importlib.util
spec = importlib.util.spec_from_file_location("init_sanctum", Path(__file__).parent.parent / "init-sanctum.py")
init_sanctum = importlib.util.module_from_spec(spec)
sys.modules["init_sanctum"] = init_sanctum
spec.loader.exec_module(init_sanctum)


def test_parse_frontmatter():
    """Test frontmatter parsing from markdown files."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("---\nname: test-cap\ncode: TC\ndescription: A test capability\n---\n\n# Content\n")
        f.flush()
        result = init_sanctum.parse_frontmatter(Path(f.name))
        assert result["name"] == "test-cap"
        assert result["code"] == "TC"
        assert result["description"] == "A test capability"
        Path(f.name).unlink()


def test_parse_frontmatter_empty():
    """Test frontmatter parsing with no frontmatter."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("# Just a heading\n\nSome content\n")
        f.flush()
        result = init_sanctum.parse_frontmatter(Path(f.name))
        assert result == {}
        Path(f.name).unlink()


def test_substitute_vars():
    """Test variable substitution in template content."""
    content = "Hello {user_name}, your language is {communication_language}."
    variables = {"user_name": "Abdul", "communication_language": "Indonesia"}
    result = init_sanctum.substitute_vars(content, variables)
    assert result == "Hello Abdul, your language is Indonesia."


def test_discover_capabilities():
    """Test capability discovery from reference files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        refs_dir = Path(tmpdir)
        # Create a capability file
        cap_file = refs_dir / "test-cap.md"
        cap_file.write_text("---\nname: PDLC Orchestration\ncode: PO\ndescription: Coordinate course creation\n---\n\n# Content\n")
        # Create a non-capability file (no frontmatter code)
        non_cap = refs_dir / "guide.md"
        non_cap.write_text("# Just a guide\n\nNo frontmatter code here.\n")

        capabilities = init_sanctum.discover_capabilities(refs_dir, "./references")
        assert len(capabilities) == 1
        assert capabilities[0]["name"] == "PDLC Orchestration"
        assert capabilities[0]["code"] == "PO"


def test_generate_capabilities_md():
    """Test CAPABILITIES.md generation."""
    capabilities = [
        {"name": "PDLC Orchestration", "description": "Coordinate course creation", "code": "PO", "source": "./references/pdlc-orchestration.md"},
        {"name": "Context Consolidation", "description": "Merge sub-agent outputs", "code": "CC", "source": "./references/context-consolidation.md"},
    ]

    result = init_sanctum.generate_capabilities_md(capabilities, evolvable=True)
    assert "| [PO] | PDLC Orchestration | Coordinate course creation |" in result
    assert "| [CC] | Context Consolidation | Merge sub-agent outputs |" in result
    assert "## Learned" in result
    assert "## How to Add a Capability" in result


def test_generate_capabilities_md_not_evolvable():
    """Test CAPABILITIES.md generation without evolvable."""
    capabilities = [
        {"name": "Test", "description": "A test", "code": "TT", "source": "./references/test.md"},
    ]
    result = init_sanctum.generate_capabilities_md(capabilities, evolvable=False)
    assert "## Learned" not in result


def test_initiate_project_memory():
    """Test shared project memory creation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_memory = Path(tmpdir)
        init_sanctum.initiate_project_memory(project_memory)

        # Check directories exist
        assert (project_memory / "daily").is_dir()
        assert (project_memory / "curated").is_dir()
        assert (project_memory / "curated" / "content-drafts").is_dir()

        # Check index.md was created
        assert (project_memory / "index.md").exists()
        index_content = (project_memory / "index.md").read_text()
        assert "No active course" in index_content

        # Check curated files were created
        assert (project_memory / "curated" / "discovery-log.md").exists()
        assert (project_memory / "curated" / "knowledge-base.md").exists()


def test_initiate_project_memory_idempotent():
    """Test that project memory initialization is idempotent."""
    with tempfile.TemporaryDirectory() as tmpdir:
        project_memory = Path(tmpdir)

        # First run
        init_sanctum.initiate_project_memory(project_memory)
        first_index = (project_memory / "index.md").read_text()

        # Second run should not overwrite
        init_sanctum.initiate_project_memory(project_memory)
        second_index = (project_memory / "index.md").read_text()

        assert first_index == second_index


def test_parse_yaml_config():
    """Test YAML config parsing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write("user_name: Abdul\ncommunication_language: Indonesia\n")
        f.flush()
        result = init_sanctum.parse_yaml_config(Path(f.name))
        assert result["user_name"] == "Abdul"
        assert result["communication_language"] == "Indonesia"
        Path(f.name).unlink()


def test_parse_yaml_config_missing():
    """Test YAML config parsing with missing file returns empty dict."""
    result = init_sanctum.parse_yaml_config(Path("/nonexistent/config.yaml"))
    assert result == {}


if __name__ == "__main__":
    test_parse_frontmatter()
    test_parse_frontmatter_empty()
    test_substitute_vars()
    test_discover_capabilities()
    test_generate_capabilities_md()
    test_generate_capabilities_md_not_evolvable()
    test_initiate_project_memory()
    test_initiate_project_memory_idempotent()
    test_parse_yaml_config()
    test_parse_yaml_config_missing()
    print("All tests passed!")