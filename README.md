# OSRS Leagues Task Wiki Scraper
 Scrapes the OSRS wiki for Leagues tasks and dumps to a csv - originally used for the Trailblazer Reloaded League.

# Usage
To use the script simply type `python scraper.py`. Available options are:
- `-o` or `--output`: Change the output file name, defaults to `tasks`
- `-l` or `--league`: Change the league to generate the task csv for (options are TBL and RE for Trailblazer Reloaded and Raging Echoes, respectively). Defaults to Raging Echoes
 
Type `-h` or `--help` to see these options in more detail.

Once the csv is generated you can import it into another tool. For the previous League I set up a database in Notion and imported it there, it allowed me to create checkbox columns and separate views for myself and my friends which allowed us to filter our tasks against each other to see what we were missing. Added benefits are being able to filter by region, sort by points, whatever really.

# Required packages:
You need to install the following packages via pip to run the scraper:
- `requests`
- `csv`
- `bs4`

You can install them by running the command `python -m pip install PACKAGE_NAME`. If you'd like you can use Anaconda and set up a separate environment to install these packages in (Anaconda also has a package manager that lets you visually search for the necessary packages).

Once you've done that you can simply run the script and it'll generate a csv file.