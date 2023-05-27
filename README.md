# Auto-Dorker

Auto-Dorker is a tool that automates the process of generating and checking dorks for GitHub and Google search engines. It allows you to search for specific content within websites and retrieve potential vulnerabilities or sensitive information.

## Features

- Supports GitHub and Google search engines.
- Customizable dork selection.
- Progress bar for tracking the checking process.
- Saves the results to `result.txt` file.

## Requirements

- Python 3.6 or higher
- `requests` library
- `tqdm` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/5h4kun1/Auto-Dorker.git
   ```

2. Change into the `Auto-Dorker` directory:
   ```
   cd Auto-Dorker
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you are in the `Auto-Dorker` directory.

2. Run the `dork.py` script:
   ```
   python dork.py
   ```

3. Follow the instructions on the command line:
   - Enter the website you want to search.
   - Choose the dork selection:
     - `1` for GitHub dorks.
     - `2` for Google dorks.
     - `3` for both GitHub and Google dorks.
   - The script will start generating and checking the dorks, displaying a progress bar.

4. Once the process is completed, the results will be saved in the `result.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This tool is inspired by the concept of dorking and automated reconnaissance.
and the dorking files are taken from https://github.com/VxbeSec/Github-and-Google-Dorking-Automated.git huge thanks!!
