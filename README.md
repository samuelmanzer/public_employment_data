
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

Now we're going to load the data into MySQL; if you don't have MySQL already, you can get it from Homebrew and start the server running in the background:

```
brew install mysql 
mysql.server start
```

Let's load the employment data into MySQL:

```
mysql -u root < etl/create_public_employment_data_db.sql
```

When we're finished, we can delete all traces of this data:

```
mysql -u root < etl/clear_public_employment_data_db.sql
```
