from django.db import models


class Model_notes_of_user(models.Model):
    title_note = models.CharField(max_length=200)
    text_note = models.TextField()
    date_note = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title_note