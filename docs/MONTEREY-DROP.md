# macOS Monterey Support

With OpenCore Legacy Patcher v0.1.7 and newer, we've implemented beta macOS Monterey support for users. Please note that Apple has dropped a lot of hardware with this release as well as broken many of our previous patch sets. This page will be used to inform users regarding current issues and will be updated as new patch sets are developed and added to our patcher.

Current models with full, unhindered support in OpenCore Legacy Patcher are the following:

* iMac13,x and newer
  * iMac13,x series must have a Nvidia dGPU for best support
  * iMac10,1-12,x included if Wireless Card and Bluetooth upgraded as well as Metal GPU
* Macmini7,1 and newer
* MacBook8,1 and newer
* MacBookAir6,x and newer
* MacBookPro11,x and newer
* MacPro3,1 and newer
  * Requires Wireless Card and Bluetooth upgrade for 3,1-5,1 as well as Metal GPU
 
 
## Newly dropped hardware

With Monterey, Apple continues their their somewhat ruthless march of dropping Intel hardware. This release saw the removal, and thus addition into OpenCore Legacy Patcher, of the following models:

* iMac14,4
* iMac15,1
* MacBook8,1
* MacBookAir6,1
* MacBookAir6,2
* MacBookPro11,1
* MacBookPro11,2
* MacBookPro11,3

All of these models now have support in OpenCore Legacy Patcher. Note iMac15,1 does have [an unfortunate firmware bug preventing resolutions above 4k](https://github.com/dortania/OpenCore-Legacy-Patcher/issues/359) with OpenCore Legacy Patcher

## Current Hardware Drawbacks:

Below is a list of hardware that currently has issues with Monterey:

* [Acceleration Support Dropped](#acceleration-support-dropped)
  * [Metal GPUs](#metal-gpus)
  * [Non-Metal GPUs](#non-metal-gpus)
* [Bluetooth Support Dropped](#bluetooth-support-dropped)
* [Wireless Support Dropped](#wireless-support-dropped)

## Acceleration Support Dropped

### Metal GPUs

* Intel HD4000 iGPUs lost support
  * Re-introduced with OpenCore Legacy Patcher v0.1.7

By default these machines require root volume patches to gain graphics acceleration in Monterey. OpenCore Legacy Patcher supports readding support however SIP and FileVault can no longer be enabled due to root patching:

* Macmini6,x
* MacBookAir5,x
* MacBookPro9,x
* MacBookPro10,x

### Non-Metal GPUs

* Non-Metal GPUs no longer have working acceleration patches:
  * Intel Ironlake and Sandy Bridge iGPUs
  * Nvidia Tesla and Fermi GPUs
  * AMD TeraScale 1 and 2 GPUs

The following machines cannot gain graphics acceleration at all in Monterey, only basic framebuffer and brightness control (iMac8,1/9,1 and MacBook5,2 excluded):

* iMac12,x and older
* Macmini5,x and older
* MacBook7,1 and older
* MacBookAir4,x and older
* MacBookPro8,x and older

Note: iMac10,1 through iMac12,x can be upgraded with Metal GPUs, [see here for more info](https://forums.macrumors.com/threads/2011-imac-graphics-card-upgrade.1596614/)

## Bluetooth Support Dropped

* BRCM2046 and BRCM2070 Bluetooth Chipsets lost support

The following models lost Bluetooth support in macOS Monterey due to their legacy Bluetooth chipset:

* iMac12,x and older
* Macmini5,1 and older
* MacBook7,1 and older
* MacBookAir4,1 and older
* MacBookPro8,1 and older
* MacPro5,1 and older

::: details Dropped Firmwares

Here are the firmwares macOS Monterey Dropped (previously located within IOBluetoothUSBDFU.kext):

* 2046_820F.dfu
* 2046_8210.dfu
* 2046_8213.dfu
* 2046_8215.dfu
* 2046_8216.dfu
* 2046_8217.dfu
* 2070_821A.dfu
* 2070_821B.dfu
* 2070_8218.dfu
* 20702_821D.dfu
* 20702_821F.dfu
* 20702_828A.dfu
* 20702_828B.dfu
* 20702_828C.dfu
* 20702_8281.dfu
* 20702_8286.dfu

:::

Note: Native BRCM20702 and BRCM20703 are still fully support by OpenCore Legacy Patcher

### macOS 12.0 Beta 4 issue on 2011 to early 2013 machines

Currently in macOS 12.0 Beta 4, many Sandy and Ivy Bridge Macs have experienced Bluetooth issues relating to their BCM94331 chipset. Currently the exact issue is unknown however is assumed to be a bug on Apple's end. Recommend downgrading to macOS 12.0 Beta 3 till resolved:

* [12.0 Beta 3 (21A5284e) InstallAssistant (Direct)](http://swcdn.apple.com/content/downloads/02/08/071-63739-A_G5RYVW5JHT/dfz5gp3s0jm9vl7m30oewq141zkpv8edr8/InstallAssistant.pkg)
* [12.0 Beta 3 (21A5284e) InstallAssistant (archive.org)](https://archive.org/details/12.0-21a5284e-beta-3)

A temporary fix is to restart the BlueTool and bluetoothd process with each boot, note it may not work for all users:

```sh
sudo killall -9 BlueTool bluetoothd
```

## Wireless Support Dropped

* Broadcom BCM94328, BCM94322 and Atheros Wireless Chipsets lost support

The following models lost Bluetooth support in macOS Monterey due to their legacy Wireless chipset:

* iMac12,x and older
* Macmini3,1 and older
* MacBook5,x and older
* MacBookAir2,1 and older
* MacBookPro7,1 and older
* MacPro5,1 and older

Note: BCM943224, BCM94331, BCM94360 and BCM943602 are still fully support by OpenCore Legacy Patcher
