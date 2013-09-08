#############################################################
#
# tvheadend
#
##############################################################

TVHEADEND_VERSION = v3.4
TVHEADEND_SITE_METHOD = git
TVHEADEND_SITE = git://github.com/tvheadend/tvheadend.git
TVHEADEND_INSTALL_STAGING = YES
TVHEADEND_INSTALL_TARGET = YES
TVHEADEND_DEPENDENCIES = v4lutils openssl

ifeq ($(BR2_PACKAGE_AVAHI),y)
TVHEADEND_DEPENDENCIES     += avahi
endif

ifeq ($(BR2_PACKAGE_ZLIB),y)
TVHEADEND_DEPENDENCIES     += zlib
endif

ifeq ($(BR2_PACKAGE_LIBCURL),y)
TVHEADEND_DEPENDENCIES     += curl
else
TVHEADEND_CONFIGURE_OPTS   += --disable-imagecache
endif

define TVHEADEND_INSTALL_TARGET_CMDS
	$(INSTALL) -D package/thirdparty/tvheadend/S92tvheadend $(TARGET_DIR)/etc/init.d/S92tvheadend
endef
$(eval $(call AUTOTARGETS,package/thirdparty,tvheadend))
