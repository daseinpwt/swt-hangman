# Hangman
This is a console-based implementation of the well-known game "Hangman".

## Installation
- Linux/Mac OS
```bash
cd <root>
bash install.sh
```

The executable "hangman" will be installed in `/usr/local/bin`.

After the installation you can run hangman in your terminal:
```bash
hangman
```

### Options
Run `hangman -h` to check all the options.

## Development
### Setup
1. Install pipenv
2. Install python 3.6
3. Enter the development environment

```bash
cd <root>
pipenv install
pipenv shell
```

4. Leave the development environment

```bash
exit
```

### Direct run

```bash
cd <root>/src
python entry.py
```

### Build binary executable
```bash
cd <root>
bash compile.sh
```

The executable file "hangman" is generated in `<root>/dist`.
