Chef-install
============

Chef-install helps you to install Chef cookbooks on your local machine with few steps.

Install `chef-install`
----------------------
`pip install chef-install`

Get some Chef cookbooks
-----------------------
You can omit this step if you already have them
`git clone https://github.com/opscode/cookbooks ~/.chef-install/cookbooks`

Cook
----
`chef-install my_cookbook`

Note. You should run chef-install as root if any of cookbooks requires it.
`sudo chef-install nginx`
