# burrito changelog

## Version 0.9.1-dev (changes since 0.9.1 go here)

## Version 0.9.1 (2015-05-22)

* Updated default temporary directory from ``/tmp`` to python's ``tempfile.gettempdir()``. This should address many of the issues with temporary files being written to ``/tmp``, which sometimes doesn't exist, doesn't provide a lot of storage, or is not shared across cluster nodes. It is still possible that individual burrito fillings (i.e., ``CommandLineApplication`` derived classes) can hard code ``/tmp``, so care should be taken when writing those derived classes to avoid that.

## Version 0.9.0 (2014-08-04)

Initial release.
