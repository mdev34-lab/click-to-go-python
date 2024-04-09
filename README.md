# Click To Go - Python Scaffolding

Click To Go is a Python application designed to streamline the process of setting up a new Python project. It provides a user-friendly interface to create a project scaffolding with options for documentation, testing, and licensing.

## Features

- **Project Scaffolding**: Easily create a new Python project structure with essential directories and files.
- **Customizable Options**: Choose to include a tests folder, use `.rst` instead of `.md` for documentation, and automatically add the MIT license template.
- **User Interface**: A simple and intuitive UI to input project details and generate scaffolding with a single click.

## Usage

To use Click To Go, download one of the portable executables available in the Releases page or build yourself from source via the following Nuitka command (windows-only):
```bash
nuitka --enable-plugin=pyside6 --onefile --follow-imports userui.py -o ClickToGo_Python.exe --disable-console
```
You can then use [**Resource Hacker**](https://www.angusj.com/resourcehacker/) to apply version info or icons to the executable.

## License
This project uses a MIT license.
More details in the [LICENSE](LICENSE) file.

## Contributing
Contributions are welcome, but please provide proper attribution in your pull requests or forks. Attribution is required to maintain the credibility of this project and its developers.
