#!/usr/bin/env python
"""Download or list files from an Amazon S3 bucket."""
# disable exception warnings
#     pylint: disable=I0011,W0702

import platform
import subprocess
import argparse
import boto3
import Tkinter as tk
import ttk
import AppKit

# download_File = 'i1match 362.dmg'
# TODO (dohare) (before deployment) make functions to get credentials
#      accept username/password in args or raw_input()

#class for user entry
class EntryApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        tk.Label(self, text="Enter AWS_ACCESS code").pack()

        self.entry = tk.Entry(self,textvariable='AWS_ACCESS', bg='white')
        self.entry.pack()

        tk.Label(self, text="Enter AWS_SECRET code").pack()

        self.secret_entry = tk.Entry(self, show='*',textvariable='AWS_SECRET', bg='white')
        self.secret_entry.pack()

        tk.Button(self, text='OK', command=self.ok).pack()

    def ok(self):
        print('Text box: {}\nSecret box: {}'.format(self.entry.get(), self.secret_entry.get()))

AWS_ACCESS = ''
AWS_SECRET = ''
REGION = 'us-east-1'
BUCKET = 'jamfbde1211c73854fcdab1a39a397c87cd3'

S3CLIENT = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=AWS_ACCESS,
    aws_secret_access_key=AWS_SECRET
)


def get_args():
    """Parse arguments and return an argparse Namespace object"""
    parser = argparse.ArgumentParser(description='List, get, and install files from S3')
    parser.add_argument('-l', '--list',
                        help='List all files, or with -f, show file details.\
                              Must use at least -v to get console output.',
                        action='store_true')
    parser.add_argument('-f', '--filename', help='FILENAME from list to find or download.\
                                                  Requires -l, -i, or -o OUTPUT')
    parser.add_argument('-o', '--output', help='Output path including target filename.\
                                                Target filename can be different than original.')
    parser.add_argument('-i', '--install', action='append', dest='install', nargs='*',
                        help='Install file from temp location.\
                              If -o, install from output path instead.\
                              To pass installer options, use -i INSTALL,\
                              where INSTALL is a list of options')
    parser.add_argument('-t', '--options', action='append', dest='options', nargs='*',
                        help='Installer options or msiexec transformations')
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='Increase verbosity, ex: -v, -vv, or -vvv.\
                              No console output without at least -v.')

    args = parser.parse_args()

    if args.filename and not args.list and not args.output and not args.install:
        parser.error("-f requires  -l, -i, or -o OUTPUT")
    if args.install and not args.filename and not args.output:
        parser.error("-i requires -f FILENAME or -o OUTPUT")
    if args.output and not args.filename and not args.install:
        parser.error("-o requires -f FILENAME or -i")
    return args


class Query(object):
    """Query object.

    Contains methods to list and download files.
    """

    def __init__(self, args=None, **kwargs):
        """filename=None, output=None, lst=None, verbosity=None"""
        self.args = argparse.Namespace()
        self.args.filename = None
        self.args.output = None
        self.args.list = False
        self.args.install = None
        self.args.options = None
        self.args.verbosity = 0

        if args is not None:
            self.args = args
        else:
            self.args = get_args()

        all_args = ['filename', 'output', 'list', 'install', 'options', 'verbosity']
        self.__dict__.update((a, v) for a, v in
                             self.args.__dict__.iteritems())
        self.__dict__.update((a, v) for a, v in
                             kwargs.iteritems() if a in all_args)

        self.files = self.get_file_list()
        self.flist = [filedict[u'Key'] for
                      filedict in self.files]


    def get_file_list(self):
        """
        Return a list with a dict for each file in the bucket.
        Used by __init__.
        """
        if self.args.verbosity >= 2:
            print 'Getting file list from bucket: %s' % BUCKET
        try:
            raw_files = S3CLIENT.list_objects(Bucket=BUCKET)
            files = [filedict for filedict in raw_files[u'Contents']]
            if self.args.verbosity >= 2:
                print 'File list ready.'
            return files
        except TypeError:
            print 'Unable to get file list from bucket: %s, \
                   Check your internet connection, and make sure \
                   you can access Amazon S3' % BUCKET


    def find_file(self):
        """
        Find a file in the bucket given a Query containing a filename.
        Return True if found or False if not found.
        Print info with -v, -vv or -vvv (options set in Query).
        """
        fname = self.args.filename

        if fname in self.flist:

            if self.args.verbosity >= 2:
                size = (self.files[self.flist.index(fname)]['Size'] /
                        1024.0) / 1024
                mod = self.files[self.flist.index(fname)]['LastModified']
                print 'Found: %s, Size: %s mb, Modified: %s' % (fname, size, mod)
                if self.args.verbosity >= 3:
                    raw = self.files[self.flist.index(fname)]
                    print 'Raw details:\n%s' % raw
            elif self.args.verbosity >= 1:
                print 'Found: %s' % fname

            return True

        else:
            if self.args.verbosity >= 1:
                print fname + ' NOT FOUND'
            return False


    def list_files(self):
        """
        Return a list all files in bucket.\
        Print list with -v or use -vv to print with size and last mod.
        """
        file_list = []
        for i, name in enumerate(self.flist):
            if self.args.verbosity >= 2:
                size = (self.files[self.flist.index(name)]['Size'] /
                        1024.0) / 1024
                mod = self.files[self.flist.index(name)]['LastModified']
                print '%s: %s, Size: %s mb, Modified: %s' % (i, name, size, mod)
            elif self.args.verbosity >= 1:
                print '%s %s' % (i, name)
            file_list.append(str(name))

        return file_list


    def get_file(self):
        """
        Download a file from S3 given a Query with filename and output attributes.
        Return output path on success, None on failure.
        """
        if not self.args.output:
            self.args.output = '/tmp/' + self.args.filename
        download_args = (BUCKET, self.args.filename, self.args.output)

        if self.args.verbosity >= 2:
            print 'Looking for %s' % self.args.filename

        if self.find_file():
            if self.args.verbosity >= 2:
                print 'Downloading: %s to Output Path: %s' % \
                       (self.args.filename, self.args.output)
            elif self.args.verbosity >= 1:
                print 'Downloading: ' + self.args.filename

            if self.args.verbosity >= 3:
                S3CLIENT.download_file(*download_args)
                print 'File: %s ready at Path: %s' \
                       % (self.args.filename, self.args.output)
                return self.args.output
            else:
                try:
                    S3CLIENT.download_file(*download_args)
                    if self.args.verbosity >= 1:
                        print '%s downloaded' % self.args.filename
                    return self.args.output

                except:
                    if self.args.verbosity >= 1:
                        print 'Download FAILED'
                    return None


    # TODO WORK IN PROGRESS - Need to add and test Windows deployment
    def deploy(self):
        """Install msi in Windows, or pkg in Mac OS"""
        if self.args.filename:
            package = self.get_file()
        else:
            package = self.args.output
        if self.args.verbosity >= 1:
            print 'Instlalling ' + package

        target_os = platform.system()
        if target_os == 'Darwin':
            cmd = ['sudo', '/usr/sbin/installer', '-pkg', package, '-tgt', '/']
        elif target_os == 'Windows':
            msi_location = package
            cmd = ['msiexec', '/i', msi_location, '/qn', 'shell=True']

        if self.args.options:
            if target_os == 'Darwin':
                cmd.extend(['-' + opt for opt in self.args.options])
            elif target_os == 'Windows':
                cmd.append('TRANSFORMS=' + self.args.options)
        if self.args.verbosity >= 3:
            print cmd
        # return
        install_process = subprocess.Popen(cmd, shell=False, bufsize=1,
                                           stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)

        if self.args.verbosity >= 3:
            print str(install_process.communicate()[0])
        elif self.args.verbosity >= 1:
            print str(install_process.communicate()[0]).split('\n')[-2]


def main():
    """Run script."""
    query = Query()
    if query.args.verbosity >= 3:
        print query.args
    if query.args.list and query.args.filename:
        query.find_file()

    elif query.args.list:
        query.list_files()

    elif query.args.install:
        query.deploy()

    elif query.args.filename:
        query.get_file()


if __name__ == '__main__':
    main()
