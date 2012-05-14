root = File.expand_path(File.dirname(__FILE__))

file_cache_path  "/tmp/chef-solo"
cookbook_path root + '/cookbooks'
log_level :info
log_location STDOUT
ssl_verify_mode :verify_none
data_bag_path root + '/data_bags'