# Charter SPECTRUM GUIDE TOOLS

These are tools that have been made to help out with the testing of the SPECTRUM GUIDE!

## Installation:

1. You will need Python 2.7
2. For several of these you will need Selenium:
   * `pip install selenium`
   * **NOTE:** You don't need to do a global install you can use a virtual environment
   * **NOTE:** You will also need Firefox
3. To Install:
    1. Fork this Repo.
    2. Navigate to your users home directory:
       * `$ cd ~/`
    3. Create the following directories:
       * `$ mkdir dev`
       * `$ mkdir dev/charter`
    4. Then navigate to the charter directory:
       * `$ cd dev/charter`
    5. Download from GitHub:
       * `$ git clone YOUR_FORKED_REPO`
    6. Add this Repo as your 'upstream':
       * `$ git remote add upstream git@github.com:knappkeith/tools-charter.git`
4. For best results have your `skyuisp` directory located in `~/dev/charter`.

## What, Where and How:

#### Replace Line:
* Most common to use.
* Will preform a line replacement in a file.
* These scripts use the My_Replacer class in the libs folder.
* To Run, `$ python REPLACE_LINE_SCRIPT.py` or `$ ./REPLACE_LINE_SCRIPT.py`
   * If successful you will see `Replacing in {FILE_NAME}`
* Most scripts can be reverted, `$ python REPLACE_LINE_SCRIPT.py --revert` or `$ ./REPLACE_LINE_SCRIPT.py --revert`
* More help can be found, `$ python REPLACE_LINE_SCRIPT.py --help` or `$ ./REPLACE_LINE_SCRIPT.py --help`

#### Get Stash PRs:
* Will Pull Open PR List from Stash
* This script does require selenium and Firefox.
* Does require some setup:
   1. goto tools directory, 
      - `$ cd ~/dev/charter/tools`
   2. copy private_info_template.json, 
      - `$ cp private_info_template.json private_info.json`
   3. open private_info.json and edit the user name and password for your Stash Account.
   4. save and close.
* This script is set up as an executable so to run, 
   - `$ ./get_stash_prs.py`
* Copy and Paste the output into the Google Spreadsheet

#### Get Blocked Tickets:
* Will Pull JIRA Ticket from the queues of the Dev Testers with a BLOCKED status.
* This script does require selenium and Firefox.
* Does require some setup:
   1. goto tools directory, 
      - `$ cd ~/dev/charter/tools`
   2. copy private_info_template.json, 
      - `$ cp private_info_template.json private_info.json`
   3. open private_info.json and edit/add the user name and password for your JIRA Account.
   4. save and close.
* This script is set up as an executable so to run, 
   - `$ ./blocked_jira_bugs.py`
* Copy and Paste the output into the Google Spreadsheet

#### Get Bugs in Triage Tickets:
* Will Pull JIRA Tickets in the 'Bugs in Triage' Sprint.
* This script does require selenium and Firefox.
* Does require some setup:
   1. goto tools directory, 
      - `$ cd ~/dev/charter/tools`
   2. copy private_info_template.json, 
      - `$ cp private_info_template.json private_info.json`
   3. open private_info.json and edit/add the user name and password for your JIRA Account.
   4. save and close.
* This script is set up as an executable so to run, 
   - `$ ./jira_bugs_in_triage.py`
* Copy and Paste the output into the Google Spreadsheet

#### Cloud TV Log:
* Goto Cloud TV folder, `$ cd cloud_tv'
* Copy the Log from Cloud TV Player to Log.txt.
* To Run, `$ python console_parser.py`
* There will be several selections available:
    1. Display Errors only
    2. Display Events only
    3. Display Log only
    4. Display Warnings only
    5. Display All
    6. Reload the file, This will reload the file in case it has changed
    7. EXIT