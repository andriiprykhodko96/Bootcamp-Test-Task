from TikTokApi import TikTokApi
from re import findall
from getpass import getuser
from os import path, mkdir


def download_tt(link):
    with TikTokApi() as api:
        print("Trying to download your video...")
        id = str(max(findall("[0-9]+", link)))
        video = api.video(id=id)
        video_data = video.bytes()

        path_to_save = "C:/Users/{0}/Gifs".format(getuser())
        if not path.exists(path_to_save):
            print("Creating folder to save GIFs...")
            mkdir(path_to_save)
            print("Folder was created!")
        full_path = path_to_save+"/"+id+".gif"
        with open(full_path, "wb") as out_file:
            out_file.write(video_data)
        print("GIF was saved at", full_path)
        return full_path


if __name__ == '__main__':
    link = "https://www.tiktok.com/@stargripper44/video/7113237891983101190?is_from_webapp=1&sender_device=pc"
    link1 = "https://www.tiktok.com/@eduarduky/video/7121437356841897222?is_from_webapp=1&sender_device=pc"
    download_tt(link1)
