      window.dataLayer = window.dataLayer || \[\]; dataLayer.push({"userId":521277,"visitorType":"student","batch":{"id":124,"fullNameWithC":"AFR-0823 (C#19)","schoolLocation":{"id":1,"name":"ALX Africa"}},"curriculum":{"id":1,"name":"SE Foundations"}}); window.gtm\_user\_custom\_event = function (name, options) { if (typeof name === 'undefined') { return; } window.dataLayer.push({ customEventOptions: typeof options !== 'undefined' ? options : {}, event: name, }); } (function(w,d,s,l,i){w\[l\]=w\[l\]||\[\];w\[l\].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)\[0\], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-N4C8MF2'); Project: 0x0A. Configuration management | ALX Africa Intranet          Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);  

Toggle navigation[

](/)

*   [
    
    My Planning
    
    ](/planning/me)
*   [
    
    Projects
    
    ](/projects/current)
*   [
    
    QA Reviews I can make
    
    ](/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](/concepts)
*   [
    
    Conference rooms
    
    ](/dashboards/video_rooms)
*   [
    
    Servers
    
    ](/servers)
*   [
    
    Sandboxes
    
    ](/user_containers/current)
*   [
    
    Tools
    
    ](/dashboards/my_tools)
*   [
    
    Video on demand
    
    ](/dashboards/videos)

* * *

*   [
    
    Peers
    
    ](/users/peers)
*   [
    
    Captain's Logs
    
    ](/dashboards/my_captain_log)

* * *

*   [
    
    Discord
    
    ](https://discord.com/app)
    
    [
    
    My Profile
    
    ](/users/my_profile)
    

[

](/)

*   [
    
    My Planning
    
    ](/planning/me)
*   [
    
    Projects
    
    ](/projects/current)
*   [
    
    QA Reviews I can make
    
    ](/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](/concepts)
*   [
    
    Conference rooms
    
    ](/dashboards/video_rooms)
*   [
    
    Servers
    
    ](/servers)
*   [
    
    Sandboxes
    
    ](/user_containers/current)
*   [
    
    Tools
    
    ](/dashboards/my_tools)
*   [
    
    Video on demand
    
    ](/dashboards/videos)

* * *

*   [
    
    Peers
    
    ](/users/peers)
*   [
    
    Captain's Logs
    
    ](/dashboards/my_captain_log)

* * *

*   [
    
    Discord
    
    ](https://discord.com/app)
    
    [
    
    My Profile
    
    ](/users/my_profile)
    

Curriculum

SE Foundations Average: 139.83%

*   [
    
    SE Foundations Average: 139.83%
    
    
    
    ](/curriculums/1/observe)

[

You have a captain's log due before 2024-03-24 (in 2 days)! Log it now!

](/captain_logs/5250113/edit)

0x0A. Configuration management
==============================

Background Context
------------------

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240322T163143Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4fc3a238dc266bb4ea9a94949bb7ee9cffbf7ebc8eaf47a7f7861db0c747a814)](https://youtu.be/ogYLFyp68cI)

When I was working for SlideShare, I worked on an auto-remediation tool called [Skynet](/rltoken/0zbIzBqH_ktMmRQvJwZs2A "Skynet") that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent `nil` to the filter method.

There were 2 pieces of bad news:

1.  When MCollective receives `nil` as an argument for its filter method, it takes this to mean ‘all servers’
2.  The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif)

That was me ^\_^‘: [https://twitter.com/devopsreact/status/836971570136375296](/rltoken/jIyF-Oa80s40ssG21cyNAg "https://twitter.com/devopsreact/status/836971570136375296")

Resources
---------

**Read or watch**:

*   [Intro to Configuration Management](/rltoken/GL30hu-aRcKzPOvK8JO-Bg "Intro to Configuration Management")
*   [Puppet resource type: file](/rltoken/WON0M4DNRabf88KAG_pDUA "Puppet resource type: file") (_check “Resource types” for all manifest types in the left menu_)
*   [Puppet’s Declarative Language: Modeling Instead of Scripting](/rltoken/0V2fBdafkfKPMxA1umea3Q "Puppet's Declarative Language: Modeling Instead of Scripting")
*   [Puppet lint](/rltoken/CRUMeEMdcX-UtbWsUM9xLQ "Puppet lint")
*   [Puppet emacs mode](/rltoken/MzHXCntAkPzOqMnI6_rpWQ "Puppet emacs mode")

Requirements
------------

### General

*   All your files will be interpreted on Ubuntu 20.04 LTS
*   All your files should end with a new line
*   A `README.md` file at the root of the folder of the project is mandatory
*   Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
*   Your Puppet manifests must run without error
*   Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
*   Your Puppet manifests files must end with the extension `.pp`

Note on Versioning
------------------

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install `puppet`

    $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
    $ apt-get install -y ruby-augeas
    $ apt-get install -y ruby-shadow
    $ apt-get install -y puppet
    

You do **not** need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](/rltoken/fsIr2xFkJHTkaXwqZFFcbA "Puppet 5 Docs")

### Install `puppet-lint`

    $ gem install puppet-lint
    

Tasks
-----

### 0\. Create a file

mandatory

Using Puppet, create a file in `/tmp`.

Requirements:

*   File path is `/tmp/school`
*   File permission is `0744`
*   File owner is `www-data`
*   File group is `www-data`
*   File contains `I love Puppet`

Example:

    root@6712bef7a528:~# puppet-lint --version
    puppet-lint 2.5.2
    root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
    root@6712bef7a528:~# 
    root@6712bef7a528:~# puppet apply 0-create_a_file.pp
    Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
    Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
    Notice: Finished catalog run in 0.03 seconds
    root@6712bef7a528:~#
    root@6712bef7a528:~# ls -l /tmp/school
    -rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
    root@6712bef7a528:~# cat /tmp/school
    I love Puppetroot@6712bef7a528:~#
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0A-configuration_management`
*   File: `0-create_a_file.pp`

Done?! Check your code

×

#### Correction of "0. Create a file"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 1\. Install a package

mandatory

Using Puppet, install `flask` from `pip3`.

Requirements:

*   Install `flask`
*   Version must be `2.1.0`

Example:

    root@9665f0a47391:/# puppet apply 1-install_a_package.pp
    Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
    Notice: /Stage[main]/Main/Package[Flask]/ensure: created
    Notice: Applied catalog in 0.20 seconds
    root@9665f0a47391:/# flask --version
    Python 3.8.10
    Flask 2.1.0
    Werkzeug 2.1.1
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0A-configuration_management`
*   File: `1-install_a_package.pp`

Done?! Check your code

×

#### Correction of "1. Install a package"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

### 2\. Execute a command

mandatory

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

*   Must use the `exec` Puppet resource
*   Must use `pkill`

Example:

Terminal #0 - starting my process

    root@d391259bf577:/# cat killmenow
    #!/bin/bash
    while [[ true ]]
    do
        sleep 2
    done
    
    root@d391259bf577:/# ./killmenow
    

Terminal #1 - executing my manifest

    root@d391259bf577:/# puppet apply 2-execute_a_command.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
    Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
    Notice: Finished catalog run in 0.10 seconds
    root@d391259bf577:/# 
    

Terminal #0 - process has been terminated

    root@d391259bf577:/# ./killmenow
    Terminated
    root@d391259bf577:/#
    

**Repo:**

*   GitHub repository: `alx-system_engineering-devops`
*   Directory: `0x0A-configuration_management`
*   File: `2-execute_a_command.pp`

Done?! Check your code

×

#### Correction of "2. Execute a command"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

Get a sandbox

×

#### Recommended Sandbox

Copyright © 2024 ALX, All rights reserved.

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`

window.codySettings = { widget\_id: "9993bc72-2258-452b-a4bf-b2fe1ad5e0d7" }; !function(){var t=window,e=document,a=function(){var t=e.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://trinketsofcody.com/cody-widget.js";var a=e.getElementsByTagName("script")\[0\];a.parentNode.insertBefore(t,a)};"complete"===document.readyState?a():t.attachEvent?t.attachEvent("onload",a):t.addEventListener("load",a,!1)}();