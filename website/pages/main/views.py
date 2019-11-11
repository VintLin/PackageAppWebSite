from flask import render_template
from . import main
from .form import *

permissions = [
    "ACCESS_LOCATION_EXTRA_COMMANDS",
    "ACCESS_NETWORK_STATE",
    "ACCESS_NOTIFICATION_POLICY",
    "ACCESS_WIFI_STATE",
    "BLUETOOTH",
    "BLUETOOTH_ADMIN",
    "BROADCAST_STICKY",
    "CHANGE_NETWORK_STATE",
    "CHANGE_WIFI_MULTICAST_STATE",
    "CHANGE_WIFI_STATE",
    "DISABLE_KEYGUARD",
    "EXPAND_STATUS_BAR",
    "GET_PACKAGE_SIZE",
    "INSTALL_SHORTCUT",
    "INTERNET",
    "KILL_BACKGROUND_PROCESSES",
    "MODIFY_AUDIO_SETTINGS",
    "NFC",
    "READ_SYNC_SETTINGS",
    "READ_SYNC_STATS",
    "RECEIVE_BOOT_COMPLETED",
    "REORDER_TASKS",
    "REQUEST_IGNORE_BATTERY_OPTIMIZATIONS",
    "REQUEST_INSTALL_PACKAGES",
    "SET_ALARM",
    "SET_TIME_ZONE",
    "SET_WALLPAPER",
    "SET_WALLPAPER_HINTS",
    "TRANSMIT_IR",
    "UNINSTALL_SHORTCUT",
    "USE_FINGERPRINT",
    "VIBRATE",
    "WAKE_LOCK",
    "WRITE_SYNC_SETTINGS",
]


@main.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        wd = form.input.data
        permissions.append(wd)
    return render_template('/main/index.html', permissions=permissions, input_form=form)


@main.route('/permissions/<index>', methods=['GET'])
def delete_permission(index):
    permissions.remove(permissions[int(index)])
    return "Success"
