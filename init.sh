sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
git config user.email "s@s.r"
git config user.name "s@s.r"
alias ll='ls -ilhao --color=auto' 
mkdir /home/box/.ssh 
chmod 755 /home/box/.ssh 
echo "-----BEGIN RSA PRIVATE KEY-----MIIEowIBAAKCAQEAskiO1agXd9KbPcUJjX/BTjJ+06stBGaOjFL4P2LkxyHHRbB2gEYz9vLRv54yFL9yta6dZm8ehTa9UR1GHAOTNRSGMcLAtg0Pae3ENiCPZVp5a5vfSTbK/eeFExPrbFMb5CJABoMlpvVA/Y8n8IpENzBFQCWwgM7ikkUNykYwaLBgm1xeS7HVfiQ3lIGGSWdi2AfT0PXMgGBJ9gQIQTx9aPZ9JRR9Ac7qpFIzCHN+rjwZT5on7Zf/esxoCWrfpOZ/3CHtc3+P0AFLJn6AxGIaMYS4YTOSm7nHQP/ojUJ2j5R1mIQkBG4NKQI/81SsGnf2skBsClpTxGrFVcF3/KuvfwIDAQABAoIBAQCMXgJPiAPKLIBbttnZlX+N4MXoQ7qy30hWhTC9P1Ce1CJ/5Pq37g4V3YJ1GsmVelKHZw64Sr695aZSyficL9hkD1/Ep/BwpYHARhqY/zPHed9lcRjxHPnfxLwKlEFkTV8FVE4Skok/lZNwz5iDk2k4BoJPih0YnUrYHRRJcM/Ga970VR4rydFRqyH0fQwQQ5EO+pYNKXxkr7ntU+qD7aafkgu/RinnV7dBNX002OQ3Y+wCj7KH9BRbdsBX4g4cJZn2/oW50kM2Rn0tGJ0BeRwnPOG7zlXZ66AVIaWqohOHZHmLiMpeyHCMUywdiywbN/P4uKlzsJDfmQnRSVXXc+yhAoGBAOKtIXL4TOLqOPHFpJIz0EhSntmj2hk8+hnJJH0vEjWtl1V3RAN3pNdaHV3/ZMPRdU/1VkvudCROW49HdrBOA6L6b569muIEsKOiRneQ5j0t5BCT/ZQohPQpPsW6q+wBEO8ZsfuovZDFvalecjhK6ZAeSAxW6auB0bJxRUTHI+pPAoGBAMlYy1nmR5sOsy/IF0LkxH+LzpcZfQixEaTbEQdE1Foh5jxYp0jtD4EiXPeiUpnHYKkP055b1as9Sz7mAsf9Ic/Lrj7aNddaRwbx4+k4S7clxC8KDSs3A1cXIXJNRK7vk8yCfZtmFtyGVgZubYZ8/o5D7kgX2PYsEuwSyyOkOAvRAoGAVwhYfnc9tiZuRM45GPWR9CLc4P2bgPM7p+jl/La1DC0hnOwVDivC+/iaq/uiadkjbNbrEm5043e+ie3LcXgSx2HWt6FfNYbNd5aX7dKRxE25cnAP/fHs0n5/npXE6vGh2dwIzXKFjm+OGdisjFafBPnLeglo4LQQmq4JBZZcgNsCgYBin2iztzUZwUCJxgOG05FgPDXME0MIT9spmdgkbFVrdLFWm8IM2Xk/snpBHbRB+MPi64qnRapKPzKtM3LnTJkUNFs8FBxNSL4Dq9YL9XQ42HnY5J6ArWiobv8GAs0Ctvz5Lm2iAYZvLCnU6qAhQPZa7vE3RN8T7ZCzK51u7tA5EQKBgCKSZiv8ovMVGrvfJjw+kTwwedEHhQSJY66ODxvH0HwyrIPrd9Sn9U7+D5LRuyO4qsDW7gGeUpgpPhOSbug8pt2iQpownIRu8m/+hPS9UwzFvkvs4T5Bh4V5TeYm56BH7Bz9XsxkihYARk3kk4kkPLlqweQWNCy1ecEuXCH+5qwD-----END RSA PRIVATE KEY-----" >/home/box/.ssh/id_rsa
chmod 600 /home/box/.ssh/id_rsa
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCySI7VqBd30ps9xQmNf8FOMn7Tqy0EZo6MUvg/YuTHIcdFsHaARjP28tG/njIUv3K1rp1mbx6FNr1RHUYcA5M1FIYxwsC2DQ9p7cQ2II9lWnlrm99JNsr954UTE+tsUxvkIkAGgyWm9UD9jyfwikQ3MEVAJbCAzuKSRQ3KRjBosGCbXF5LsdV+JDeUgYZJZ2LYB9PQ9cyAYEn2BAhBPH1o9n0lFH0BzuqkUjMIc36uPBlPmiftl/96zGgJat+k5n/cIe1zf4/QAUsmfoDEYhoxhLhhM5KbucdA/+iNQnaPlHWYhCQEbg0pAj/zVKwad/ayQGwKWlPEasVVwXf8q69/ s@s.r#stepic-pyweb">/home/box/.ssh/id_rsa.pub
chmod 600 /home/box/.ssh/id_rsa.pub
eval "$(ssh-agent -s)"
eval "$(ssh-agent)"   
ssh-add /home/box/.ssh/id_rsa
#loook at http://pastebin.com/88rpiTiF
