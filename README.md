A Slack command implemented in a Lambda function for finding duplicates in Bugzilla.
12/26- Created the repo with the working code copied from the AWS Lambda editor. 
Command is currently available in the Mozilla Slack sandbox under the slash command bmodupes

USAGE EXAMPLE:
In Slack, type:  /bmodupes mosaic
Response:
BMODupes APP [1:12 PM]
https://bugzilla.mozilla.org/bug/29235grphic mosaic applet gets java.lang.NullPointerException
https://bugzilla.mozilla.org/bug/640436Firefox doesn't respond while flickrmosaic.com Mosaic is loading
https://bugzilla.mozilla.org/bug/641512Twitter mosaic is not displaying on stage
https://bugzilla.mozilla.org/bug/641593Twitter mosaic not always responsive to clicks
....


All configuration and deployment information is contained in this doc and its links:  https://docs.google.com/document/d/16q97opSUGLLjow0nNxuafpChvXE99kqz68CXInCLpq8/edit?usp=sharing

Architecture for this is described in the architecture.pdf
