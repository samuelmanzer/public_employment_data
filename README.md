
# SETUP

Run the following commands:

```
virtualenv env
. env/bin/activate
pip install -r requirements.txt
```

Now you can pull Federal employment data from OPM; the script will auto-decompress
the data for you:

```
python scripts/fetch_raw_data.py
```
