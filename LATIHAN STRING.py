#!/usr/bin/env python
# coding: utf-8

# In[19]:


nama = "Muhammad Abidin"

# inisialisasi variabel hitung
jumlah_huruf = 0
jumlah_vokal = 0
jumlah_konsonan = 0

# menghitung jumlah huruf, vokal, dan konsonan
for huruf in nama:
    if huruf != " ":
        jumlah_huruf += 1
        if huruf in "aiueoAIUEO":
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# mencetak hasil
print("Jumlah huruf pada nama", nama, "adalah:", jumlah_huruf)
print("Jumlah huruf vokal pada nama", nama, "adalah:", jumlah_vokal)
print("Jumlah huruf konsonan pada nama", nama, "adalah:", jumlah_konsonan)


# In[ ]:




