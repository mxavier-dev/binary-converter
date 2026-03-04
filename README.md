# Binary Converter

Simple GUI programs to convert between binary and decimal numbers.

Included files
- [Projetos_git/Binario/binary_converter_EN.py](Projetos_git/Binario/binary_converter_EN.py) — English UI and labels.
- [Projetos_git/Binario/binary_converter_PT-BR.py](Projetos_git/Binario/binary_converter_PT-BR.py) — Portuguese UI and labels.

Requirements
- Python 3.8 or newer
- `customtkinter` (install with `pip install customtkinter`)
- A working Tkinter installation (usually bundled with Python on most platforms)

Quick start
1. Open a terminal in the repository root (the folder that contains `Projetos_git`).
2. Run the English version:

```bash
python3 Projetos_git/Binario/binary_converter_EN.py
```

Or run the Portuguese version:

```bash
python3 Projetos_git/Binario/binary_converter_PT-BR.py
```

What it does
- Provides a small GUI with two tabs: "Binary → Decimal" and "Decimal → Binary".
- Input validation prevents invalid characters. The binary entry allows only `0` and `1`, disallows leading `0` (but accepts an empty string so the user can clear the field). The decimal entry accepts digits only.
- Conversions are performed in the GUI and results are shown on-screen.

Notes
- The programs are lightweight single-file scripts intended for learning and personal use.
- If you want to bundle them as executables, tools like `pyinstaller` or `cx_Freeze` work well with GUI scripts.

Contributing
- Improvements, bug reports or pull requests are welcome. Please include a short description and steps to reproduce any issue.

License
- MIT License — include a `LICENSE` file if you want to publish this publicly.

Author
- (Add your name or contact info here)
# binary-converter