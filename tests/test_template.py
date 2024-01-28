def test_bake_project(cookies):
    project_name = "A Cool Package"
    result = cookies.bake(extra_context={"project_name": project_name})

    assert result.exit_code == 0
    assert result.exception is None

    assert (
        result.project_path.name
        == f"{ project_name.lower().replace(' ', '-') }-py"
    )
    assert result.project_path.is_dir()
