# Project Setup

## Setting up a Virtual Environment

To create a virtual environment, use the following command:

```sh
python -m venv venv
```

### Activating the Virtual Environment

#### On Windows
```sh
.\venv\Scripts\activate
```

#### On Linux and macOS
```sh
source venv/bin/activate
```

### Installing Dependencies

Once the virtual environment is activated, install the required dependencies using:

```sh
pip install -r requirements.txt
```

## Kaggle API Setup

### Installation

Ensure you have Python 3 and the package manager pip installed.

Run the following command to access the Kaggle API using the command line:

```sh
pip install kaggle
```

> **Note:** You may need to do `pip install --user kaggle` on Mac/Linux. Installations done through the root user (i.e. `sudo pip install kaggle`) will not work correctly unless you understand what you're doing. User installs are strongly recommended in the case of permissions errors.

If you run into a `kaggle: command not found` error, ensure that your python binaries are on your path. You can see where kaggle is installed by doing `pip uninstall kaggle` and seeing where the binary is (then cancel the uninstall when prompted). For a local user install on Linux, the default location is `~/.local/bin`. On Windows, the default location is `$PYTHON_HOME/Scripts`.

> **IMPORTANT:** We do not offer Python 2 support. Please ensure that you are using Python 3 before reporting any issues.

### API Credentials

To use the Kaggle API, sign up for a Kaggle account at [Kaggle](https://www.kaggle.com). Then go to the 'Account' tab of your user profile (https://www.kaggle.com/`<username>`/account) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location appropriate for your operating system:

- **Linux:** `$XDG_CONFIG_HOME/kaggle/kaggle.json` (defaults to `~/.config/kaggle/kaggle.json`). The path `~/.kaggle/kaggle.json` which was used by older versions of the tool is also still supported.
- **Windows:** `C:\Users\<Windows-username>\.kaggle\kaggle.json` - you can check the exact location, sans drive, with `echo %HOMEPATH%`.
- **Other:** `~/.kaggle/kaggle.json`

You can define a shell environment variable `KAGGLE_CONFIG_DIR` to change this location to `$KAGGLE_CONFIG_DIR/kaggle.json` (on Windows it will be `%KAGGLE_CONFIG_DIR%\kaggle.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command:

```sh
chmod 600 ~/.config/kaggle/kaggle.json
```

You can also choose to export your Kaggle username and token to the environment:

```sh
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
```

In addition, you can export any other configuration value that normally would be in the `kaggle.json` in the format `KAGGLE_` (note uppercase). For example, if the file had the variable "proxy" you would export `KAGGLE_PROXY` and it would be discovered by the client.