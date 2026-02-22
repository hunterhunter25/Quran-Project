[app]
# (str) Title of your application
title = قران كريم

# (str) Package name
package.name = quran_ayed

# (str) Package domain (needed for android packaging)
package.domain = org.ayed

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,sdl2_image,sdl2_ttf,sdl2_mixer,gst_python

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WAKE_LOCK

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (str) Android entry point
android.entrypoint = main.py

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
