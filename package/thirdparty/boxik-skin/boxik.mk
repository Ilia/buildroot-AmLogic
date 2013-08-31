BOXIK_VERSION = 4763cdc8872f80ccfad11c811517cf9a0c02d87a
BOXIK_SITE_METHOD = git
BOXIK_SITE = git://github.com/Ilia/skin.boxik.git
BOXIK_INSTALL_STAGING = YES
BOXIK_INSTALL_TARGET = YES
BOXIK_DEPENDENCIES = xbmc
TEXTURE_PACKER=$(XBMC_DIR)/tools/TexturePacker/TexturePacker

define BOXIK_BUILD_CMDS
	$(TEXTURE_PACKER) -use_none -i $(@D)/media -o $(@D)/media/Textures.xbt
endef

define BOXIK_INSTALL_STAGING_CMDS
        mkdir -p $(STAGING_DIR)/usr/share/xbmc/addons/skin.boxik
        cp -rf $(@D)/* $(STAGING_DIR)/usr/share/xbmc/addons/skin.boxik/
endef

define BOXIK_INSTALL_TARGET_CMDS
	mkdir -p $(TARGET_DIR)/usr/share/xbmc/addons/skin.boxik/media
	cd $(@D); cp -rf `ls -I media -1` $(TARGET_DIR)/usr/share/xbmc/addons/skin.boxik
	cp -f $(@D)/media/Textures.xbt $(TARGET_DIR)/usr/share/xbmc/addons/skin.boxik/media
endef

$(eval $(call GENTARGETS,package/thirdparty,boxik))
