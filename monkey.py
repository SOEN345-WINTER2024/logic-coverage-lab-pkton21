# Imports the monkeyrunner modules used by this program.
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object.
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# whether the installation worked.
device.installPackage('/Users/khanhton/Documents/SOEN345/AndroidApps/mp1-pkton21/BasicCalculator/app/build/intermediates/apk/debug/app-debug.apk')

# Sets a variable with the package's internal name.
package = 'com.bradteachescode.basiccalculator'

# Sets a variable with the name of an Activity in the package.
activity = 'com.bradteachescode.basiccalculator.MainActivity'

# Sets the name of the component to start.
runComponent = package + '/' + activity

# Runs the component.
device.startActivity(component=runComponent)

MonkeyRunner.sleep(5)

# Presses the Menu button.
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

device.touch(140, 1080, MonkeyDevice.DOWN_AND_UP)

device.touch(140, 900, MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot.
result = device.takeSnapshot()

# Writes the screenshot to a file.
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot1.png','png')

device.touch(420, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot2.png','png')

device.touch(680, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot3.png','png')

device.touch(140, 720, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot4.png','png')

device.touch(420, 720, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot5.png','png')

device.touch(680, 720, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot6.png','png')

device.touch(140, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot7.png','png')

device.touch(420, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot8.png','png')

device.touch(680, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot9.png','png')

device.touch(420, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/shot0.png','png')

device.touch(140, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/clearButton.png','png')

# For the addition operation
device.touch(420, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/addition1.png','png')

device.touch(960, 1080, MonkeyDevice.DOWN_AND_UP)

device.touch(680, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/addition2.png','png')

device.touch(680, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/addition3.png','png')

# Clearing
device.touch(140, 1080, MonkeyDevice.DOWN_AND_UP)

# For the subtraction operation
device.touch(420, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/subtraction1.png','png')

device.touch(960, 900, MonkeyDevice.DOWN_AND_UP)

device.touch(680, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/subtraction2.png','png')

device.touch(680, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/subtraction3.png','png')

# Clearing
device.touch(140, 1080, MonkeyDevice.DOWN_AND_UP)

# For the division operation
device.touch(420, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/division1.png','png')

device.touch(960, 720, MonkeyDevice.DOWN_AND_UP)

device.touch(680, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/division2.png','png')

device.touch(680, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/division3.png','png')

# Clearing
device.touch(140, 1080, MonkeyDevice.DOWN_AND_UP)

# For the multiplication operation
device.touch(420, 900, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/mul1.png','png')

device.touch(960, 540, MonkeyDevice.DOWN_AND_UP)

device.touch(680, 540, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/mul2.png','png')

device.touch(680, 1080, MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('/Users/khanhton/Documents/SOEN345/AndroidApps/MonkeyRunner/mul3.png','png')