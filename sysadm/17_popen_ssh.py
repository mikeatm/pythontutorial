import subprocess
hostname="remotehost.tld"
cmd="uname -a"

ssh = subprocess.Popen(["ssh", "%s" % hostname, cmd], shell=False,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print ssh.stdout.readlines()
