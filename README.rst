Chef-install
============

Chef-install helps you to install Chef cookbooks on your local machine with single command.

Currently works on Ubuntu only.

*Note. Behind the scenes chef-install uses ruby and chef-solo*

Install
-------
     pip install -e git+https://exslim@github.com/exslim/chef-install.git#egg=chef_install


Get some Chef cookbooks
-----------------------
    git clone https://github.com/opscode/cookbooks ~/.chef-install/cookbooks

You can omit this step if you already have them. Just edit ``~/.chef-install/solo.rb`` and set proper path to cookbooks.

Example of ``~/.chef-install/solo.rb``

     file_cache_path  "/tmp/chef-solo"

     cookbook_path root + '/cookbooks'

     log_level :info

     log_location STDOUT

     ssl_verify_mode :verify_none

     data_bag_path root + '/data_bags'

Cook!
-----
    chef-install my_cookbook

Note. You should run chef-install as root if any of cookbooks requires it.
