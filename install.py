#!/usr/bin/env python3

# Install dotfiles for Windows
# $ ./install.py windows
# Install dotfiles for Linux
# $ ./install.py linux

import sys, os, site

if len(sys.argv) == 1:
    print("Usage: ./install.py <Operating System>")
    sys.exit(1)

commands = []    

def windows():
    commands.append("lynx -source rawgit.com/transcode-open/apt-cyg/master/apt-cyg > apt-cyg");
    commands.append("install apt-cyg /bin && rm apt-cyg");
    commands.append("apt-cyg install wget curl tar p7zip git openssh sed wget vim tmux zsh make automake gcc-core gcc-g++ python3");
    commands.append("grep -q -F '/cygdrive/c/Users /home none bind 0 0' /etc/fstab || echo '/cygdrive/c/Users /home none bind 0 0' >> /etc/fstab");
    commands.append("mount -a");
    commands.append("curl -LOC - 'https://cygwin.com/setup-x86_64.exe' && install setup-x86_64.exe /bin && rm setup-x86_64.exe");
    commands.append("find ~/ -maxdepth 1 -name '.bashrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.bash_profile' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.minttyrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.zshrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.tmux.conf' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.vimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.gvimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name 'dotfile' -exec rm -rf '{}' \;")
    commands.append("find ~/ -maxdepth 1 -name '.oh-my-zsh' -exec rm -rf '{}' \;")
    commands.append("git clone --depth=1 https://github.com/j16180339887/dotfile.git ~/dotfile");
    commands.append("git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh");
    commands.append("curl -LOC - 'https://bootstrap.pypa.io/get-pip.py'");
    commands.append("python3 get-pip.py");
    commands.append("rm get-pip.py");
    commands.append("echo y | pip3 install youtube-dl");
    commands.append("echo y | pip3 install you-get");
    pkgLocation = site.getsitepackages()
    for location in pkgLocation:
        commands.append("install -D ~/dotfile/Windows/sitecustomize.py " + location + "/sitecustomize.py")
    commands.append("ln -s ~/dotfile/.bashrc ~/.bashrc")
    commands.append("ln -s ~/dotfile/.bash_profile ~/.bash_profile")
    commands.append("ln -s ~/dotfile/.tmux.conf ~/.tmux.conf")
    commands.append("ln -s ~/dotfile/.zshrc ~/.zshrc")
    commands.append("cp ~/dotfile/.vimrc ~/.vimrc")
    commands.append("cp ~/dotfile/.gvimrc ~/.gvimrc")
    commands.append("ln -s ~/dotfile/Windows/.minttyrc ~/.minttyrc")
    
def linux():
    commands.append("sudo apt-get update")
    commands.append("sudo apt-get install tmux zsh git -y")
    commands.append("find ~/.config/openbox/ -name '*.xml' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.bashrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.bash_profile' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.zshrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.tmux.conf' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.vimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.gvimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name 'dotfile' -exec rm -rf '{}' \;")
    commands.append("find ~/ -maxdepth 1 -name '.oh-my-zsh' -exec rm -rf '{}' \;")
    commands.append("git clone --depth=1 https://github.com/j16180339887/dotfile.git ~/dotfile")
    commands.append("git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh");
    commands.append("ln -s ~/dotfile/.bashrc ~/.bashrc")
    commands.append("ln -s ~/dotfile/.bash_profile ~/.bash_profile")
    commands.append("ln -s ~/dotfile/.tmux.conf ~/.tmux.conf")
    commands.append("ln -s ~/dotfile/.zshrc ~/.zshrc")
    commands.append("ln -s ~/dotfile/.vimrc ~/.vimrc")
    commands.append("ln -s ~/dotfile/Linux/.config_openbox_rc.xml ~/.config/openbox/rc.xml")
    commands.append("openbox --reconfigure")
    
def bsd():
    commands.append("sudo pkg update")
    commands.append("sudo pkg install tmux zsh git -y")
    commands.append("find ~/ -maxdepth 1 -name '.bashrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.bash_profile' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.zshrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.tmux.conf' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.vimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name '.gvimrc' -delete")
    commands.append("find ~/ -maxdepth 1 -name 'dotfile' -exec rm -rf '{}' \;")
    commands.append("find ~/ -maxdepth 1 -name '.oh-my-zsh' -exec rm -rf '{}' \;")
    commands.append("git clone --depth=1 https://github.com/j16180339887/dotfile.git ~/dotfile")
    commands.append("git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh");
    commands.append("ln -s ~/dotfile/.bashrc ~/.bashrc")
    commands.append("ln -s ~/dotfile/.bash_profile ~/.bash_profile")
    commands.append("ln -s ~/dotfile/.tmux.conf ~/.tmux.conf")
    commands.append("ln -s ~/dotfile/.zshrc ~/.zshrc")
    commands.append("ln -s ~/dotfile/.vimrc ~/.vimrc")
    
def install():
    for cmd in commands:
        if os.system(cmd) != 0:
            print("Error: " + cmd)
            sys.exit(1)

target = sys.argv[1].lower()

if   target == "windows":
    windows()
    install()
elif target == "linux":
    linux()
    install()
elif target == "bsd":
    bsd()
    install()
else:
    print("System not support")
    sys.exit(1)

sys.exit(0)
