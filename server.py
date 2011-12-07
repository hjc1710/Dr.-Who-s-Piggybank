#from Crypto.Cipher import AES
import os,random, struct
#import zlib
import gzip



def encrypt_file(input_string):
    key = "29"
    size = len(input_string)
    if (size%2) != 0:
        input_string += " "
    for i in xrange(size/2):
        key += '29'
    input_string = "".join(chr(ord(a)^ord(b))for a,b in zip(input_string,key))
    return input_string

def compress_file(input_string, is_binary = False):
    #f = open(in_filename,"r")
    #string = f.read()
    #f.close()
    #compr = glib.compress(in_filename)
    #output = open(out_filename,"w")
    #output.write(compr)
    #output.close()
    #print input_string
    if is_binary:
        if os.name =='nt':
            file_name = os.getcwd() + '\\tempfileftp.gz'
            tempfile = gzip.open(file_name,'wb')
            tempfile.write(input_string)
            tempfile.close()
        else:
            file_name = os.getcwd() + '/tempfileftp.gz'
            tempfile = gzip.open(file_name,'wb')
            tempfile.write(input_string)
            tempfile.close()
    else:
        if os.name =='nt':
            file_name = os.getcwd() + '\\tempfileftp.txt.gz'
            tempfile = gzip.open(file_name ,'wb')
            #tempfile = gzip.open('test.txt','wb')
            tempfile.write(input_string)
            tempfile.close()
        else:
            file_name = os.getcwd() + '/tempfileftp.txt.gz'
            tempfile = gzip.open(file_name,'wb')
            tempfile.write(input_string)
            tempfile.close()
    #print open(file_name).read()
    #file_name = 'test.txt'    
    return file_name

#Function inputs a compressed file and outputs a string
def decompress_file(in_file):
    #f = open(in_filename,"r")
    #string = f.read()
    #f.close()
    #decomp = zlib.decompress(in_string)
    #output = open(out_filename,"w")
    #output.write(decomp)
    #output.close()
    tempfile = gzip.open(in_file, 'rb')
    output_string = tempfile.read()
    tempfile.close()
    os.remove(in_file)
    return output_string



#
#def encrypt_file(in_filename, out_filename=None, chunksize=64*1024):
#    """ Encrypts a file using AES (CBC mode) with the
#        given key.
#
#        key:
#            The encryption key - a string that must be
#            either 16, 24 or 32 bytes long. Longer keys
#            are more secure.
#
#        in_filename:
#            Name of the input file
#
#        out_filename:
#            If None, '<in_filename>.enc' will be used.
#
#        chunksize:
#            Sets the size of the chunk which the function
#            uses to read and encrypt the file. Larger chunk
#            sizes can be faster for some files and machines.
#            chunksize must be divisible by 16.
#    """
#    
#    key = '86309lonh6bdcx34'
#    
#    if not out_filename:
#        out_filename = in_filename + '.enc'
#
#    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
#    encryptor = AES.new(key, AES.MODE_CBC, iv)
#    filesize = os.path.getsize(in_filename)
#    #filesize = len(in_filename)
#
#    with open(in_filename, 'rb') as infile:
#        with open(out_filename, 'wb') as outfile:
#            outfile.write(struct.pack('<Q', filesize))
#            outfile.write(iv)
#            
#            the_string = ''
#
#            while True:
#                chunk = infile.read(chunksize)
#                if len(chunk) == 0:
#                    break
#                elif len(chunk) % 16 != 0:
#                    chunk += ' ' * (16 - len(chunk) % 16)
#                the_string += encryptor.encrypt(chunk)
#
#                #outfile.write(encryptor.encrypt(chunk))
#            return(the_string)
#
#def decrypt_file(in_filename, out_filename=None, chunksize=24*1024):
#    """ Decrypts a file using AES (CBC mode) with the
#        given key. Parameters are similar to encrypt_file,
#        with one difference: out_filename, if not supplied
#        will be in_filename without its last extension
#        (i.e. if in_filename is 'aaa.zip.enc' then
#        out_filename will be 'aaa.zip')
#    """
#    key = '86309lonh6bdcx34'
#    
#    if not out_filename:
#        out_filename = os.path.splitext(in_filename)[0]
#
##    with open(in_filename, 'rb') as infile:
##        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
##        iv = infile.read(16)
#    decryptor = AES.new(key, AES.MODE_CBC)
##
##        with open(out_filename, 'wb') as outfile:
##            the_string = ''
##            while True:
##                chunk = infile.read(chunksize)
##                if len(chunk) == 0:
##                    break
#    the_string = decryptor.decrypt(in_filename)
#            
##            the_string.truncate(origsize)
#    return the_string
#                
#                #outfile.write(decryptor.decrypt(chunk))
#
#            #outfile.truncate(origsize)
#
#def compress_file(in_filename):
#    #f = open(in_filename,"r")
#    #string = f.read()
#    #f.close()
#    compr = zlib.compress(in_filename)
#    #output = open(in_filename,"w")
#    #output.write(compr)
#    #output.close()
#    return compr
#        
#def decompress_file(in_string):
#    #f = open(in_filename,"r")
#    #string = f.read()
#    #f.close()
#    decomp = zlib.decompress(in_string)
#    #output = open(in_filename,"w")
#    #output.write(decomp)
#    #output.close()
#    return decomp





def get_file_name(path):
    name = ''
    for i in range(len(path) - 1, -1, -1):
        if (path[i] == '/' or path[i] == '\\'):
            break
        name += path[i]
    return name[::-1]


def grab_domain(m):
    email_re = re.compile('^[\w+\-.]+@[A-Za-z\d\-]+\.(?P<domain>[a-z.]+)+$')
    
    matches = re.match(email_re, m)
    
    if not matches:
        return False
    else:
    
        dom = matches.groups()

    #groups = m.groups()
        domains = ['com', 'edu', 'gov', 'org', 'biz', 'cc', 'us', 'uk', 'co', 'net', 'info', 'me', 'mobi', 'jp', 'co.uk']
        if dom[0] in domains:
            return True
        else:
            return False

# Echo server program
import socket
import os
import re
from math import ceil
from stat import *

#datum = open('pg76.txt').read()
#temp_fn = compress_file(datum)
#print open(temp_fn, 'rb').read()
#raw_input()
#string2 = decompress_file(temp_fn)
#
#print string2

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50007
buffsize = 2048
print 'Server hosted on ' + str(HOST) + ' Port ' + str(PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

user_split = re.compile('\!@\!')

while 1:
    print 'Waiting for Connection....'
    conn, addr = s.accept()
    
    conn.send('pwd')
    user = conn.recv(buffsize)
    user_info = user_split.split(user)
    user_name = user_info[0][5:]
    user_pw = user_info[1][9:]
    
    if (user_name != 'anonymous'):
        conn.send('Incorrect Username')
        print str(addr) + ' tried to connect with invalid user name: ' + user_name
        conn.close()
        continue
    else:
        if (not grab_domain(user_pw)):
            conn.send('Incorrect Password')
            print str(addr) + ' tried to connect with invalid password.'
            conn.close()
            continue
        else:
            conn.send('entry')
    
    print 'Connected by', addr
    
    ENCRYPT = False
    COMPRESS = False
    BINARY = False
    
    workingdir = os.curdir
    
    while 1:
        data = conn.recv(buffsize)
        
        # Exit
        if data == 'exit' or data == 'quit':
            conn.send('Goodbye!')
            break
        elif not data:
            break
        
        # LS or DIR        
        elif data == 'ls' or data == 'dir':
            dirs = os.listdir(os.getcwd())
            the_dirs = "\n".join(dirs)
            conn.send(the_dirs)
        
        elif data == 'os':
            conn.send('os is ' + os.name)
            
        # CD        
        elif data[0:2] == 'cd':
            print data[3:]
            os.chdir(data[3:])
            
        # PUT        
        elif data[0:3] == 'put':
            pieces = user_split.split(data)
            print pieces
            fn = pieces[0][7:]
            if '.' not in fn:
                fn += '.txt'
            f = ''
            done = False
            while (not done):
                dat = conn.recv(buffsize)
                
                if ('>>>~~FILE~~DONE~~<<<' in dat):
                    dat = dat.replace('>>>~~FILE~~DONE~~<<<', '')
                    f.rstrip('>>>~~FILE~~DONE~~<<<')
                    done = True
                
                f += dat
            
            if COMPRESS:
                if os.name == 'nt':
                    temp_fp = os.getcwd() + '\\temp_file.gzip'
                else:
                    temp_fp = os.getcwd() + '/temp_file.gzip'
                temp = open(temp_fp, 'wb')
                temp.write(f)
                temp.close()
                f = decompress_file(temp_fp)
                #print f
                #os.remove(temp_fp)
            
            if ENCRYPT:
                f = encrypt_file(f)
                
            if BINARY:
                stor = open(fn, 'wb')
            else:
                stor = open(fn,'w')
            stor.write(f)
            stor.close()
            print fn + ' successfully received'
            
        # GET            
        elif data[0:3] == 'get':
            f = data[7:]
            try:
                if BINARY:
                    f_open = open(f,'rb').read()
                else:
                    f_open = open(f).read()
            except:
                print 'Error ' + f + ' not found'
                conn.send('Error ' + f + ' not found')
                continue
            if (f[0] != '\\' and f[0] != '/' and f[0] != 'C' and f[0] != '.'):
                if (os.name == 'nt'):
                    file_path = os.getcwd() + '\\' + f
                else:
                    file_path = os.getcwd() + '/' + f
            else:
                file_path = f
            fd = 'get FN:' + f
            conn.send(fd)
            
            if ENCRYPT:
                print 'First fifteen characters of file before', f_open[0:15]
                f_open = encrypt_file(f_open)
                print 'First fifteen characters of file after', f_open[0:15]
            
            if COMPRESS:
                print 'Length of file before compression: ', len(f_open)
                compressed_file_name = compress_file(f_open)
                f_open = open(compressed_file_name, 'rb').read()
                #print f_open
                print 'Length of file after compression: ', len(f_open)
            conn.send(f_open)
            conn.send('>>>~~FILE~~DONE~~<<<')
            
            print f + ' successfully sent'
            
            if COMPRESS:
                os.remove(compressed_file_name)
            
        # MPUT        
        elif data[0:4] == 'mput':
            fnum = data[11:]
            
            for i in range(0,int(fnum)):
                conn.send('begin transfer number: ' + str(i))
                data = conn.recv(buffsize)
                print data
                pieces = user_split.split(data)
                fn = pieces[0][7:]
                print fn
                if '.' not in fn:
                    fn += '.txt'
                f = ''
                done = False
                while (not done):
                    dat = conn.recv(buffsize)
                    
                    if ('>>>~~FILE~~DONE~~<<<' in dat):
                        dat = dat.replace('>>>~~FILE~~DONE~~<<<', '')
                        done = True
                    
                    f += dat
                if COMPRESS:
                    if os.name == 'nt':
                        temp_fp = os.getcwd() + '\\temp_file.gzip'
                    else:
                        temp_fp = os.getcwd() + '/temp_file.gzip'
                    temp = open(temp_fp, 'wb')
                    temp.write(f)
                    temp.close()
                    f = decompress_file(temp_fp) 
                
                if ENCRYPT:
                    f = encrypt_file(f)
                
                if BINARY:
                    stor = open(fn, 'wb')
                else:
                    stor = open(fn,'w')
                stor.write(f)
                stor.close()
                print fn + ' successfully received'
                
        #MGET        
        elif data[0:4] == 'mget':
            files = data[5:]
            if files[-1]=='*':
                file_path= files[:-1]
                if not file_path.strip():
                    file_path = os.getcwd()
                contents = os.listdir(file_path)
                files = []
                for i in range(0,len(contents)):
                    if os.name == 'nt':
                        this_path=file_path + '\\' + contents[i]
                    else:
                        this_path=file_path + '/' + contents[i]
                    mode=os.stat(this_path).st_mode
                    if not S_ISDIR(mode):
                        files.append(this_path)
            else:
                files=files.split()
            fd='mget FILES:' + str(len(files))
            conn.send(fd)
            
            for i in range (0,len(files)):
                conn.recv(buffsize)
                sender = open(files[i])
                file_path = files[i]
                if (file_path[0] != "\\" and file_path[0] != '/' and file_path[0] != 'C' and file_path[0] != '.'):
                    if (os.name== 'nt'):
                        file_path = os.getcwd() + '\\' + file_path
                    else:
                        file_path = os.getcwd() + '/' + file_path
                try:
                    if BINARY:
                        sender = open(file_path, 'rb').read()
                    else:
                        sender = open(file_path).read()
                except:
                    print 'File located at: ' + file_path + ' not found.  Ignoring \
                    and moving on.'
                
                file_descriptor = 'get FN:' + get_file_name(file_path)
                fn = get_file_name(file_path)
                print file_descriptor
                conn.send(file_descriptor)
                
                if ENCRYPT:
                    print 'First fifteen characters of file before', sender[0:15]
                    sender = encrypt_file(sender)
                    print 'First fifteen characters of file after', sender[0:15]
                    
                if COMPRESS:
                    print 'Length of file before compression: ', len(sender)
                    compressed_file_name = compress_file(sender)
                    sender = open(compressed_file_name, 'rb').read()
                    #print f_open
                    print 'Length of file after compression: ', len(sender)
                conn.send(sender)
                conn.send('>>>~~FILE~~DONE~~<<<')
                print fn + ' successfully sent'
                                
                if COMPRESS:
                    os.remove(compressed_file_name)
                    
                
                
        # COMPRESSION ON/OFF                
        elif data == 'compress':
            if COMPRESS:
                COMPRESS = False
                print 'Compression disabled'
            else:
                COMPRESS = True
                print 'Compression enabled'
                
        #ENCRYPTION ON/OFF        
        elif data == 'encrypt':
            if ENCRYPT:
                ENCRYPT = False
                print 'Encryption disabled'
            else:
                ENCRYPT = True
                print 'Encryption enabled'
                
        # NORMAL MODE                            
        elif data == 'normal':
            ENCRYPT = False
            COMPRESS = False
            print 'Compression and Encryption disabled'
            
        #BINARY ON/OFF        
        elif data == 'binary':
            BINARY = True
            print 'Binary mode on'
            
        #ASCII ON/OFF        
        elif data == 'ascii':
            BINARY = False
            print 'ASCII mode on'
            
    conn.close()
    print 'Disconnected by', addr
