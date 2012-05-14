Chef-install
============

Chef-install helps you to install Chef cookbooks on your local machine with few steps.

Install
-------
    pip install chef-install


Get some Chef cookbooks
-----------------------
    git clone https://github.com/opscode/cookbooks ~/.chef-install/cookbooks

You can omit this step if you already have them. Just edit ``~/.chef-install/solo.rb`` and set proper path to cookbooks.

Cook!
-----
    chef-install my_cookbook

Note. You should run chef-install as root if any of cookbooks requires it.
