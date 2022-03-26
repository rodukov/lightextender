# lightextender
A software for downloading screenshots from the lightshot website

## Let's install it!
```bash
git clone https://github.com/rodukov/lightextender
cd lightextender
```

## Example of use
```python
>>> from lightextender import lightextender
>>> a = [lightextender.bashdownload(lightextender.request(_index=lightextender.generate())) for i in range(0, 100)] # It's going to take some time
>>> print(a) # Output the results to the console
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 2048, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256]
```
