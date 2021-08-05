Soil texture classification
===========================

![PyPI - Downloads](https://img.shields.io/pypi/dm/soiltexture)

How to install:
**`pip install soiltexture`**

Possible classifications:
- USDA
- FAO
- INTERNATIONAL
- ISSS

Usage:
```python
from soiltexture import getTexture, getTextures

getTexture(13, 50, classification='USDA')
# silty loam

getTextures([13, 45], [50, 24], classification='FAO')
# ['fine', 'medium']
```

Requirements:
- matplotlib : to use the `path` module

Source for the .dat file:
https://github.com/gmassei/SoilTexture
