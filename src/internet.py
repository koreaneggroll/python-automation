import speedtest


def download_speed():
    print("\t\t===DOWNLOAD SPEED===")

    down_speed = speedtest.Speedtest()
    download = down_speed.download()
    print(f"\t\t\t {download}\n")


def upload_speed():
    print("\t\t===UPLOAD SPEED===")

    up_speed = speedtest.Speedtest()
    upload = up_speed.upload()
    print(f"\t\t\t {upload}\n")


def ping():
    print("\t\t===PING===")
    st = speedtest.Speedtest()

    st.get_servers([])
    ping = st.results.ping

    print(f"\t\t\t {ping}ms\n")


def main():
    print("\n\n\t\t\t\t=======INTERNED SPEED=======\n\n\n\n")
    download_speed()
    upload_speed()
    ping()


main()
