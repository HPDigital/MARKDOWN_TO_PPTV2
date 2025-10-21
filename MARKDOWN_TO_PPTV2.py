"""
MARKDOWN_TO_PPTV2
"""

#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pypandoc
#direccion = "C:\Users\HP\Desktop\PORTAFOLIO DE PROYECTOS\Markdown2powerpoint.md"
output = pypandoc.convert_file('Markdown2powerpoint.md', 'pptx', outputfile="salida.pptx")
assert output == ""


# In[ ]:




