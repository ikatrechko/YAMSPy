import struct

def readbytes(data, size=8, unsigned=False, read_as_float=False):
    """Unpack bytes according to size / type

    Parameters
    ----------
    data : bytearray
        Data to be unpacked
    size : int, optional
        Number of bits (8, 16 or 32) (default is 8)
    unsigned : bool, optional
        Indicates if data is unsigned or not (default is False)
    read_as_float: bool, optional
        Indicates if data is read as float or not (default is False)
        
    Returns
    -------
    int
        unpacked bytes according to input options
    """
    buffer = bytearray()

    for _ in range(int(size/8)):
        buffer.append(data.pop(0))
    
    if size==8:
        unpack_format = 'b'
    elif size==16:
        if read_as_float: # for special situations like MSP2_INAV_DEBUG
            unpack_format = 'e'
        else:   
            unpack_format = 'h'
    elif size==32:
        if read_as_float: # for special situations like MSP2_INAV_DEBUG
            unpack_format = 'f'
        else:
            unpack_format = 'i'
    
    if unsigned:
        unpack_format = unpack_format.upper()

    return struct.unpack('<' + unpack_format, buffer)[0]


def bit_check(mask, bit):
    return ((mask>>bit)%2) != 0


def convert(val_list, n=16): 
    """Convert to n*bits (8 multiple) list

    Parameters
    ----------
    val_list : list
        List with values to be converted
    
    n: int, optional
        Number of bits (multiple of 8) (default is 16)
        
    Returns
    -------
    list
        List where each item is the equivalent byte value
    """ 
    buffer = []
    for val in val_list:
        for i in range(int(n/8)): 
            buffer.append((int(val)>>i*8) & 255) 
    return buffer 

def _crc8_dvb_s2(crc, ch):
    """CRC for MSPV2
    *copied from inav-configurator
    """
    crc ^= ch
    for _ in range(8):
        if (crc & 0x80):
            crc = ((crc << 1) & 0xFF) ^ 0xD5
        else:
            crc = (crc << 1) & 0xFF
    return crc
