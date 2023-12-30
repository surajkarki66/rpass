# rpass

simple command line app for generating strong random passwords. It also shows all the passwords you generated.

## Installation

### Using Pip

```bash
  pip install rpass
```

### Manual

```bash
  git clone https://github.com/surajkarki66/rpass
  cd rpass
  python setup.py install
```

## Usage

```bash
  rpass [Options]
```

**Options**

-h, --help<br>
Display help

-v<br>
Display version

-l, --length LENGTH<br>
Passwords should contain LENGTH characters. Defaults to 12.

-ns, --no-symbols<br>
Don't use symbols

-nd, --no-digits<br>
Don't use digits

--upper<br>
Use only upper-case letters

--lower<br>
Use only lowercase letters

---

## Help

```bash
  rpass --help
```

## Examples

Below are some examples of rpass usage.

- Generate password:

```bash
  rpass
```

Your password is 9CI=OydGufZm<br>
Saved! to clipboard

- Generate a password with eight characters:

```bash
  rpass -l 8
```

Your password is TgRt6ZU?<br>
Saved! to clipboard

- Generate password with all upper case letters:

```bash
  rpass --upper
```

Your password is 8#ZS"=]FG#qW<br>
Saved! to clipboard

- Generate a password without symbols and save:

```bash
  rpass -ns -s
```

Your password is D3PDbbePwcYE<br>
Saved! to clipboard<br>
Saved! to file<br>
