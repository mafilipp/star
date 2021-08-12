# Levenshtein Distance
This small script prints all the strings from a csv "," separated file, that have a desidered Levenshtein distance from a target string.

# Install
To run the script you need to install the following python package
```
pip install levenshtein
```
Or just use
```
pip install -r requirements.txt
```

Documentation of [levenshtein package](https://www.coli.uni-saarland.de/courses/LT1/2011/slides/Python-Levenshtein.html)

# Usage
Then you can run the program with
```
python path_to_main.py -c comparison_string -l desired_levenshtein_distance -f path_to_csv_file -i column_index
```

# Example
Download this First [CSV file](https://opendata.swiss/en/dataset/hundenamen-aus-dem-hundebestand-der-stadt-zurich2/resource/3e48403f-1ca2-434f-8766-cf0a73d7c2a1)
```
python path_to_main.py -c Luca -l 1 -f path_to_csv_file -i 0
```