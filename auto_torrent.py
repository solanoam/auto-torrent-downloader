from qbittorrent import Client

class AutoTorrentDownloader(object): 
    def __init__(self):
        self.torrent_db_location = "C:/Users/Noam/Dropbox/Dropbox/torrent_db.txt"
        self.added_torrents_db_location = "added_torrent_db.txt"
        self.client = Client('http://127.0.0.1:8080/')

    
    def add_torrent(self, link: str) -> None:
        self.client.download_from_link(link)
    
    def refresh_torrent_list(self):
        torrent_db = self.get_torrent_db()
        added_torrent_db = self.get_added_torrent_db()
        for torrent_link in torrent_db:
            if torrent_link in added_torrent_db:
                continue
            
            self.add_torrent(torrent_link)
            self.add_added_torrent(torrent_link)
    

    def get_db(self, location: str, mode: str) -> []:
        db_object = []
        with open(location, mode) as db:
            for line in db:
                if 'str' in line:
                    break
                db_object.append(line)
        
        return db_object

    def get_torrent_db(self):
        return self.get_db(self.torrent_db_location, "r")

    def get_added_torrent_db(self):
        return self.get_db(self.added_torrents_db_location, "r")

    def add_added_torrent(self, link: str):
        with open(self.added_torrents_db_location, "a") as added_db:
            added_db.write(link)
    

driver = AutoTorrentDownloader().refresh_torrent_list()