# RAE-553-2-summer-2019
#Practical laboratory work in class for FTP
#First of all because I didn't had Linux I downloaded miniconda, debian and others

(base) C:\Users\User>conda create -n 191AEM006_FTP.env           #to create an environment for me
Collecting package metadata (current_repodata.json): done
Solving environment: done    
## Package Plan ##

  environment location: F:\Miniconda\envs\191AEM006_FTP.env
  Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate 191AEM006_FTP.env
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\User>conda activate 191AEM006_FTP.env

(191AEM006_FTP.env) C:\Users\User>conda list
(191AEM006_FTP.env) C:\Users\User>conda list
# packages in environment at F:\Miniconda\envs\191AEM006_FTP.env:
#
# Name                    Version                   Build  Channel
(191AEM006_FTP.env) C:\Users\User>conda install python
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: F:\Miniconda\envs\191AEM006_FTP.env

  added / updated specs:
    - python


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    python-3.7.4               |       h5263a28_0        18.2 MB
    ------------------------------------------------------------
                                           Total:        18.2 MB

The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2019.5.15-1
  certifi            pkgs/main/win-64::certifi-2019.6.16-py37_1
  openssl            pkgs/main/win-64::openssl-1.1.1c-he774522_1
  pip                pkgs/main/win-64::pip-19.2.2-py37_0
  python             pkgs/main/win-64::python-3.7.4-h5263a28_0
  setuptools         pkgs/main/win-64::setuptools-41.0.1-py37_0
  sqlite             pkgs/main/win-64::sqlite-3.29.0-he774522_0
  vc                 pkgs/main/win-64::vc-14.1-h0510ff6_4
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.16.27012-hf0eaf9b_0
  wheel              pkgs/main/win-64::wheel-0.33.4-py37_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py37_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
python-3.7.4         | 18.2 MB   | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
>>> from ftplib import FTP
>>> ftp = FTP('ftp.lt.debian.org')
>>> ftp.login();
'230 Login successful.'
>>> data = ftp.retrlines('LIST')
drwxr-xr-x  198 ftp      ftp          8192 Sep 09 12:30 apache
drwxr-xr-x    9 ftp      ftp          4096 Sep 10 09:15 debian
drwxr-xr-x    5 ftp      ftp           102 Sep 10 09:12 debian-backports
drwxr-xr-x    5 ftp      ftp           127 Sep 08 16:43 debian-cd
drwxr-xr-x    7 ftp      ftp           142 Sep 10 09:12 debian-security
-rw-r--r--    1 ftp      ftp           571 Sep 10 10:44 debian-sources.list
-rw-r--r--    1 ftp      ftp           566 Apr 16  2014 ftp-sources.list
drwxr-xr-x    4 ftp      ftp           127 Sep 10 09:13 raspbian
drwxr-xr-x   12 ftp      ftp          4096 Sep 10 10:13 releases
drwxr-xr-x    7 ftp      ftp          4096 Sep 10 09:30 ubuntu
-rw-r--r--    1 ftp      ftp           862 Sep 10 10:44 ubuntu-sources.list
>>> print(data)
226 Directory send OK.
>>> ftp.retrlines('LIST')
drwxr-xr-x  198 ftp      ftp          8192 Sep 09 12:30 apache
drwxr-xr-x    9 ftp      ftp          4096 Sep 10 09:15 debian
drwxr-xr-x    5 ftp      ftp           102 Sep 10 09:12 debian-backports
drwxr-xr-x    5 ftp      ftp           127 Sep 08 16:43 debian-cd
drwxr-xr-x    7 ftp      ftp           142 Sep 10 09:12 debian-security
-rw-r--r--    1 ftp      ftp           571 Sep 10 10:44 debian-sources.list
-rw-r--r--    1 ftp      ftp           566 Apr 16  2014 ftp-sources.list
drwxr-xr-x    4 ftp      ftp           127 Sep 10 09:13 raspbian
drwxr-xr-x   12 ftp      ftp          4096 Sep 10 10:13 releases
drwxr-xr-x    7 ftp      ftp          4096 Sep 10 09:30 ubuntu
-rw-r--r--    1 ftp      ftp           862 Sep 10 10:44 ubuntu-sources.list
'226 Directory send OK.'
>>> print(data)
226 Directory send OK.
>>> ftp.cwd('debian')
'250 Directory successfully changed.'
out = '/f/MinicondaLinux/README.html'
>>> with open(out, 'wb') as f:
...     ftp.retrbinary('RETR ' + 'README.html', f.write)
'226 Transfer complete.'


