#!/usr/bin/env python

import os
from shutil import copyfile
import zipfile

# constructs a zip file containing the binary of the certyflie source code
# along with the binary of the nrf module
#
# @param base_dir {string} - the directory of the certyflie project
#
def construct_firmware(base_dir):
	# copy certyflie and nrf binaries to the same folder
	os.mkdir('certyflie-firmware')
	print('copying certyflie binary')
	bin_path = base_dir + '/obj/cflie.bin'
	print(bin_path)
	copyfile(bin_path, 'certyflie-firmware/cflie.bin')
	print('copying nrf binary')
	copyfile('cf2_nrf-2016.11.bin', 'certyflie-firmware/cf2_nrf-2016.11.bin')
	
	# zip the contents to make the certyflie firmware
	firmware = zipfile.ZipFile('certyflie-firmware.zip', 'w', zipfile.ZIP_DEFLATED)
	for root, dirs, files in os.walk('certyflie-firmware'):
		for file in files:
			print('writing: ', file)
			firmware.write(os.path.join(root, file))
			os.remove(os.path.join(root, file))
	
	print('done')