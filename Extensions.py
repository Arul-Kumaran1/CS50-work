def get_media_type(filename):
    types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    filename = filename.lower()
    filename = filename.strip()

    for extension in types:
        if filename.endswith(extension):
            return types[extension]

    return "application/octet-stream"

filename = input("Name of the file: ")

media_type = get_media_type(filename)

print(media_type)