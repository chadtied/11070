sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt install git
sudo apt install gcc
sudo apt install make
exit
git clone https://github.com/weippig/112_1_OS_PG1.git src
ls
la
top
ls
cd src/
ls
vim simple.c 
make
ls
sudo insmod simple.ko
dmesg
sudo rmmod simple
dmesg
make clean
ls
cat hello
cat hello.c 
vim hello.c 
ls
vim Makefile 
make
sudo insmod hello.ko
ls
cd ..
ls
cd src
cat /proc/hello
la
sudo rmmod hello
make clean
ls
vim seconds.c 
gcc seconds.c 
vim seconds.c 
vim Makefile 
make
vim seconds.c 
make clean
make
vim seconds.c 
make clean
make
sudo insmod seconds.ko
cat /proc/seconds
make clean
sudo rrmode seconds
sudo rmmode seconds
sudo rmmod seconds
vim seconds.c 
cat seconds.c 
vim seconds.c 
make
vim seconds.c 
make clean
make
vim seconds.c 
make clean
make
sudo insmod seconds.ko
cat /proc/seconds
vim seconds.c 
sudo rmod seconds.ko
sudo remod seconds.ko
sudo rmmod seconds.ko
make clean
make
sudo insmod seconds.ko
cat /proc/seconds
sudo remod seconds.ko
sudo rmmod seconds.ko
make clean
exit
ls
cd src
l
vim third_example.c 
vim 
vim Makefile 
make
sudo insmod third_example.ko mystring="bebop" myintarray=-1
sudo dmesg -t|tail -7
sudo rmmod third_example 
sudo insmod third_example.ko mystring="bebop" myintarray=1,2 myshort=5 mylong=8888 myint=55
sudo dmesg -t|tail -7

make clean
sudo dmesg -t|tail -5
vim third_example.c 
touch third.c
ls
cp third_example.c third.c
ls
vim third.c
vim Makefile 
mkae
make
vim third.c
make clean
make
vim third.c
make
make clean
make
vim third.c
make clean
make
vim third.c
make
make clean
vim third.c
make clean
make
vim third.c
make clean
make
sudo insmod third.ko myname="helen" myage=20 mybirthday=3,19
sudo rmmod third
sudo dmesg -t | tail -5
vim Makefile 
ls
make clean
ls
vim simple.c 
vim Makefile 
make
sudo insmod simple.ko
sudo lsmod | grep simple
sudo rmmod simple
dmesg
sudo rmmod simple
sudo rmmod third_example
sudo rmmod third
sudo rmmod seconds
sudo rmmod hello
exit
