# The android version that we're targeting this application to run on
TARGET_ANDROID_VERSION = 10

# Release type differentiates the experimental and stable features
# Possible values are [ 'production', 'development' ]
RELEASE_TYPE = "production"

# Fetch Package is the package you wish to pull from your device
# Possible Values are ['core', 'basic', 'omni', 'stock', 'full', 'ultra', 'addons', 'addonsets', '<addon>' (for e.g 'YouTube')]
FETCH_PACKAGE = "full"

# This will help fetch the files which requires root access such as overlay files
ADB_ROOT_ENABLED = False

# DEBUG_MODE will be helpful in printing more stuff so program can be debugged
DEBUG_MODE = True
if RELEASE_TYPE.__eq__("production"):
    DEBUG_MODE = False
