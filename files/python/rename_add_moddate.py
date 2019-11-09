"""
Rename :: Adds ISO date based on modified date of files.
"""

# %% Imports
import os
import time

# %%
cwd = "/Volumes/Cloud_Nine/Sound/Field Recordings/2019_H1n/19-08-22-Offloaded"

os.chdir(cwd)

# %%
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_name = f_name[4:]
    f_ext = f_ext.lower()

    secs = os.path.getmtime(f)
    year = time.localtime(secs)[0]
    month = time.localtime(secs)[1]
    day = time.localtime(secs)[2]

    new_name = f"{year}-{month}-{str(day).zfill(2)}_{f_name}{f_ext}"
    # print(new_name)

    os.rename(f, new_name)


# %%
