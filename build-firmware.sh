#!/bin/bash

# set certyflie to equal the location of the Certyflie repository on your machine
# NB: unix style file separators '/' will also work for windows in this case.
#     this saves having to escape the windows file separators ('\' -> '\\')
certyflie=<PATH TO CERTYFLIE SOURCE CODE>

python -c "import line_ending_converter;line_ending_converter.convert_line_endings('$certyflie')"
gprbuild -P $certyflie/cf_ada_spark.gpr -p
arm-eabi-objcopy $certyflie/obj/cflie.elf -O binary $certyflie/obj/cflie.bin
python -c "import construct_firmware;construct_firmware.construct_firmware('$certyflie')"
rmdir certyflie-firmware