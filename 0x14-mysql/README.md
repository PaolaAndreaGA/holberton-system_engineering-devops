# How To Install MySQL 5.7 on Ubuntu 20.04

By

[Lorna Chepkoech](https://computingforgeeks.com/author/cheplorna/)


In our guide today, we are looking at how to install MySQL 5.7 on Ubuntu 20.04 (Focal Fossa) Server. MySQL is one of the most commonly used Database Management Systems. It uses the concept of relational databases and has a client/server architecture. It can be installed on various operating systems including Windows, CentOS and Debian among others.

The below steps describe how to install and configure MySQL 5.7 on Ubuntu 20.04. It start with adding APT repository with packages for MySQL then dives to the actual package installations and configurations.

## Step 1: Add MySQL APT repository in Ubuntu

Ubuntu already comes with the default MySQL package repositories. In order to add or install the latest repositories, we are going to install package repositories . Download the repository using the below command:

```
sudo apt update
sudo apt install wget -y
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
```

Once downloaded, install the repository by running the command below:

```
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
```

In the prompt, choose  **Ubuntu Bionic**  and click  **Ok**

[![How to install mysql 5.7 on ubuntu 20.04 03](https://computingforgeeks.com/wp-content/uploads/2020/09/How-to-install-mysql-5.7-on-ubuntu-20.04-03.png?ezimgfmt=ng%3Awebp%2Fngcb23%2Frs%3Adevice%2Frscb23-1 "How To Install MySQL 5.7 on Ubuntu 20.04 1")](https://computingforgeeks.com/wp-content/uploads/2020/09/How-to-install-mysql-5.7-on-ubuntu-20.04-03.png?ezimgfmt=ng%3Awebp%2Fngcb23%2Frs%3Adevice%2Frscb23-1)

The next prompt shows MySQL 8.0 chosen by default. Choose the first option and click  **OK**

![How to install mysql 5.7 on ubuntu 20.04 04](https://computingforgeeks.com/wp-content/uploads/2020/09/How-to-install-mysql-5.7-on-ubuntu-20.04-04-1024x181.png?ezimgfmt=rs:696x123/rscb23/ng:webp/ngcb23 "How To Install MySQL 5.7 on Ubuntu 20.04 2")

In the next prompt, select **MySQL 5.7** server and click  **OK**.

![How to install mysql 5.7 on ubuntu 20.04](https://computingforgeeks.com/wp-content/uploads/2020/09/How-to-install-mysql-5.7-on-ubuntu-20.04-1024x150.png?ezimgfmt=rs:696x102/rscb23/ng:webp/ngcb23 "How To Install MySQL 5.7 on Ubuntu 20.04 3")

The next prompt selects MySQL5.7 by default. Choose the last otpion  _**Ok**_ and click  **OK**

![How to install mysql 5.7 on ubuntu 20.04 01](https://computingforgeeks.com/wp-content/uploads/2020/09/How-to-install-mysql-5.7-on-ubuntu-20.04-01-1024x167.png?ezimgfmt=rs:696x114/rscb23/ng:webp/ngcb23 "How To Install MySQL 5.7 on Ubuntu 20.04 4")

## Step 2: Update MySQL Repository on Ubuntu

Run the below command to update your system packages

```
sudo apt-get update
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29

```
sudo apt-get update
```

Now search for MySQL 5,7 using  **apt-cache**  as shown below:

```
$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
    Candidate: 8.0.26-0ubuntu0.20.04.2
      Version table:
           8.0.26-0ubuntu0.20.04.2 500
	           500 http://mirrors.digitalocean.com/ubuntu focal-updates/main amd64 Packages
		           500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
			        8.0.19-0ubuntu5 500
				        500 http://mirrors.digitalocean.com/ubuntu focal/main amd64 Packages
					     5.7.35-1ubuntu18.04 500
					             500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
						     ```

As you can see  **MySQl 5.7.31-1ubuntu18.04**  is appearing in the list.

## Step 3: Install MySQL 5.7 on Ubuntu 20.04 Linux machine

Having found MySQL 5.7 in our system, we are going to install MySQL 5.7 client, MySQL 5.7 server with the below command:

```
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* mysql-server=5.7*