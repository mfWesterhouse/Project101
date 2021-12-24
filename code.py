import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A-vvEprr3For4YlNeBAuAJgh_GBJJR_rD4p0rLY0L5_Hlj-9RIAHN3vazMbn3WBIVrMtONW29wT4bXvEVH0Mwzq_n8ZGvE2-ewqL2KjMl26Wjt9eWeOIjG5sdHvIySXNhq8DYW8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to Dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()