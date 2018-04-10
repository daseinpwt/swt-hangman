---
title: Testing Guide
author: Mars Group
---

# Black-box testing
For the purpose of black-box testing, the source code should be invisible.
Therefore we provide a script "install.sh" for generating the binary executable.
By using the installation script, the tester need not to run the program by using
Python interpreter to execute the python scripts.

```bash
cd <root>
bash install.sh
```

Of course, if the tester wants, he/she can still check the source code. To
ensure a strict black-box testing, one can remove `./src` after running 'install.sh'.
