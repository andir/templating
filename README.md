# templating

[![Coverage Status](https://coveralls.io/repos/andir/templating/badge.svg?branch=master&service=github)](https://coveralls.io/github/andir/templating?branch=master)
[![Coverage Status](https://travis-ci.org/andir/templating.svg)](https://travis-ci.org/andir/templating)

# Usage
Simply install the `templating` package from pypi and execute the `templating` tool. Unless the config flag is specified (`-c`, `--config`) `templating` searches for a config file named `templating.yaml` in the current directory, if it is not found `~/.templating.yaml` might be used, if it exists.
```
pip install templating
templating -c myconf.yaml
```

## Sample config

```yaml
---
templates:
  'test {{ instance }} - {{ my_var }}.conf': test.jinja2

defaults:
  my_var: foo

instances:
  - foo
  - bar
    my_var: bar

```
