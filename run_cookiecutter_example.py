#!/usr/bin/env python3
import pexpect

p = pexpect.spawn('cookiecutter .')

p.expect('full_name .*')
p.sendline('Brookhaven National Lab')

p.expect('email .*')
p.sendline('dallan@bnl.gov')

p.expect('github_username .*')
p.sendline('danielballan')

p.expect('project_name .*')
p.sendline('Example')

p.expect('package_dist_name .*')
p.sendline('')

p.expect('package_dir_name .*')
p.sendline('')

p.expect('repo_name .*')
p.sendline('')

p.expect('project_short_description .*')
p.sendline('')

p.expect('Select minimum_supported_python_version.*')
p.sendline('')

# Runs until the cookiecutter is done; then exits.
p.interact()
