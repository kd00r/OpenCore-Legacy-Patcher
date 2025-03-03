# Handle misc CLI menu options
# Copyright (C) 2020-2021, Dhinak G, Mykola Grymalyuk
from __future__ import print_function
import subprocess

from Resources import Constants, Utilities


class MenuOptions:
    def __init__(self, model, versions):
        self.model = model
        self.constants: Constants.Constants = versions

    def change_verbose(self):
        Utilities.cls()
        Utilities.header(["Set Verbose mode"])
        change_menu = input("Enable Verbose mode(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.verbose_debug = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.verbose_debug = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_verbose()

    def change_oc(self):
        Utilities.cls()
        Utilities.header(["Set OpenCore DEBUG mode"])
        change_menu = input("Enable OpenCore DEBUG mode(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.opencore_debug = True
            self.constants.opencore_build = "DEBUG"
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.opencore_debug = False
            self.constants.opencore_build = "RELEASE"
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_oc()

    def change_kext(self):
        Utilities.cls()
        Utilities.header(["Set Kext DEBUG mode"])
        change_menu = input("Enable Kext DEBUG mode(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.kext_debug = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.kext_debug = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_kext()

    def change_metal(self):
        Utilities.cls()
        Utilities.header(["Assume Metal GPU Always in iMac"])
        print(
            """This is for iMacs that have upgraded Metal GPUs, otherwise
Patcher assumes based on stock configuration (ie. iMac10,x-12,x)

Valid Options:

1. None(stock GPU)
2. Nvidia GPU
3. AMD GPU
Q. Return to previous menu

Note: Patcher will detect whether hardware has been upgraded regardless, this
option is for those patching on a different machine or OCLP cannot detect.
        """
        )
        change_menu = input("Set GPU Patch type(ie. 1): ")
        if change_menu == "1":
            self.constants.metal_build = False
            self.constants.imac_vendor = "None"
        elif change_menu == "2":
            self.constants.metal_build = True
            self.constants.imac_vendor = "Nvidia"
        elif change_menu == "3":
            self.constants.metal_build = True
            self.constants.imac_vendor = "AMD"
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_metal()

    def change_serial(self):
        Utilities.cls()
        Utilities.header(["Set SMBIOS Spoof Level"])
        print(
            """This section is for setting how OpenCore generates the SMBIOS
Recommended for adanced users who want control how serials are handled

Valid options:

1. Minimal:\tUse original serials and minimally update SMBIOS
2. Moderate:\tReplace entire SMBIOS but keep original serials
3. Advanced:\tReplace entire SMBIOS and generate new serials
Q. Return to previous menu

Note: For new users we recommend leaving as default(1. Minimal)
        """
        )
        change_menu = input("Set SMBIOS Spoof Level(ie. 1): ")
        if change_menu == "1":
            self.constants.serial_settings = "Minimal"
        elif change_menu == "2":
            self.constants.serial_settings = "Moderate"
        elif change_menu == "3":
            self.constants.serial_settings = "Advanced"
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_serial()

    def change_showpicker(self):
        Utilities.cls()
        Utilities.header(["Set OpenCore Picker mode"])
        print(
            """By default, OpenCore will show its boot picker each time on boot up,
however this can be disabled by default and be shown on command by repeatedly
pressing the "Esc" key
        """
        )
        change_menu = input("Show OpenCore Picker by default(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.showpicker = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.showpicker = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_showpicker()

    def change_vault(self):
        Utilities.cls()
        Utilities.header(["Set OpenCore Vaulting"])
        print(
            """By default, this patcher will sign all your files and ensure none of the
contents can be tampered with. However for more advanced users, you may
want to be able to freely edit the config.plist and files.

Note: For security reasons, OpenShell will be disabled when Vault is set.

        """
        )
        change_menu = input("Enable Vault(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.vault = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.vault = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_vault()

    def change_sip(self):
        Utilities.cls()
        Utilities.header(["Set System Integrity protection"])
        print(
            """SIP is used to ensure proper secuirty measures are set,
however to patch the root volume this must be disabled.
Only disable is absolutely necessary. SIP value = 0xFEF

Valid options:

1. Enable SIP
2. Disable SIP
Q. Return to previous menu

        """
        )
        change_menu = input("Set SIP: ")
        if change_menu == "1":
            self.constants.sip_status = True
        elif change_menu == "2":
            self.constants.sip_status = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_sip()

    def change_sbm(self):
        Utilities.cls()
        Utilities.header(["Set SecureBootModel"])
        print(
            """SecureBootModel is used to ensure best firmware security,
however to patch the root volume this must be disabled.
Only disable is absolutely necessary. SIP value = 0xFEF

Valid options:

1. Enable SecureBootModel
2. Disable SecureBootModel
Q. Return to previous menu

        """
        )
        change_menu = input("Set SecureBootModel: ")
        if change_menu == "1":
            self.constants.secure_status = True
        elif change_menu == "2":
            self.constants.secure_status = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.change_sbm()

    def set_amfi(self):
        Utilities.cls()
        Utilities.header(["Set AMFI"])
        print(
            """Required for Root Patching non-Metal GPUs
in macOS Big Sur. Without this, will receive kernel panic once
Patcher finishes installing legacy acceleration patches.
        """
        )
        change_menu = input("Disable AMFI(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.amfi_status = False
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.amfi_status = True
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.set_amfi()

    def bootstrap_setting(self):
        Utilities.cls()
        Utilities.header(["Set Bootstrap method"])
        print(
            """Sets OpenCore's bootstrap method, currently the patcher supports the
following options.

Valid options:

1. System/Library/CoreServices/boot.efi (default)
2. EFI/BOOT/BOOTx64.efi
Q. Return to previous menu

Note: S*/L*/C*/boot.efi method is only installed to the EFI partition only
and not to macOS itself.

Recommended to set to BOOTx64.efi in situations where your Mac cannot
see the EFI Boot entry in the boot picker.

        """
        )
        change_menu = input("Set Bootstrap method: ")
        if change_menu == "1":
            self.constants.boot_efi = False
        elif change_menu == "2":
            self.constants.boot_efi = True
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.bootstrap_setting()

    def drm_setting(self):
        Utilities.cls()
        Utilities.header(["Set DRM preferences"])
        print(
            """Sets OpenCore's DRM preferences for iMac13,x and iMac14,x.
In Big Sur, some DRM based content may be broken by
default in AppleTV, Photobooth, etc.

To resolve, you can opt to disable Intel QuickSync support in
favor of Nvidia's Software rendering. This can aid in DRM however
greatly hampers Video rendering performance in Final Cut Pro and
other programs relying on such features.

Recommend only disabling if absolutely required.
        """
        )
        change_menu = input("Enable Nvidia's Software DRM rendering(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.drm_support = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.drm_support = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.drm_setting()

    def allow_native_models(self):
        Utilities.cls()
        Utilities.header(["Allow OpenCore on native Models"])
        print(
            """Allows natively supported Macs to use OpenCore. Recommended
for users with 3rd Party NVMe SSDs to achieve improved overall
power usage.

        """
        )
        change_menu = input("Allow OpenCore on all Models(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.allow_oc_everywhere = True
            self.constants.serial_settings = "None"
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.allow_oc_everywhere = False
            self.constants.serial_settings = "Minimal"
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_native_models()

    def custom_cpu(self):
        Utilities.cls()
        Utilities.header(["Set custom CPU Model Name"])
        print(
            """Change reported CPU Model name in About This Mac
Custom names will report as follows:

1: Original Name: 2.5 Ghz Dual-Core Intel Core i5
2. CPU name:      Intel(R) Core(TM) i5-3210M CPU @ 2.50Ghz
3. Custom Name:   2.5Ghz Cotton Candy (example)
Q. Return to previous menu
        """
        )
        if self.constants.custom_cpu_model_value == "":
            if self.constants.custom_cpu_model == 0:
                print("Currently using original name")
            else:
                print("Currently using CPU name")
        else:
            print(f"Custom CPU name currently: {self.constants.custom_cpu_model_value}")
        change_menu = input("Set custom CPU Name(1,2,3): ")
        if change_menu == "1":
            self.constants.custom_cpu_model = 2
            self.constants.custom_cpu_model_value = ""
        elif change_menu == "2":
            self.constants.custom_cpu_model = 0
            self.constants.custom_cpu_model_value = ""
        elif change_menu == "3":
            self.constants.custom_cpu_model = 1
            self.constants.custom_cpu_model_value = input("Enter new CPU Name: ")
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.custom_cpu()

    def disable_cpufriend(self):
        Utilities.cls()
        Utilities.header(["Disable CPU Friend?"])
        print(
            """Only recommended for advanced users
Disabling CPUFriend forces macOS into using a different
Mac's power profile for CPUs and GPUs, which can harm the
hardware
        """
        )
        change_menu = input("Disable CPU Friend?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.disallow_cpufriend = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.disallow_cpufriend = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.disable_cpufriend()

    def set_smbios(self):
        Utilities.cls()
        Utilities.header(["Set SMBIOS Spoof Model"])
        print(
            """Change model OpenCore spoofs Mac too

Valid options:
1. Default set by OpenCore (Default)
2. User Override
3. Disable all spoofing (unsupported configuration)
Q. Return to previous menu
        """
        )

        change_menu = input("Set SMBIOS Spoof Model: ")
        if change_menu == "1":
            print("Setting SMBIOS spoof to default mode")
            self.constants.override_smbios = "Default"
        elif change_menu == "2":
            custom_smbios = input("Set new SMBIOS mode: ")
            try:
                test = self.constants.board_id[custom_smbios]
                self.constants.override_smbios = custom_smbios
            except KeyError:
                print("Unsupported SMBIOS, defaulting to Default setting")
                self.constants.override_smbios = "Default"
        elif change_menu == "3":
            print("Disabling SMBIOS spoof")
            self.constants.override_smbios = self.model
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.set_smbios()

    def allow_firewire(self):
        Utilities.cls()
        Utilities.header(["Allow FireWire Boot Support"])
        print(
            """
In macOS Catalina and newer, Apple restricted
usage of FireWire devices to boot macOS for
security concerns relating to DMA access.

If you are comfortable lowering the security,
you can re-enable FireWire support for Catalina
and newer.

Note: MacBook5,x-7,1 don't support FireWire boot
        """
        )

        change_menu = input("Enable FireWire Boot support?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.firewire_boot = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.firewire_boot = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_firewire()

    def allow_nvme(self):
        Utilities.cls()
        Utilities.header(["Allow NVMe UEFI Support"])
        print(
            """
For machines not natively supporting NVMe,
this option allows you to see and boot NVMe
drive in OpenCore's picker

Not required if your machine natively supports NVMe

Note: You must have OpenCore on a bootable volume
first, ie. USB or SATA drive. Once loaded,
OpenCore will enable NVMe support in it's picker
        """
        )

        change_menu = input("Enable NVMe Boot support?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.nvme_boot = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.nvme_boot = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_nvme()

    def allow_wowl(self):
        Utilities.cls()
        Utilities.header(["Allow Wake on WLAN"])
        print(
            """
Due to an unfortunate bug in macOS Big Sur+, Wake on WLAN is
disabled by default for BCM943224, BCM94331 and BCM94360/2 chipsets.

This is due to Wake on WLAN creating network instability and in other cases
halving network speeds. This issue is not replicable across machines however
be prepared if enabling.
        """
        )

        change_menu = input("Allow Wake on WLAN?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.enable_wake_on_wlan = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.enable_wake_on_wlan = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_wowl()

    def allow_ivy(self):
        Utilities.cls()
        Utilities.header(["Allow Ivy iMac iGPU"])
        print(
            """
For iMac13,x systems with a Nvidia dGPU, the iGPU is disabled by default to
allow Delta Updates, FileVault, SIP and such on macOS Monterey. However due to
this, DRM and QuickSync support may be broken.

Users can choose to override this option but be aware SIP and FileVault must be
disabled to run root patches to fix DRM and QuickSync.

Note: This does not apply for Big Sur, the iGPU can be renabled without
consequence
Note 2: This setting only affects iMac13,x with dGPUs
        """
        )

        change_menu = input("Allow Ivy iMac iGPU?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.allow_ivy_igpu = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.allow_ivy_igpu = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_ivy()

    def latebloom_settings(self):
        Utilities.cls()
        Utilities.header(["Set latebloom properties"])
        print(
            f"""
Set latebloom properties, useful for debugging boot stalls on
pre-Sandy Bridge Macs.

Valid options:

1. Set delay (currently: {self.constants.latebloom_delay}ms)
2. Set range (currently: {self.constants.latebloom_range}ms)
3. Set debug (currently: {bool(self.constants.latebloom_debug)})
Q. Return to previous menu
        """
        )

        change_menu = input("Select latebloom property(1/2/3): ")
        if change_menu == "1":
            try:
                self.constants.latebloom_delay = int(input("Set delay: "))
            except ValueError:
                input("Invalid value, press [ENTER] to continue")
            self.latebloom_settings()
        elif change_menu == "2":
            try:
                self.constants.latebloom_range = int(input("Set range: "))
            except ValueError:
                input("Invalid value, press [ENTER] to continue")
            self.latebloom_settings()
        elif change_menu == "3":
            try:
                print("Currently supports either 0(False) or 1(True)")
                latebloom_debug = int(input("Set debug(0/1): "))
                if latebloom_debug not in [0, 1]:
                    input("Invalid value, press [ENTER] to continue")
                else:
                    self.constants.latebloom_debug = latebloom_debug
            except ValueError:
                input("Invalid value, press [ENTER] to continue")
            self.latebloom_settings()
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.latebloom_settings()

    def allow_moj_cat_patch(self):
        Utilities.cls()
        Utilities.header(["Allow Root Patching on Mojave/Catalina"])
        print(
            """
This is an experimental option that allows the usage of legacy acceleration
patches in Mojave and Catalina.

The main goal of this is to allow developers to better test patch sets as well
as allow acceleration on TeraScale 2 machines. Not all features may be available
(ie. GPU switching may not work, FileVault is not supported, etc)

Note: for the average user, we recommend using dosdude1's legacy patcher:

- http://dosdude1.com/software.html
        """
        )

        change_menu = input("Allow Root Patching on Mojave/Catalina?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.moj_cat_accel = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.moj_cat_accel = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.allow_moj_cat_patch()

    def disable_thunderbolt(self):
        Utilities.cls()
        Utilities.header(["Disable Thunderbolt on 2013-14 MacBook Pros"])
        print(
            """
Some 2013-14 MacBook Pro's have issues with the built-in thunderbolt,
resulting in kernel panics and random shutdowns.

To alliviate, you can disable the thunderbolt controller on MacBookPro11,x 
machines with this option.

Note: This option only works on MacBookPro11,x, file an issue if you know of
other devices that benefit from this fix.
        """
        )

        change_menu = input("Disable Thunderbolt?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.disable_thunderbolt = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.disable_thunderbolt = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.disable_thunderbolt()

    def terascale_2_accel(self):
        Utilities.cls()
        Utilities.header(["Set TeraScale 2 Acceleration"])
        print(
            """
By default this patcher will install TeraScale 2 acceleration, however
for some laptops this may be undesired due to how degraded their dGPU
is.

Disabling TeraScale 2 acceleration will instead install basic framebuffer
support allowing for basic brightness control and let the HD3000 iGPU
handle acceleration tasks.
        """
        )

        change_menu = input("Allow TeraScale 2 Acceleration?(y/n/q): ")
        if change_menu in {"y", "Y", "yes", "Yes"}:
            self.constants.allow_ts2_accel = True
        elif change_menu in {"n", "N", "no", "No"}:
            self.constants.allow_ts2_accel = False
        elif change_menu in {"q", "Q", "Quit", "quit"}:
            print("Returning to previous menu")
        else:
            self.terascale_2_accel()

    def dump_hardware(self):
        Utilities.cls()
        Utilities.header(["Dumping detected hardware"])
        print("")
        print(self.constants.computer)
        input("\nPress [ENTER] to exit: ")
