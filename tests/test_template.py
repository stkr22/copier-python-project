def test_bake_project_default(copie):
    """Test basic project generation with default settings."""
    result = copie.copy(extra_answers={"project_name": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # Check basic files are always present
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# helloworld\n"


def test_bake_project_with_containers(copie):
    """Test project generation with containers enabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "use_containers": True
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # Container-related files should be present
    container_files = [
        "Containerfile",
        ".dockerignore",
        ".github/workflows/container-build-push.yml",
        ".github/workflows/container-build-pr.yml"
    ]
    
    for file_path in container_files:
        assert (result.project_dir / file_path).exists(), f"Container file {file_path} should exist when use_containers=True"


def test_bake_project_without_containers(copie):
    """Test project generation with containers disabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "use_containers": False
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # Container-related files should NOT be present
    container_files = [
        "Containerfile",
        ".dockerignore",
        ".github/workflows/container-build-push.yml",
        ".github/workflows/container-build-pr.yml"
    ]
    
    for file_path in container_files:
        assert not (result.project_dir / file_path).exists(), f"Container file {file_path} should not exist when use_containers=False"


def test_bake_project_with_pypi_publishing(copie):
    """Test project generation with PyPI publishing enabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "publish_to_pypi": True
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # PyPI publishing file should be present
    pypi_file = ".github/workflows/release-to-pypi.yml"
    assert (result.project_dir / pypi_file).exists(), f"PyPI workflow {pypi_file} should exist when publish_to_pypi=True"


def test_bake_project_without_pypi_publishing(copie):
    """Test project generation with PyPI publishing disabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "publish_to_pypi": False
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # PyPI publishing file should NOT be present
    pypi_file = ".github/workflows/release-to-pypi.yml"
    assert not (result.project_dir / pypi_file).exists(), f"PyPI workflow {pypi_file} should not exist when publish_to_pypi=False"


def test_bake_project_all_features_enabled(copie):
    """Test project generation with all optional features enabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "use_containers": True,
        "publish_to_pypi": True
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # All optional files should be present
    optional_files = [
        "Containerfile",
        ".dockerignore",
        ".github/workflows/container-build-push.yml",
        ".github/workflows/container-build-pr.yml",
        ".github/workflows/release-to-pypi.yml"
    ]
    
    for file_path in optional_files:
        assert (result.project_dir / file_path).exists(), f"Optional file {file_path} should exist when all features are enabled"


def test_bake_project_all_features_disabled(copie):
    """Test project generation with all optional features disabled."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "use_containers": False,
        "publish_to_pypi": False
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # No optional files should be present
    optional_files = [
        "Containerfile",
        ".dockerignore",
        ".github/workflows/container-build-push.yml",
        ".github/workflows/container-build-pr.yml",
        ".github/workflows/release-to-pypi.yml"
    ]
    
    for file_path in optional_files:
        assert not (result.project_dir / file_path).exists(), f"Optional file {file_path} should not exist when all features are disabled"


def test_bake_project_mixed_features(copie):
    """Test project generation with mixed feature settings."""
    result = copie.copy(extra_answers={
        "project_name": "helloworld",
        "use_containers": True,
        "publish_to_pypi": False
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    
    # Container files should be present
    container_files = [
        "Containerfile",
        ".dockerignore",
        ".github/workflows/container-build-push.yml",
        ".github/workflows/container-build-pr.yml"
    ]
    
    for file_path in container_files:
        assert (result.project_dir / file_path).exists(), f"Container file {file_path} should exist when use_containers=True"
    
    # PyPI file should NOT be present
    pypi_file = ".github/workflows/release-to-pypi.yml"
    assert not (result.project_dir / pypi_file).exists(), f"PyPI workflow {pypi_file} should not exist when publish_to_pypi=False"