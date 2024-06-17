def test_bake_project(copie):
    result = copie.copy(extra_answers={"project_name": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == "# helloworld\n"
