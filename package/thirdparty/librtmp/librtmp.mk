#############################################################
#
#librtmp
#
#############################################################
LIBRTMP_VERSION = 5ba573a97122d7844b907a34f98d2b120e97070c
LIBRTMP_SITE_METHOD = git
LIBRTMP_SITE = git://git.ffmpeg.org/rtmpdump
LIBRTMP_INSTALL_STAGING = YES
LIBRTMP_INSTALL_TARGET = YES
LIBRTMP_DEPENDENCIES = openssl

define LIBRTMP_BUILD_CMDS
	sed -ie "s|prefix=/usr/local|prefix=/usr|" $(@D)/librtmp/Makefile
        sed -ie "s|prefix=/usr/local|prefix=/usr|" $(@D)/Makefile
	$(MAKE) CC="$(TARGET_CC)" LD="$(TARGET_LD)" AR="$(TARGET_AR)" -C $(@D)/librtmp
	$(MAKE) CC="$(TARGET_CC)" LD="$(TARGET_LD)" AR="$(TARGET_AR)" -C $(@D)
endef

define LIBRTMP_INSTALL_STAGING_CMDS
	$(MAKE) -C $(@D)/librtmp install DESTDIR=$(STAGING_DIR)
	$(MAKE) -C $(@D) install DESTDIR=$(STAGING_DIR)
endef

define LIBRTMP_INSTALL_TARGET_CMDS
	install -m 644 $(@D)/librtmp/librtmp.so.0 $(TARGET_DIR)/usr/lib
	install -m 644 $(@D)/rtmpdump $(TARGET_DIR)/usr/bin
	install -m 644 $(@D)/rtmpgw $(TARGET_DIR)/usr/bin
	install -m 644 $(@D)/rtmpsrv $(TARGET_DIR)/usr/bin
	install -m 644 $(@D)/rtmpsuck $(TARGET_DIR)/usr/bin
endef

$(eval $(call GENTARGETS,package/thirdparty,librtmp))
