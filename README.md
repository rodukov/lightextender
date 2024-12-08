<div align=center>
  
  <img src="https://github.com/user-attachments/assets/475e0f97-950a-4c87-9796-7fe8bd63bb53" width=180px>
  
</div>

# lightextender
A software for downloading screenshots from the lightshot website
<img align="center" alt="Preview" src="preview.png"/>
## Let's install it!
```bash
git clone https://github.com/rodukov/lightextender
cd lightextender
pip3 install -r requirements.txt
```

## Example of use
```python
>>> from lightextender import lightextender
>>> a = [lightextender.bashdownload(lightextender.request(_index=lightextender.generate())) for i in range(0, 100)] # It's going to take some time
>>> print(a) # Output the results to the console
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2048, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 2048, 0, 0, 0, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 256]
```
