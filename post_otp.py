import urllib2
import shutil

data = open('./otp.bin', 'rb').read()
print("uploading otp file...")
req = urllib2.Request('https://felipejfc.com/a9lh', data)
res = urllib2.urlopen(req)

with open('arm9loaderhax.3dsx', 'wb') as f:
  shutil.copyfileobj(res, f)

print('arm9loaderhax.3dsx received! now check the sha256sums')

print('arm9loaderhax.3ds sha256: ' + res.info().getheader('Installer-Sha256'))
print('otp.bin sha256: ' + res.info().getheader('OTP-Sha256'))

print('press enter to exit')

raw_input()
