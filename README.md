# terraform-tools
Scripts to make terraforming more pleasant


## Tools
- [blame_state](./blame_state.py): Tells you the last user to modify the state. Works off of the user's username on their machine.  
- [fix_state_hash](./fix_state_hash.py) (or as I have it aliased: `unfuck_state`): Fixes a state mismatch (which happens if you manually muck in the state file), see below


```
Error loading state: state data in S3 does not have the expected content.

This may be caused by unusually long delays in S3 processing a previous state
update.  Please wait for a minute or two and try again. If this problem
persists, and neither S3 nor DynamoDB are experiencing an outage, you may need
to manually verify the remote state and update the Digest value stored in the
DynamoDB table to the following value: f2d9a092195e6fbc447755193b4a6cfe
```
