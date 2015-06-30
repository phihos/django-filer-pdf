from filer.models import File
import os


class PDF(File):
    # the icon it will use
    _icon = 'pdf'

    @classmethod
    def matches_file_type(cls, iname, ifile, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.pdf']
        ext = os.path.splitext(iname)[1].lower()
        return ext in filename_extensions
