################################
#
# HELPER FUNCTIONS FOR UPLOADING 
# DOWNLOADING DATA ON GOOGLE DRIVE
# WHEN USING GOOGLE COLAB
#
################################
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

class GoogleDriveIO:
    def __init__(self):
        # 1. Authenticate and create the PyDrive client.
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        self.drive = GoogleDrive(gauth)
    
    def upload(self, filename, title=None):
        """Uploads a file to Google Drive.
        
        title (str) : Name to given file stored on Google Drive (default=None)
        filename (path) : path to the file being uploaded
        
        """
        if not title:
            title = filename
        uploaded = self.drive.CreateFile({'title': title})
        uploaded.SetContentFile(filename)
        uploaded.Upload()
        print(f"Uploaded file with ID {uploaded.get('id')} and title {uploaded.get('title')}")
    
    def download(self, title, filename):
        """Downloads a file from Google Drive.
        
        title (str) : Name to given file stored on Google Drive
        filename (path) : path to where the file will be stored. 
        
        """
        file_id = self.find_file_id_by_title(title)
        if file_id:
            self.download_file_by_id(file_id, filename)
        else:
            print(f"File with title: {title} not found.")
            
    def download_file_by_id(self, file_id, save_as_filename):
        """Download a file by its ID and save it with a specific filename."""
        downloaded = self.drive.CreateFile({'id': file_id})
        downloaded.GetContentFile(save_as_filename)
        print(f"Downloaded the file and saved as {save_as_filename}")

        
    def find_file_id_by_title(self, title):
        """Find a file ID based on its title."""
        file_list = self.drive.ListFile({'q': f"title='{title}'"}).GetList()
        for file in file_list:
            if file['title'] == title:
                return file['id']
        return None
        