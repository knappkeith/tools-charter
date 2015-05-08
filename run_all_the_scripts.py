#! /usr/bin/env python
from blocked_jira_bugs import main_puller as blocked_puller
from get_stash_prs import main_puller as pr_puller
from jira_bugs_in_triage import main_puller as triage_puller

print "Pulling...STASH PRs!"
print ""
pr_puller()
print ""
print "Pulling...Blocked JIRA Bugs!"
print ""
blocked_puller()
print ""
print "Pulling...Bugs in Triage!"
print ""
triage_puller()