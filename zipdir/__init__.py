import glob
import tempfile
import zipfile
import pathlib

def zipDirectory( directory, outputFile = None ):
    globPattern = '{}/**'.format( directory )
    files = glob.glob( globPattern, recursive = True )
    with tempfile.NamedTemporaryFile( prefix = 'zipdir_' ) as namedTemporary:
        zipFile = zipfile.ZipFile( namedTemporary.name, 'w' )
        for file in files:
            zipFile.write( file )

        zipFile.close()
        data = pathlib.Path( namedTemporary.name ).read_bytes()
        if outputFile is not None:
            pathlib.Path( outputFile ).write_bytes( data )
        else:
            return data
