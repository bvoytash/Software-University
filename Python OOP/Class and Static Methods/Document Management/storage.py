from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for objects in self.categories:
            if objects.name == category.name:
                return
        self.categories.append(category)

    def add_topic(self, topic:Topic):
        for objects in self.topics:
            if objects.id == topic.id:
                return
        self.topics.append(topic)

    def add_document(self, document:Document):
        for objects in self.documents:
            if objects.id == document.id:
                return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        for objects in self.categories:
            if objects.id == category_id:
                objects.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for objects in self.topics:
            if objects.id == topic_id:
                objects.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for objects in self.documents:
            if objects.id == document_id:
                objects.edit(new_file_name)

    def delete_category(self, category_id):
        for objects in self.categories:
            if objects.id == category_id:
                self.categories.remove(objects)

    def delete_topic(self, topic_id):
        for objects in self.topics:
            if objects.id == topic_id:
                self.topics.remove(objects)

    def delete_document(self, document_id):
        for objects in self.documents:
            if objects.id == document_id:
                self.documents.remove(objects)

    def get_document(self, document_id):
        for objects in self.documents:
            if objects.id == document_id:
                return objects

    def __repr__(self):
        result = []
        for objects in self.documents:
            result.append(repr(objects))
        return '\n'.join(result)



