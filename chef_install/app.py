import os
import sys
import platform
import subprocess
import shutil
import tempfile
import logging


logging.basicConfig(format='[%(name)s] %(levelname)s: %(message)s')
logger = logging.getLogger('chef-install')
logger.setLevel(logging.INFO)

USER_HOME = os.path.expanduser('~')
META_DIRNAME = '.chef-install'
META_DIR = os.path.join(USER_HOME, META_DIRNAME)

def run(command, capture=False):
    """
    Run command in shell

    @param command: command to run
    @param capture: flag to capture output
    """
    if not capture:
        dev_null = open(os.devnull, 'w+')
        p = subprocess.Popen(command, shell=True, stdout=dev_null, stderr=dev_null)
    else:
        p = subprocess.Popen(command, shell=True,)
    stdout, stderr = p.communicate()
    return stdout

def which(program):
    """
    Analog of `which` command in Linux.
    Returns full path ti program or None

    @param program: Program name to check
    """

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def _check_dependencies():
    """
    Checks if ruby, gems, chef is installed
    """
    logger.info('Checking program dependencies ...')

    if not which('ruby'):
        logger.warn('Ruby not found')
        logger.info('Running apt-get update ...')
        run('apt-get update')
        logger.info('Installing ruby ...')
        run('apt-get install git-core ruby ruby-dev libopenssl-ruby build-essential wget ssl-cert curl rubygems -y')

    # Check if `gem` is available
    if not which('gem'):
        logger.warn('Gem not found')
        logger.info('Installing rubygems ...')
        run('gem install rubygems-update && update_rubygems')

    # Check if chef is available
    if not which('chef-solo'):
        logger.warn('chef-solo not found')
        logger.info('Installing Chef ...')
        run('gem install chef --no-ri --no-rdoc')

    logger.info('All dependencies is met')

def main():
    """
    Entry point
    """
    system = platform.system()
    dist = platform.linux_distribution()

    # This program designed for Ubuntu and depends on apt-get
    if system != 'Linux' or dist[0] != 'Ubuntu':
        logger.error('This program is designed for Ubuntu')
        sys.exit(1)

    logger.info('OS: %s/%s', dist[0], dist[1])
    _check_dependencies()

    if len(sys.argv[1:]) < 1:
        logger.info("Usage: chef-install cookbook1 [cookbook2, cookbookN]")
        sys.exit(1)

    # Verify if meta dir exists
    if not os.path.exists(META_DIR):
        logger.warn('Meta directory does not exists')
        os.mkdir(META_DIR)
        shutil.copy(os.path.join('templates', 'solo.rb'), META_DIR)

    cookbooks = sys.argv[1:]
    run_template = """{ "run_list": [ %s ]  }"""
    temp = tempfile.NamedTemporaryFile(prefix='chef-install.')
    recipes = map(lambda x: '"recipe[%s]"' % x, cookbooks)
    temp.write(run_template % ', '.join(recipes))
    temp.seek(0)

    solo_config = os.path.join(META_DIR, 'solo.rb')
    logger.info('Installing cookbooks %s ...' % ', '.join(cookbooks))
    command = 'chef-solo -c %s -j %s' % (solo_config, temp.name)
    run(command, capture=True)
