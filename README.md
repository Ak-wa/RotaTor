# RotaTor
![python](https://img.shields.io/pypi/pyversions/Django.svg)
![size](https://img.shields.io/github/size/ak-wa/RotaTor/rotaTor.py.svg)
![lastcommit](https://img.shields.io/github/last-commit/ak-wa/RotaTor.svg)
![follow](https://img.shields.io/github/followers/ak-wa.svg?label=Follow&style=social)
### Python Class for changing the tor identity
![](rotator.gif)

## Usage in terminal:   
Terminal 1 (used for starting tor service):   
```
tor
```   
Terminal 2 (runs the code):
```
python3 example.py
```




## Usage in Code:  
example.py   
```python
from rotaTor import Rotator
rot = Rotator(verbose=False)
for i in range(3):
    rot.rotate()
    print(rot.get_node())
 ```    
 * You can get your external IP address(current exit node) with  
 `get_node()`  
 * If called with `verbose=True`, it will do that automatically




## Easy Setup:   
```sh
git clone https://github.com/Ak-wa/RotaTor.git
cd RotaTor/
apt install tor
pip3 install -r requirements.txt
echo -en 'ControlPort 9051\nCookieAuthentication 1' >> /etc/tor/torrc

after that close the terminal; open a new one
```


## Setup breakdown:
* To make this work, you need to add the following lines to your "torrc" file:  
`ControlPort 9051`  
`CookieAuthentication 1`

* You can find the file here:  
if you compiled tor from source:  
`/usr/local/etc/tor/torrc`  
if you installed a pre-built package:  
`/etc/tor/torrc or /etc/torrc`  
fallback location if above file is not found:  
`$HOME/.torrc`  
on windows in TorBrowser folder:  
`\Tor Browser\Browser\TorBrowser\Data\Tor\torrc`
