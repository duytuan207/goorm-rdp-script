print("This script was created by duytuan207. Follow them on github https://github.com/duytuan207")
import os, subprocess
username=input("Nhập tên người dùng của bạn:")
password=input("Gõ mật khẩu:")
print("Hãy nhớ mật khẩu này vì nó sẽ được sử dụng trong khi cung cấp các lệnh siêu người dùng trên máy tính của bạn \n khi tạo người dùng của bạn....hãy kiên nhẫn một chút")
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
print(f"Người dùng được tạo và định cấu hình có tên người dùng `{username}` và mật khẩu `{password}`")
CRP= input("Dán Lệnh Chrome Remote Desktop mà bạn đã sao chép:")
Pin=input("Chọn mã pin cho RDP chrome của bạn (tối thiểu 6 chữ số):")
print("Github tác giả: github.com/duytuan207")
Autostart = True
class CRD:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.finish(user)
        print("\nRDP được tạo thành công chuyển sang https://remotedesktop.google.com/access")
    @staticmethod
    def installCRD():
        print("Tải Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("systemctl disable lightdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Tải Google Chrome")
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)
        os.system("wget https://dl1.pling.com/api/files/download/j/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUzMDc3NDYwMCwidSI6bnVsbCwibHQiOiJkb3dubG9hZCIsInMiOiIzM2ExNWQ3YWU0MTNhMTE2ZWJlY2E4YzZmOWFmYjhkNTE0Y2NmMmU0Y2U3ZTUzZDUyOWU0NDQ5YjY1N2Y3YmQ3MjMxNTIwZDRlZGE5ZjhiMWRmYjZiOTQ2Y2ZiNzU0OGJiODFhYjcxNTZhYTZiYWQ4M2UwYjA2MmEyMTY3NzcyNCIsInQiOjE2NDU1MTM0OTcsInN0ZnAiOiIyNGFhYWZiMWVhZmU2ZjU1YzUwMTI3ZmViMGJmOTdkNCIsInN0aXAiOiIzNS4xNTQuMTY2LjE1NSJ9.pfHVPOG-fhRwKRsVdNWiyaoepEIsw-3wqAosQcbwAE4/ocs-url_3.1.0-0ubuntu1_amd64.deb")
        os.system("dpkg -i ocs-url_3.1.0-0ubuntu1_amd64.deb")
        os.system("apt-get install -y curl gnupg wget htop sudo git git-lfs software-properties-common build-essential libgl1 zip unzip")
        os.system("curl -sL https://deb.nodesource.com/setup_18.x")
        os.system("sudo apt install nodejs -y")
        os.system("sudo apt install -f -y")

    @staticmethod
    def finish(user):
        print("Finalizing")
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "https://github.com/duytuan207/"
            colab_autostart = """[Desktop Entry]

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")

        os.system(f"adduser {user} chrome-remote-desktop")
        os.system("wget -O ~/Pictures/wall.jpg https://w.wallhaven.cc/full/9m/wallhaven-9m7l2k.jpg")
        os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s ~/Pictures/wall.jpg")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        

        print("Đã thành công!")
        print("RDP tạo thành công và chuyển về https://remotedesktop.google.com/access")

try:
    if CRP == "":
        print("Vui lòng nhập mã xác thực từ liên kết đã cho")
    elif len(str(Pin)) < 6:
        print("Nhập mật khẩu ít nhất 6 chữ số")
    else:
        CRD(username)
except NameError as e:
    print("'username' không thấy, tạo người dùng trước...")
