# Python Project Template

## Introduction

This template uses [Copier](https://copier.readthedocs.io/) to help you set up a new Python project quickly and easily. Copier allows you to create new projects from this template with enhanced features such as handling existing directories, versioning, and more.

## Usage

### Create a Virtual Environment

It’s a good practice to create a virtual environment for your project. Here’s how you can do it:

```bash
python -m venv .env
# On Windows
.\.env\Scripts\activate
# On macOS/Linux
source .env/bin/activate
```

### Install Copier

First, install [Copier](https://copier.readthedocs.io/en/stable/installation/):

```bash
pip install copier
```

### Generate a New Project

To generate a new project from this template, run:

```bash
copier copy gh:stkr22/cookiecutter-python-project path/to/destination
```

Replace `path/to/destination` with your desired project directory. Copier will prompt you for various options defined in the template.

### Update an Existing Project

If you need to apply updates from the template to an existing project (e.g., you have cloned an existing remote repository), navigate to the root of your project directory and run:

```bash
copier update
```

This will update your project files according to the latest template while preserving your custom changes where possible.

## Important Features and Tips

### Handling Existing Projects

- **Overwrite Prompt**: Copier intelligently handles existing directories and files. If you run `copier copy` in an existing project directory, it will prompt you before overwriting files.
- **Skip Files**: Use the `_copy_without_render` list in `copier.yaml` to specify files or patterns that should not be processed by Copier.

### Template Versioning

- **Version Control**: Copier can manage template versions, making it easy to upgrade projects to newer versions of the template.
- **`_copier_template`**: This field in `copier.yaml` indicates the template source path, helping Copier track which template version your project uses.

### Advanced Features

- **Dynamic Prompts**: You can add dynamic prompts and validations in `copier.yaml` to gather more specific inputs from users.
- **Complex Templating**: Copier supports complex Jinja2 templating, allowing for conditionals, loops, and other logic directly within your template files.

### Additional Commands

- **`copier diff`**: Shows the differences between the current project and the template.
- **`copier update`**: Applies the latest changes from the template to the existing project.

### Troubleshooting

- **Validation Errors**: If Copier encounters issues with template variables or formatting, check `copier.yaml` for typos or incorrect types.
- **Debugging**: Run `copier copy --debug` to get detailed output, which can help diagnose issues during project generation.

### Example Commands

Here are a few example commands for common Copier tasks:

```bash
# Create a new project
copier copy gh:stkr22/cookiecutter-python-project new_project

# Update an existing project
cd existing_project
copier update

# Preview changes before applying
copier diff
```
