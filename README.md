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
* Right now these are all their own scripts.
* To Run, `$ python REPLACE_LINE_SCRIPT.py`
   * If successful you will see `FOUND IT!! Replacing`
* Most scripts can be reverted, `$ python REPLACE_LINE_SCRIPT.py revert`

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
* You will notice a prompt that will ask for a refresh or not, if you have the resources you can leave this open forever and if you need to repull just type `r` and hit `ENTER`.  It will retreive the list faster than starting the script from scratch.  Otherwise type `q` and hit `ENTER`.

#### Cloud TV Log:
* More description later, need to get to work.
