# FIFA World Cup 2018 Simulator

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

An entertainment-only Python 3/Tkinter simulator using the **historical 2018 group roster**, not current national-team rankings. Eight groups produce sixteen qualifiers and a 15-match fictional knockout tournament. A seed allows reproducible simulations for tests.

```sh
python3 WorldCup.py
python3 WorldCup.py --text --seed 42
python3 -m unittest discover -s tests -v
```

The original EasyGUI implementation is preserved on the [old branch](https://github.com/hamdyaea/Fifa-World-Cup-Simulator-Python-3-GUI/tree/old). Outcomes are random and do not predict real sporting results.
