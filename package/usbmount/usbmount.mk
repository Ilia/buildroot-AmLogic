#############################################################
#
# usbmount
#
#############################################################
USBMOUNT_VERSION = 0.0.22
USBMOUNT_SOURCE = usbmount_$(USBMOUNT_VERSION).tar.gz
USBMOUNT_SITE = $(BR2_DEBIAN_MIRROR)/debian/pool/main/u/usbmount
USBMOUNT_DEPENDENCIES = udev lockfile-progs util-linux

define USBMOUNT_INSTALL_TARGET_CMDS
	mkdir -p $(TARGET_DIR)/usr/share/usbmount/
	$(INSTALL) -m 0755 package/usbmount/usbmount $(TARGET_DIR)/usr/share/usbmount/usbmount
	$(INSTALL) -m 0644 -D $(@D)/usbmount.rules $(TARGET_DIR)/lib/udev/rules.d/usbmount.rules

	mkdir -p $(TARGET_DIR)/media/
endef

define USBMOUNT_UNINSTALL_TARGET_CMDS
	rm -rf	$(TARGET_DIR)/usr/share/usbmount/usbmount	\
		$(TARGET_DIR)/lib/udev/rules.d/usbmount.rules	\
		$(TARGET_DIR)/media/?
endef

$(eval $(call GENTARGETS,package,usbmount))
