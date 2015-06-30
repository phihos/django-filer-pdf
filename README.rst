================
django-filer-pdf
================

This is a fork of Patrick Toal's PDF plugin for `django-filer`_. Currently this app does only provide a PDF icon for PDF-files. But maybe more features are added to make the originally intended features happen. Contributions are welcome ;-)

Dependencies
------------

* `django-filer`_ > 0.9a2

Installation
------------

To get started using ``django-filer-pdf`` simply install it with
``pip``::

    $ pip install django-filer-pdf
    

Configuration
-------------

Add ``"filer_pdf"`` to your project's ``INSTALLED_APPS`` setting and run ``syncdb`` or ``migrate``.



================
Original text
================

This app extends `django-filer`_ by adding the following features for PDF files:

 - Thumbnail generation for the first page of PDF documents.
 - Text extraction from PDF for indexing by search engines ( eg: Haystack )

* Currently in "vaporware" state *

Dependencies
------------

* `django-filer`_ > 0.9a2
* `pdfminer`_
* `ImageMagick`_ (for PDF thumbnail generation)

.. _django-filer: https://github.com/stefanfoulis/django-filer
.. _pdfminer: http://www.unixuser.org/~euske/python/pdfminer/
.. _ImageMagick: http://www.imagemagick.org/


