class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.__photos = [PhotoAlbum.photos_per_page * [None] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.__photos):
            for i, photo in enumerate(page):
                if not photo:
                    self.__photos[index][i] = label
                    return f"{label} photo added successfully on page {index + 1} slot {i + 1}"
        return "No more free slots"

    @property
    def photos(self):
        result = []
        for page in self.__photos:
            current_page = []
            for photo in page:
                if photo:
                    current_page.append(photo)
            result.append(current_page)
        return result

    def display(self):
        message = []
        dashes = "-"*11
        for pages in self.photos:
            current = ""
            message.append(dashes)
            for photo in pages:
                if photo:
                    current += "[] "
            message.append(current.rstrip())
            # message.append(dashes)
        message.append(dashes)
        return "\n".join(message)




album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
