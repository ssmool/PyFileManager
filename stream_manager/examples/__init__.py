import stream_manager.io as IO
import stream_manager.binary as BINARY
import stream_manager.base64 as BASE64
import stream_manager.cripto as CRIPTO
import stream_manager.server as SERVER

_t_tx0 = ''

#TEST BOARD IO
_t_tx0 = '#TEST BOARD IO'
print(_t_tx0)
_r = IO.OpenWriter('io.txt', 'hello world!')
print(_r)
_r = IO.OpenReader('io.txt')
print(_r)

#TEST BOARD BINARY
_t_tx0 = '#TEST BOARD BINARY'
print(_t_tx0)
_b = bytes([104, 101, 108, 108, 111])
_r = BINARY.OpenBinaryWriter('io_bin.txt', _b)
print(_r)
_r = BINARY.OpenBinaryReader('io_bin.txt')
print(_r)

#TEST BOARD BASE64
_t_tx0 = 'TEST BOARD BASE64'
print(_t_tx0)
_r = BASE64.OpenBase64Writer('io_64.txt', 'hello world =]')
print(_r)
_r = BASE64.OpenBase64Reader('io_64.txt')
print(_r)

#TEST BOARD CRIPTO
_t_tx0 = '#TEST BOARD CRIPTO'
print(_t_tx0)
_rk = CRIPTO.GenerateCriptoKey()
print(_rk)
_rc = CRIPTO.CriptographyContent('hello world :?', _rk)
print(_rc)
_r = CRIPTO.Uncripto(_rc, _rk)
print(_r)
_r = BASE64.OpenBase64Writer('io_cripot.txt', _rc)
print(_rc)
_r64 = BASE64.OpenBase64Reader('io_cripot.txt')
print(_r64)

#TEST BOARD SERVER
_t_tx0 = '#TEST BOARD SERVER'
print(_t_tx0)
SERVER.OpenFileServer('localhost', 80, 'io_cripot.txt' )

