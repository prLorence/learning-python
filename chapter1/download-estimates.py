import math

downloadSize = float(input("Enter the download size: "))
downloadSpeed = float(input("Enter the download speed: "))
downloadedContent = float(input("Enter the downloaded size: "))

megabits = 8


remainingSize = float(downloadedContent / downloadSize)
progressInPercent = remainingSize * 100
remaining = downloadSize - downloadedContent
remainingInMegaBits = remaining * megabits


time = float(remainingInMegaBits / downloadSpeed)
hours = 0.0
minutes = float(math.floor(time / 60))
seconds = float(time % 60)

print("Progress: {0} / {1} MB ({2}%), Remaining: {3} MB, {4}h {5}m {6}s".format(downloadedContent, downloadSize, progressInPercent, remaining, hours, minutes, seconds))
